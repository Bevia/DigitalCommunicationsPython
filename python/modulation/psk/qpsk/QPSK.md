Here’s a solid overview of QPSK (Quadrature Phase Shift Keying) — 
a key modulation technique in digital communications:

⸻

📘 What is QPSK?

QPSK stands for Quadrature Phase Shift Keying. It’s a phase modulation technique where each symbol 
represents 2 bits of data. Instead of shifting just one phase like in BPSK (Binary Phase Shift Keying), 
QPSK uses four distinct phase shifts.

⸻

📐 How It Works
	•	QPSK encodes 2 bits per symbol, so the symbol set is:

Bits	Phase
00	45°
01	135°
11	225°
10	315°

(Note: These angles may vary by implementation — 0°, 90°, 180°, and 270° is another common mapping)

	•	The signal is represented as:
s(t) = \sqrt{\frac{2E_b}{T}} \cos(2\pi f_c t + \theta)
where \theta is one of the four phase angles above.

⸻

🧠 Why It’s Efficient
	•	More bits per symbol than BPSK → 2x bandwidth efficiency.
	•	Same energy per bit (compared to BPSK), with a similar error performance.
	•	Easy to implement using I/Q modulation:
s(t) = I(t) \cdot \cos(2\pi f_c t) - Q(t) \cdot \sin(2\pi f_c t)
where I(t) and Q(t) are the in-phase and quadrature components (usually ±1).

⸻

🛰️ Use Cases
	•	Wi-Fi (IEEE 802.11)
	•	GPS
	•	Cellular (4G/LTE)
	•	Satellite comms

⸻

🧪 BER (Bit Error Rate)
	•	In AWGN, the theoretical BER for QPSK is:
P_b = Q\left(\sqrt{2 \frac{E_b}{N_0}}\right)
Exactly the same as BPSK — because it’s really just two orthogonal BPSKs.

⸻

🧊 Constellation Diagram

       Q
       ↑
   01 ●     ● 00
      │     │
   11 ●     ● 10
       └────→ I

Each point represents a 2-bit symbol. The spacing between points determines noise resilience.

⸻