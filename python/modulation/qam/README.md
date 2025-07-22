✅ Definitions
	•	Phase Noise: A slow, random variation of the carrier phase (e.g., due to oscillator instability).
	•	Jitter: Typically refers to timing uncertainty, but in baseband IQ simulation, it can be modeled similarly 
to high-frequency phase variations (or sample offset if you’re modeling a full system).

In our case, we’ll simulate both as a random phase offset:
	•	Low-frequency phase noise → slow phase drift
	•	High-frequency phase noise (or jitter) → fast random phase changes per symbol