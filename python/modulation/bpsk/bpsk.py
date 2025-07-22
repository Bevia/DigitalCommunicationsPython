import numpy as np
import matplotlib.pyplot as plt

# Parameters
bit_rate = 100  # bits per second
fc = 1000       # carrier frequency in Hz
fs = 10000      # samples per second
bit_duration = 1 / bit_rate
samples_per_bit = int(fs * bit_duration)

# Bitstream (random or fixed)
np.random.seed(0)
bitstream = np.random.randint(0, 2, 10)
print("Bitstream:", bitstream)


def bpsk_modulate(bits, fc, fs, samples_per_bit):
    t = np.arange(0, len(bits) * samples_per_bit) / fs
    carrier = np.cos(2 * np.pi * fc * t)
    bit_values = np.repeat(2 * bits - 1, samples_per_bit)  # Map 0→-1, 1→+1
    return bit_values * carrier, t

def bpsk_demodulate(signal, bits, fc, fs, samples_per_bit):
    recovered_bits = []
    for i in range(len(bits)):
        start = i * samples_per_bit
        end = start + samples_per_bit
        t = np.arange(start, end) / fs
        carrier = np.cos(2 * np.pi * fc * t)
        product = signal[start:end] * carrier
        # Integrate over bit duration (i.e., sum the product)
        recovered_bit = 1 if np.sum(product) > 0 else 0
        recovered_bits.append(recovered_bit)
    return np.array(recovered_bits)


modulated_signal, t = bpsk_modulate(bitstream, fc, fs, samples_per_bit)
recovered_bits = bpsk_demodulate(modulated_signal, bitstream, fc, fs, samples_per_bit)


def get_bpsk_symbols(signal, fc, fs, samples_per_bit):
    symbols = []
    for i in range(0, len(signal), samples_per_bit):
        segment = signal[i:i + samples_per_bit]
        t = np.arange(0, len(segment)) / fs
        # Mix with local oscillator (in-phase and quadrature)
        I = np.sum(segment * np.cos(2 * np.pi * fc * t))
        Q = np.sum(segment * np.sin(2 * np.pi * fc * t))  # Should be ~0 in BPSK
        symbols.append(complex(I, Q))
    return np.array(symbols)

def plot_constellation(symbols, title="Constellation Diagram"):
    plt.figure(figsize=(5, 5))
    plt.plot(symbols.real, symbols.imag, 'bo')
    plt.axhline(0, color='gray', lw=1)
    plt.axvline(0, color='gray', lw=1)
    plt.title(title)
    plt.xlabel('In-Phase (I)')
    plt.ylabel('Quadrature (Q)')
    plt.grid(True)
    plt.axis('equal')
    plt.show()


def add_awgn(signal, snr_db):
    sig_power = np.mean(signal ** 2)
    snr_linear = 10 ** (snr_db / 10)
    noise_power = sig_power / snr_linear
    noise = np.random.normal(0, np.sqrt(noise_power), signal.shape)
    return signal + noise

# Plotting
plt.figure(figsize=(12, 5))
plt.plot(t, modulated_signal)
plt.title("BPSK Modulated Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()

print("Recovered bits:", recovered_bits)
print("Bit errors:", np.sum(recovered_bits != bitstream))

symbols = get_bpsk_symbols(modulated_signal, fc, fs, samples_per_bit)
plot_constellation(symbols)

noisy_signal = add_awgn(modulated_signal, snr_db=5)
symbols = get_bpsk_symbols(noisy_signal, fc, fs, samples_per_bit)
plot_constellation(symbols, title="BPSK Constellation with Noise")