import numpy as np
import matplotlib.pyplot as plt

def bits_to_qpsk(bits):
    if len(bits) % 2 != 0:
        bits = np.append(bits, 0)  # pad to even length

    symbols = []
    for i in range(0, len(bits), 2):
        b1, b2 = bits[i], bits[i+1]
        # Gray-coded mapping:
        if (b1, b2) == (0, 0):
            s = 1 + 1j
        elif (b1, b2) == (0, 1):
            s = -1 + 1j
        elif (b1, b2) == (1, 1):
            s = -1 - 1j
        elif (b1, b2) == (1, 0):
            s = 1 - 1j
        symbols.append(s / np.sqrt(2))  # normalize to unit power
    return np.array(symbols)

def plot_constellation(symbols, title="Constellation"):
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


np.random.seed(42)
bitstream = np.random.randint(0, 2, 20)
symbols = bits_to_qpsk(bitstream)
plot_constellation(symbols, title="QPSK Constellation")