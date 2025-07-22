import matplotlib.pyplot as plt
from ber_sim import simulate_16qam_ber

snrs, bers = simulate_16qam_ber()

plt.semilogy(snrs, bers, marker='o')
plt.grid(True, which='both')
plt.xlabel('SNR (dB)')
plt.ylabel('Bit Error Rate (BER)')
plt.title('16-QAM BER vs SNR with AWGN')
plt.show()