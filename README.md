# 🛰️ Digital Modulation Toolkit

A Python-based toolkit to simulate, visualize, and analyze digital modulation schemes. Ideal for signal processing learners, engineers, and researchers.

> Supports QPSK, 16-QAM, AWGN channel modeling, BER analysis, and constellation visualization. More schemes like 32-QAM, 128-QAM, and OFDM coming soon!

---

## 📡 Features

- ✅ **QPSK** Modulation/Demodulation
- ✅ **16-QAM** with Constellation Mapping
- ✅ **AWGN Simulation** with configurable SNR
- ✅ **BER Calculation** across SNR range
- ✅ **Constellation Plots** (ideal, noisy, rotated)
- 🚧 **OFDM** (Coming soon)
- 🚧 **32-QAM, 64-QAM, 128-QAM** Support (Planned)

🎯 Roadmap 
- QPSK with BER and noise visualization 
- QAM basic implementation 
  - 4QAM, 16QAM, 32QAM, 64-QAM, 128-QAM 
  - OFDM simulation with FFT/IFFT 
  - Channel modeling (multipath, fading, Doppler)
  - CLI tool or Web dashboard


📚 Digital Communications / Coding Theory
`Subtopics`:
- Forward Error Correction (FEC):
- convolutional codes → Viterbi algorithm, trellis decoding 
- block codes → Reed-Solomon, Hamming codes, LDPC, BCH 
- Decoding Algorithms:
  - Viterbi (for convolutional codes)
  - Berlekamp-Massey (for Reed-Solomon)
  - Modulation and Coding Schemes (MCS):
    - Combined use of modulation (QAM, PSK) with coding 
    - Channel Capacity & Noise Modeling:
    - AWGN, Rayleigh fading, etc.

⸻

Modulation techniques like QAM (Quadrature Amplitude Modulation) are critical in satellite communication systems because they directly impact data rate, bandwidth efficiency, and robustness against noise and interference. Here’s a concise breakdown:

⸻

✅ Modulation Matters in Satellite Modems

1. Efficient Use of Bandwidth
	•	Satellites operate over limited spectrum (e.g., Ku, Ka bands), so using higher-order modulations like 16-QAM, 64-QAM allows transmitting more bits per symbol.
	•	This increases data throughput without needing more bandwidth.

2. Trade-off Between Data Rate and Robustness
	•	QPSK (4-QAM) is more robust to noise and phase distortions (important for long-distance satellite links with weak signals).
	•	16-QAM or higher increases data rates but is more susceptible to errors, so it’s typically used under good SNR conditions.

3. Adaptive Modulation
	•	Many satellite modems use adaptive modulation, adjusting between QPSK, 8-PSK, 16-QAM, etc., depending on link quality (e.g., rain fade in Ka-band).
	•	This ensures maximum efficiency and link reliability.

4. Demodulation at Receiver
	•	Satellite receivers need to demodulate signals accurately even with impairments like:
	•	Doppler shift
	•	Phase noise from LNB/oscillators
	•	Non-linearities from power amplifiers

Hence, modulation schemes are designed to be resilient and recoverable under these conditions.

⸻

🛰️ Summary:

QAM and related modulation techniques are the foundation of reliable and efficient satellite communications, enabling high-speed data transfer while adapting to harsh and variable space link conditions.

Let me know if you want a comparison chart between QPSK, 8PSK, and 16-QAM for satellite use.

🤝 Contributing

Pull requests are welcome! Whether you’re fixing a bug, adding a new scheme, or improving visualizations — all help is appreciated.
	1.	Fork the repo
	2.	Create your feature branch: git checkout -b feature/qam32
	3.	Commit your changes
	4.	Push and open a PR

⸻

📘 License

This project is licensed under the MIT License. See LICENSE for details.

⸻

📡 About the Author

👋 Created by Vincent Bevia — a senior software engineer and DSP enthusiast.

Worked as a Telecommunication Engineer at EFData and Fairchild with hands-on experience in satellite system engineering, signal processing, and communications link analysis.

Feel free to reach out for feedback, suggestions, or collaboration!
