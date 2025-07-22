import numpy as np
import matplotlib.pyplot as plt

def generate_qpsk_symbols(num_symbols):
    bits = np.random.randint(0, 2, (num_symbols, 2))
    symbols = (2 * bits[:, 0] - 1) + 1j * (2 * bits[:, 1] - 1)
    symbols /= np.sqrt(2)  # normalize energy
    return symbols

def add_awgn(symbols, snr_db):
    snr_linear = 10 ** (snr_db / 10)
    noise_power = 1 / (2 * snr_linear)
    noise = np.sqrt(noise_power) * (np.random.randn(*symbols.shape) + 1j * np.random.randn(*symbols.shape))
    return symbols + noise

def apply_rotation(symbols, rotation_deg):
    theta = np.deg2rad(rotation_deg)
    return symbols * np.exp(1j * theta)

def visualize_qpsk_noise_and_rotation():
    num_symbols = 1000
    snr_db = 10
    rotation_deg = 30

    original = generate_qpsk_symbols(num_symbols)
    noisy = add_awgn(original, snr_db)
    rotated = apply_rotation(original, rotation_deg)

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.title(f'QPSK with AWGN (SNR = {snr_db} dB)')
    plt.scatter(noisy.real, noisy.imag, alpha=0.5, color='blue', label='Noisy symbols')
    plt.scatter(original.real, original.imag, color='red', label='Ideal symbols', marker='x')
    plt.xlabel('In-phase (I)')
    plt.ylabel('Quadrature (Q)')
    plt.grid(True)
    plt.axis('equal')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.title(f'QPSK with {rotation_deg}° Rotation')
    plt.scatter(rotated.real, rotated.imag, color='purple', alpha=0.5, label='Rotated symbols')
    plt.scatter(original.real, original.imag, color='red', marker='x', label='Ideal symbols')
    plt.xlabel('In-phase (I)')
    plt.ylabel('Quadrature (Q)')
    plt.grid(True)
    plt.axis('equal')
    plt.legend()

    plt.tight_layout()
    plt.show()

visualize_qpsk_noise_and_rotation()