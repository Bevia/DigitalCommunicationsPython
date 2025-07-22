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

⸻

🛰️ Use Cases
📡 1. Wireless Communications (Wi-Fi, LTE, 5G)
	•	Wi-Fi (IEEE 802.11a/g/n/ac/ax): 16-QAM is commonly used in medium to high data rate modes.
	•	4G LTE: LTE uses adaptive modulation; it dynamically switches between QPSK, 16-QAM, and 64-QAM depending on signal quality.
	•	5G NR (New Radio): Higher QAM levels like 256-QAM and 1024-QAM are used, but 16-QAM still plays a role under moderate SNR conditions.
✅ Why: Improves data rates without drastically increasing error rates in decent SNR conditions.

🛰️ 2. Digital TV and Satellite Systems
	•	Used in systems like DVB (Digital Video Broadcasting):
	•	DVB-C (Cable)
	•	DVB-T (Terrestrial)
	•	DVB-S (Satellite)
✅ Why: Offers better spectral efficiency than QPSK, ideal for fixed-point broadcasting where SNR is manageable.

📞 3. Cable Modems (DOCSIS Standards)
	•	Used in DOCSIS (Data Over Cable Service Interface Specification) for broadband cable internet.
	•	Earlier DOCSIS versions use 16-QAM for upstream and downstream channels.
✅ Why: Allows higher throughput over existing coaxial infrastructure.

📡 4. Software Defined Radio (SDR) & Research
	•	Frequently used in simulations, educational tools, and SDR platforms like GNU Radio or MATLAB.
	•	Ideal for learning modulation trade-offs between data rate and error performance.
✅ Why: A clear step-up from QPSK for teaching the impact of amplitude + phase modulation.

📊 5. Microwave and Fixed Wireless Links
	•	Used in point-to-point microwave links for backhaul (e.g., mobile base station to network).
	•	Higher QAM levels (up to 1024-QAM) are used, but 16-QAM is a fallback for reliability under fading conditions.
✅ Why: Efficient use of spectrum with controlled SNR environments.

🔒 6. Modems and Legacy Systems
	•	DSL modems (e.g., ADSL, VDSL) often used 16-QAM and 64-QAM as part of their multicarrier schemes.
✅ Why: Allows dynamic adjustment of modulation based on line quality per subcarrier.