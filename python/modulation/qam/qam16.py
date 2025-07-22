import numpy as np
import matplotlib.pyplot as plt


def bits_to_16qam(bits):
	# Pad bits if not a multiple of 4
	if len(bits) % 4 != 0:
		bits = np.append(bits, [0] * (4 - len(bits) % 4))

	symbols = []
	for i in range(0, len(bits), 4):
		b = bits[i:i + 4]

		# Gray-coded or natural - here we're doing natural binary for simplicity
		i_val = (b[0] << 1) | b[1]  # First two bits
		q_val = (b[2] << 1) | b[3]  # Next two bits

		# Map 2-bit values to levels: 00 -> -3, 01 -> -1, 10 -> +1, 11 -> +3
		level_map = [-3, -1, +3, +1]  # You can change to [−3, −1, +1, +3] for standard Gray mapping
		I = level_map[i_val]
		Q = level_map[q_val]
		symbols.append(complex(I, Q))

	# Normalize average power to 1
	symbols = np.array(symbols)
	symbols /= np.sqrt((np.mean(np.abs(symbols) ** 2)))

	return symbols


def plot_constellation(symbols, title="16-QAM Constellation"):
	plt.figure(figsize=(6, 6))
	plt.plot(symbols.real, symbols.imag, 'ro')
	plt.axhline(0, color='gray', lw=1)
	plt.axvline(0, color='gray', lw=1)
	plt.grid(True)
	plt.title(title)
	plt.xlabel("In-Phase (I)")
	plt.ylabel("Quadrature (Q)")
	plt.xlim(-4, 4)
	plt.ylim(-4, 4)
	plt.gca().set_aspect('equal', adjustable='box')
	plt.show()


def add_awgn_noise(symbols, snr_db):
	"""
    Add AWGN noise to a complex baseband signal.
    snr_db: Signal-to-noise ratio per symbol in dB
    """
	snr_linear = 10 ** (snr_db / 10)
	symbol_power = np.mean(np.abs(symbols) ** 2)
	noise_power = symbol_power / snr_linear

	# Generate complex Gaussian noise
	noise = np.sqrt(noise_power / 2) * (np.random.randn(*symbols.shape) + 1j * np.random.randn(*symbols.shape))
	return symbols + noise


np.random.seed(0)
bits = np.random.randint(0, 2, 400)
qam16 = bits_to_16qam(bits)
plot_constellation(qam16)

snr_values = [20, 10, 5]  # dB
for snr_db in snr_values:
	noisy_symbols = add_awgn_noise(qam16, snr_db)
	plot_constellation(noisy_symbols, title=f"16-QAM with AWGN (SNR = {snr_db} dB)")
