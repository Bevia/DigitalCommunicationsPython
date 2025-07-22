🧱 16-QAM Modulator (Gray-coded)

🔹 Step 1: Mapping 4 Bits → One Complex Symbol

### what we have in code:

	•	QPSK modulator with Gray coding
	•	16-QAM modulator with normalized power
	•	Constellation plotting for both

add White Gaussian Noise (WGN) to your 16-QAM signal so you can simulate a noisy communication channel — 
and then visualize how the constellation gets corrupted with increasing noise levels.

⸻

✅ Additive White Gaussian Noise (AWGN) Channel

We’ll use the following model:

y = x + n

Where:
	•	x is the transmitted QAM symbol.
	•	n is complex Gaussian noise: n = n_I + j \cdot n_Q
	•	The noise power is related to the desired Eb/N0 (energy per bit to noise power spectral density).

✅ Expected Visuals
	•	20 dB SNR: Symbols still tightly clustered — small cloud around each constellation point.
	•	10 dB: More spread, but still separable.
	•	5 dB: Clear overlap begins, risk of symbol error.