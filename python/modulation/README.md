Gray-coded mapping is a technique used in digital modulation schemes (like QAM, PSK) where the bit patterns assigned to constellation points are arranged so that adjacent points differ by only one bit.

⸻

✅ What is Gray Code?
	•	A binary numeral system where only one bit changes between two successive values.
	•	Example (2-bit Gray code):

Binary   Gray
00       00  
01       01  
10       11  
11       10  

⸻

📡 Why Use Gray-Coded Mapping in Modulation?

Because in real-world transmission, noise may cause the received symbol to land near a neighboring constellation point. If:
	•	Adjacent points differ by just one bit, then
	•	A small symbol error causes only one bit error, not multiple.

This significantly reduces Bit Error Rate (BER).

⸻

🔍 Visual Example (4-QAM):

Symbol	Coordinates	Binary	Gray-coded
S0	    -1 - 1j	    00	    00
S1	    -1 + 1j	    01	    01
S2	    +1 - 1j	    10	    11
S3	    +1 + 1j	    11	    10

Gray-coded version ensures adjacent symbols differ by one bit.

⸻

✨ Summary:

Gray coding minimizes bit errors caused by symbol errors, which is especially valuable in noisy channels like wireless and satellite links. It improves reliability with no added bandwidth or power cost.

