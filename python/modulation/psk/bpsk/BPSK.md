📡 What is BPSK (Binary Phase Shift Keying)?
	•	Modulation: Transmits bits as phase changes (0 → 0°, 1 → 180°)
	•	Mapping:
	•	Bit 0 → +1 (cos(ωt))
	•	Bit 1 → -1 (cos(ωt + π) = -cos(ωt))

🔎 Output:

You’ll see:
	•	A modulated carrier with ±cos(ωt) flips depending on bits.
	•	Recovered bitstream from coherent demodulation.
	•	Zero or few bit errors (if no noise added).

💡 What is a Constellation Diagram?

A plot of complex symbols (I/Q values) transmitted or received. For BPSK:
	•	Bit 0 → +1 (real axis)
	•	Bit 1 → -1 (real axis)

So BPSK lives only on the real axis, but plotting helps:
	•	Debug modulation/demod
	•	Visualize channel noise
	•	Validate symbol timing