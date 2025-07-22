
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