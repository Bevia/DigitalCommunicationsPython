
🔧 What’s a Lookup Table (LUT) in this context?

A LUT stores precomputed complex symbols for each bit pattern in a QAM constellation, allowing fast mapping of input bits to signal points (IQ pairs).

⸻

✅ Why use a LUT?
	•	Speeds up modulation (no real-time computation of coordinates).
	•	Easy to reuse and test.
	•	Reduces runtime complexity — just a dictionary or array access.

🔍 Notes:
	•	The LUT is normalized to unit average power (/ sqrt(10)), which is correct for simulation.
	•	This plot function labels each point with its corresponding bit pattern (from the LUT key).

✅ Definitions
	•	Phase Noise: A slow, random variation of the carrier phase (e.g., due to oscillator instability).
	•	Jitter: Typically refers to timing uncertainty, but in baseband IQ simulation, it can be modeled similarly 
to high-frequency phase variations (or sample offset if you’re modeling a full system).

In our case, we’ll simulate both as a random phase offset:
	•	Low-frequency phase noise → slow phase drift
	•	High-frequency phase noise (or jitter) → fast random phase changes per symbol