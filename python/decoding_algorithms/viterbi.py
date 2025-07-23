import numpy as np


def int_to_bits(x, width):
    return [int(b) for b in format(x, f'0{width}b')]


def conv_encode(bits, g=[0b111, 0b101]):
    """Rate 1/2 convolutional encoder with 3-bit constraint length."""
    K = 3  # Constraint length
    state = [0] * (K - 1)
    encoded = []

    for b in bits:
        current = [b] + state
        for poly in g:
            bits_to_xor = [a & b for a, b in zip(int_to_bits(poly, K), current)]
            encoded.append(sum(bits_to_xor) % 2)
        state = [b] + state[:-1]

    return np.array(encoded)


def add_awgn_noise(encoded_bits, snr_db):
    # Map bits: 0 → +1, 1 → -1
    bpsk_signal = 1 - 2 * encoded_bits

    # Calculate signal power and noise power
    snr_linear = 10**(snr_db / 10)
    signal_power = 1  # Since BPSK symbols are ±1
    noise_power = signal_power / snr_linear

    # Generate Gaussian noise
    noise = np.sqrt(noise_power / 2) * np.random.randn(len(bpsk_signal))

    # Add noise
    noisy_signal = bpsk_signal + noise
    return noisy_signal


def viterbi_decode(received_bits, g=[0b111, 0b101]):
    K = 3
    n = len(g)
    num_states = 2 ** (K - 1)

    # Trellis initialization
    path_metrics = [float('inf')] * num_states
    path_metrics[0] = 0  # Start at state 0
    paths = [[] for _ in range(num_states)]

    for i in range(0, len(received_bits), n):
        recv = received_bits[i:i+n]
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

                    metric = sum([a != b for a, b in zip(output, recv)])
                    total_metric = path_metrics[state] + metric

                    if total_metric < new_metrics[next_state]:
                        new_metrics[next_state] = total_metric
                        new_paths[next_state] = paths[state] + [bit]

        path_metrics = new_metrics
        paths = new_paths

    best_state = np.argmin(path_metrics)
    return np.array(paths[best_state])


def viterbi_decode_soft(received_signal, g=[0b111, 0b101]):
    K = 3
    n = len(g)
    num_states = 2 ** (K - 1)

    path_metrics = [float('inf')] * num_states
    path_metrics[0] = 0
    paths = [[] for _ in range(num_states)]

    for i in range(0, len(received_signal), n):
        recv = received_signal[i:i+n]
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
                        output.append(1 - 2 * (sum(bits_to_xor) % 2))  # Convert 0→+1, 1→-1

                    # Use squared Euclidean distance between recv and expected output
                    metric = np.sum((np.array(output) - recv)**2)
                    total_metric = path_metrics[state] + metric

                    if total_metric < new_metrics[next_state]:
                        new_metrics[next_state] = total_metric
                        new_paths[next_state] = paths[state] + [bit]

        path_metrics = new_metrics
        paths = new_paths

    best_state = np.argmin(path_metrics)
    return np.array(paths[best_state])


# 1. Generate random bits
np.random.seed(42)
input_bits = np.random.randint(0, 2, 20)

# 2.  Encode them
encoded = conv_encode(input_bits)

print("Input bits:   ", input_bits)
print("Encoded bits: ", encoded)

# 3. Add AWGN noise
snr_db = 3
noisy_signal = add_awgn_noise(encoded, snr_db)

# 4. Hard-decision (for hard Viterbi)
received_bits = (noisy_signal < 0).astype(int)

# 5. Decode
# decoded_bits = viterbi_decode(received_bits)

# 4. Decode using soft-decision
decoded_bits = viterbi_decode_soft(noisy_signal)

# 6. BER
min_len = min(len(input_bits), len(decoded_bits))
bit_errors = np.sum(input_bits[:min_len] != decoded_bits[:min_len])
ber = bit_errors / min_len

print(f"Bit Error Rate (BER): {ber:.4f}")