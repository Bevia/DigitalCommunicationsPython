import numpy as np
from modulation.qam16 import add_awgn_noise


def generate_bits(num_bits):
    return np.random.randint(0, 2, num_bits)


def bits_to_symbols(bits):
    bit_groups = bits.reshape((-1, 4))  # 4 bits per symbol for 16-QAM
    mapping = {
        (0, 0): -3, (0, 1): -1, (1, 1): 1, (1, 0): 3
    }
    I = np.array([mapping[tuple(b[:2])] for b in bit_groups])
    Q = np.array([mapping[tuple(b[2:])] for b in bit_groups])
    return I + 1j * Q


def symbols_to_bits(symbols):
    decision_levels = [-2, 0, 2]  # midpoint thresholds
    def decide(val):
        if val < -2: return (0, 0)
        elif val < 0: return (0, 1)
        elif val < 2: return (1, 1)
        else: return (1, 0)

    bits = []
    for sym in symbols:
        i_bits = decide(np.real(sym))
        q_bits = decide(np.imag(sym))
        bits.extend(i_bits + q_bits)
    return np.array(bits)


def compute_ber(original_bits, received_bits):
    errors = np.sum(original_bits != received_bits)
    return errors / len(original_bits)


def simulate_16qam_ber(num_bits=10000, snr_range=range(0, 21, 2)):
    bers = []

    bits = generate_bits(num_bits)
    symbols = bits_to_symbols(bits)

    for snr_db in snr_range:
        noisy = add_awgn_noise(symbols, snr_db)
        received_bits = symbols_to_bits(noisy)
        ber = compute_ber(bits[:len(received_bits)], received_bits)
        bers.append(ber)
        print(f"SNR {snr_db} dB: BER = {ber:.6f}")

    return snr_range, bers
