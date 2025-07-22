import numpy as np
import matplotlib.pyplot as plt

# Define Gray-coded 16-QAM constellation
qam16_lut = {
    '0000': -3 + 3j, '0001': -3 + 1j, '0011': -3 - 1j, '0010': -3 - 3j,
    '0100': -1 + 3j, '0101': -1 + 1j, '0111': -1 - 1j, '0110': -1 - 3j,
    '1100':  1 + 3j, '1101':  1 + 1j, '1111':  1 - 1j, '1110':  1 - 3j,
    '1000':  3 + 3j, '1001':  3 + 1j, '1011':  3 - 1j, '1010':  3 - 3j,
}

qam16_lut = {k: v / np.sqrt(10) for k, v in qam16_lut.items()}  # unit power


# To modulate:
def bits_to_symbols(bits, lut):
    symbols = []
    for i in range(0, len(bits), 4):
        chunk = ''.join(map(str, bits[i:i+4]))
        symbols.append(lut[chunk])
    return np.array(symbols)


# reverse LUT for demodulation:
inv_qam16_lut = {v: k for k, v in qam16_lut.items()}


def demodulate(symbols, lut):
    constellation = np.array(list(lut.values()))
    bit_patterns = list(lut.keys())
    bits = []
    for sym in symbols:
        idx = np.argmin(np.abs(sym - constellation))
        bits.extend([int(b) for b in bit_patterns[idx]])
    return bits


# Plotting the 16-QAM Constellation
def plot_qam_constellation(lut):
    plt.figure(figsize=(6, 6))
    for bits, symbol in lut.items():
        plt.plot(symbol.real, symbol.imag, 'bo')
        plt.text(symbol.real + 0.05, symbol.imag + 0.05, bits, fontsize=9)

    plt.axhline(0, color='gray', lw=0.5)
    plt.axvline(0, color='gray', lw=0.5)
    plt.grid(True)
    plt.xlabel('In-Phase (I)')
    plt.ylabel('Quadrature (Q)')
    plt.title('16-QAM Constellation (Gray-coded)')
    plt.axis('equal')
    plt.show()

plot_qam_constellation(qam16_lut)