📡 Digital Communications & Error Correction

👤 Author

Vincent Bevia – POS Architect @ MultiSafepay | Former Telecom Engineer @ COMTECH (EFData) & Fairchild | Cryptography & Signal Processing Enthusiast

⸻

🧭 Overview

This project explores the fundamental principles and practical techniques of digital communication systems, focusing on modulation, channel models, and error correction coding using Python simulations and visualizations.

⸻

📁 Contents

1. 🧮 Modulation Techniques
	•	Binary Phase Shift Keying (BPSK)
	•	Quadrature Amplitude Modulation (QAM – 4-QAM, 16-QAM)
	•	Gray-coded Mapping
	•	Constellation Diagrams
	•	Signal with AWGN + Phase Noise

2. 📡 Channel Models
	•	Additive White Gaussian Noise (AWGN)
	•	Phase noise modeling
	•	Timing jitter (TBD)
	•	Fading channels (optional future section)

3. 🧬 Error Correction Coding

🔸 Convolutional Codes
	•	Encoding logic
	•	Trellis diagrams
	•	Viterbi algorithm
	•	Bit Error Rate (BER) simulation with/without noise

🔸 Block Codes
	•	Reed-Solomon codes (RS)
	•	Hamming codes
	•	Error detection & correction limits
	•	BER performance with noisy channels

🔸 Advanced Coding (optional/future)
	•	LDPC codes
	•	Turbo codes
	•	Polar codes

⸻

🧪 Simulations

Each notebook or module includes:

✅ Bit generation
✅ Modulation (e.g., 16-QAM)
✅ Noise injection (AWGN, phase noise)
✅ Demodulation
✅ Error correction (Viterbi, RS)
✅ Bit Error Rate (BER) analysis

⸻

🔧 Requirements
	•	Python 3.10+
	•	numpy, matplotlib, scipy, reedsolo, etc.

⸻

🚀 Getting Started

Clone the repo and run:

python qam_with_viterbi_sim.py

Or explore each section via Jupyter notebooks.

⸻

📚 References
	•	“Digital Communications” by John G. Proakis
	•	“Error Control Coding” by Lin & Costello
	•	ITU & DVB Standards for channel coding

⸻

🛠 Future Work
	•	Add soft-decision decoding
	•	Simulate fading and inter-symbol interference
	•	Build a GUI to visualize signal flow in real-time

⸻
