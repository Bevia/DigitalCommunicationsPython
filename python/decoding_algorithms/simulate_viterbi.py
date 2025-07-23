import numpy as np
import matplotlib.pyplot as plt


# -------------------------------
# Convolutional Encoder
# -------------------------------
def int_to_bits(x, width):
	return [int(b) for b in format(x, f'0{width}b')]


def conv_encode(bits, g=[0b111, 0b101]):
	K = 3
	state = [0] * (K - 1)
	encoded = []

	for bit in bits:
		current = [bit] + state
		for poly in g:
			bits_to_xor = [a & b for a, b in zip(int_to_bits(poly, K), current)]
			out_bit = sum(bits_to_xor) % 2
			encoded.append(out_bit)
		state = [bit] + state[:-1]

	return np.array(encoded)


# -------------------------------
# Add AWGN to BPSK-modulated signal
# -------------------------------
def add_awgn_noise(signal, snr_db):
	snr_linear = 10 ** (snr_db / 10)
	power = 1  # BPSK: symbols are +1 or -1
	noise_power = power / snr_linear
	noise = np.sqrt(noise_power / 2) * np.random.randn(len(signal))
	bpsk_signal = 1 - 2 * signal  # 0 → +1, 1 → -1
	return bpsk_signal + noise


# -------------------------------
# Hard-decision Viterbi Decoder
# -------------------------------
def viterbi_decode_hard(bits, g=[0b111, 0b101]):
	K = 3
	n = len(g)
	num_states = 2 ** (K - 1)

	path_metrics = [float('inf')] * num_states
	path_metrics[0] = 0
	paths = [[] for _ in range(num_states)]

	for i in range(0, len(bits), n):
		recv = bits[i:i + n]
		new_metrics = [float('inf')] * num_states
		new_paths = [[] for _ in range(num_states)]

		for state in range(num_states):
			if path_metrics[state] < float('inf'):
				for bit in [0, 1]:
					next_state = ((state << 1) | bit) & (num_states - 1)
					current = [bit] + int_to_bits(state, K - 1)
					output = []
					for poly in g:
						bits_to_xor = [a & b for a, b in zip(int_to_bits(poly, K), current)]
						output.append(sum(bits_to_xor) % 2)

					metric = sum([int(a != b) for a, b in zip(output, recv)])
					total_metric = path_metrics[state] + metric

					if total_metric < new_metrics[next_state]:
						new_metrics[next_state] = total_metric
						new_paths[next_state] = paths[state] + [bit]

		path_metrics = new_metrics
		paths = new_paths

	best_state = np.argmin(path_metrics)
	return np.array(paths[best_state])


# -------------------------------
# Soft-decision Viterbi Decoder
# -------------------------------
def viterbi_decode_soft(received_signal, g=[0b111, 0b101]):
	K = 3
	n = len(g)
	num_states = 2 ** (K - 1)

	path_metrics = [float('inf')] * num_states
	path_metrics[0] = 0
	paths = [[] for _ in range(num_states)]

	for i in range(0, len(received_signal), n):
		recv = received_signal[i:i + n]
		new_metrics = [float('inf')] * num_states
		new_paths = [[] for _ in range(num_states)]

		for state in range(num_states):
			if path_metrics[state] < float('inf'):
				for bit in [0, 1]:
					next_state = ((state << 1) | bit) & (num_states - 1)
					current = [bit] + int_to_bits(state, K - 1)
					output = []
					for poly in g:
						bits_to_xor = [a & b for a, b in zip(int_to_bits(poly, K), current)]
						bpsk = 1 - 2 * (sum(bits_to_xor) % 2)  # 0→+1, 1→-1
						output.append(bpsk)

					metric = np.sum((np.array(output) - recv) ** 2)
					total_metric = path_metrics[state] + metric

					if total_metric < new_metrics[next_state]:
						new_metrics[next_state] = total_metric
						new_paths[next_state] = paths[state] + [bit]

		path_metrics = new_metrics
		paths = new_paths

	best_state = np.argmin(path_metrics)
	return np.array(paths[best_state])


# -------------------------------
# BER simulation
# -------------------------------
def run_ber_test(snr_range_db, n_bits=500):
	hard_ber = []
	soft_ber = []

	np.random.seed(0)
	original_bits = np.random.randint(0, 2, n_bits)
	encoded = conv_encode(original_bits)

	for snr in snr_range_db:
		noisy_signal = add_awgn_noise(encoded, snr)
		hard_input = (noisy_signal < 0).astype(int)  # Hard decision

		decoded_hard = viterbi_decode_hard(hard_input)
		decoded_soft = viterbi_decode_soft(noisy_signal)

		min_len = min(len(decoded_hard), len(original_bits))
		ber_hard = np.sum(original_bits[:min_len] != decoded_hard[:min_len]) / min_len
		ber_soft = np.sum(original_bits[:min_len] != decoded_soft[:min_len]) / min_len

		hard_ber.append(ber_hard)
		soft_ber.append(ber_soft)
		print(f"SNR={snr} dB | BER Hard={ber_hard:.4f}, BER Soft={ber_soft:.4f}")

	return hard_ber, soft_ber


# -------------------------------
# Run and Plot
# -------------------------------
snr_range = list(range(0, 11))
ber_hard, ber_soft = run_ber_test(snr_range)

plt.semilogy(snr_range, ber_hard, 'o-', label='Hard Decision')
plt.semilogy(snr_range, ber_soft, 's-', label='Soft Decision')
plt.grid(True, which='both')
plt.xlabel('SNR (dB)')
plt.ylabel('Bit Error Rate (BER)')
plt.title('Viterbi BER Performance: Hard vs Soft Decision')
plt.legend()
plt.tight_layout()
plt.show()