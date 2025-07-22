import numpy as np
import matplotlib.pyplot as plt

# 4-QAM LUT (binary mapped, not Gray-coded)
qam4_lut = {
    '00': -1 - 1j,
    '01': -1 + 1j,
    '11':  1 + 1j,
    '10':  1 - 1j,
}
qam4_lut = {k: v / np.sqrt(2) for k, v in qam4_lut.items()}  # Normalize power
inv_qam4_lut = {v: k for k, v in qam4_lut.items()}


def plot_qam_constellation(lut, title='4-QAM Constellation'):
    plt.figure(figsize=(5, 5))
    for bits, symbol in lut.items():
        plt.plot(symbol.real, symbol.imag, 'bo')
        plt.text(symbol.real + 0.05, symbol.imag + 0.05, bits, fontsize=10)

    plt.axhline(0, color='gray', lw=0.5)
    plt.axvline(0, color='gray', lw=0.5)
    plt.grid(True)
    plt.xlabel('In-Phase (I)')
    plt.ylabel('Quadrature (Q)')
    plt.title(title)
    plt.axis('equal')
    plt.show()


plot_qam_constellation(qam4_lut)


# Modulation
def bits_to_symbols(bits, lut):
    symbols = []
    for i in range(0, len(bits), 2):
        chunk = ''.join(map(str, bits[i:i+2]))
        symbols.append(lut[chunk])
    return np.array(symbols)


# Demodulation (minimum distance)
def symbols_to_bits(symbols, lut):
    constellation = np.array(list(lut.values()))
    bit_patterns = list(lut.keys())
    bits = []
    for sym in symbols:
        idx = np.argmin(np.abs(sym - constellation))
        bits.extend([int(b) for b in bit_patterns[idx]])
    return np.array(bits)


# AWGN noise
def add_awgn(signal, snr_db):
    snr_linear = 10**(snr_db / 10)
    signal_power = np.mean(np.abs(signal)**2)
    noise_power = signal_power / snr_linear
    noise = np.sqrt(noise_power/2) * (np.random.randn(*signal.shape) + 1j * np.random.randn(*signal.shape))
    return signal + noise


# Add phase noise
def apply_phase_noise(signal, std_dev_rad):
    phase_noise = np.random.normal(0, std_dev_rad, len(signal))
    return signal * np.exp(1j * phase_noise)


# Simulation parameters
num_bits = 10000
snr_db = 10  # Change this to test different SNRs


# Parameters
phase_noise_std = 0.05  # Radians, try 0.05 for mild, or 0.2 for strong

# Generate random bits
tx_bits = np.random.randint(0, 2, num_bits)

# Modulate
tx_symbols = bits_to_symbols(tx_bits, qam4_lut)

# Apply phase noise (simulating jitter/LO instability)
tx_symbols_noisy = apply_phase_noise(tx_symbols, phase_noise_std)

# Add AWGN
rx_symbols = add_awgn(tx_symbols_noisy, snr_db)

# Demodulate
rx_bits = symbols_to_bits(rx_symbols, qam4_lut)


# plotting the constellation for different values of phase_noise_std:
for std in [0.0, 0.05, 0.1, 0.2, 0.3]:  # add or delete to see how phase noise affects the constellation
    rx_symbols = add_awgn(apply_phase_noise(tx_symbols, std), snr_db)
    # plot rx_symbols...


# Compute BER
num_bit_errors = np.sum(tx_bits != rx_bits)
ber = num_bit_errors / num_bits
print(f"SNR(dB): {snr_db}, Bit Errors: {num_bit_errors}, BER: {ber:.4e}")

# Optional: Plot received constellation
plt.figure(figsize=(6, 6))
plt.scatter(rx_symbols.real, rx_symbols.imag, color='red', alpha=0.4, s=10, label='Received Symbols')
plt.scatter([v.real for v in qam4_lut.values()], [v.imag for v in qam4_lut.values()],
            color='blue', s=50, marker='x', label='Ideal Constellation')
plt.axhline(0, color='gray', lw=0.5)
plt.axvline(0, color='gray', lw=0.5)
plt.grid(True)
plt.xlabel('In-phase (I)')
plt.ylabel('Quadrature (Q)')
plt.title(f'4-QAM Constellation with AWGN (SNR={snr_db} dB)')
plt.legend()
plt.axis('equal')
plt.show()