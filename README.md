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

## 📊 Example: QPSK with AWGN

```python
from qpsk.qpsk_modem import simulate_qpsk
simulate_qpsk(num_symbols=1000, snr_db=10, rotation_deg=30)

<p align="center">
  <img src="assets/qpsk_awgn_example.png" width="600" alt="QPSK with AWGN">
</p>



⸻

🛠️ Installation

git clone https://github.com/yourusername/digital-modulation-toolkit.git
cd digital-modulation-toolkit
pip install -r requirements.txt


⸻

🧪 Run Simulations

python examples/visualize_qpsk.py

Or use interactive Jupyter notebooks inside examples/.

⸻

🎯 Roadmap
	•	QPSK with BER and noise visualization
	•	16-QAM basic implementation
	•	32-QAM, 64-QAM, 128-QAM
	•	OFDM simulation with FFT/IFFT
	•	Channel modeling (multipath, fading, Doppler)
	•	CLI tool or Web dashboard

⸻

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
Feel free to reach out for feedback, suggestions, or collaboration!
