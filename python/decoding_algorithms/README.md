✅ Step-by-Step Plan to Simulate Viterbi Decoding

1. Define a convolutional encoder
	•	Set constraint length K
	•	Define generator polynomials (e.g., [7, 5] in octal for rate 1/2)

2. Generate random input bits
	•	Binary input stream of a given length

3. Encode the bits
	•	Use the convolutional encoder to create a codeword

4. Add noise (optional for BER test)
	•	Pass the encoded stream through an AWGN channel

5. Viterbi decoder
	•	Implement the decoder using a trellis structure
	•	Perform hard-decision or soft-decision decoding

6. Evaluate
	•	Compare decoded bits vs original input
	•	Calculate Bit Error Rate (BER)

⸻

✅ Why Soft-Decision Decoding?

Hard-decision decoding turns the received signal into bits before decoding — potentially throwing away valuable information (e.g., how confident we are in the bit being 0 or 1).

Soft-decision decoding uses the actual received values (e.g., +0.9, -1.2, etc.) to compute path metrics more accurately, based on Euclidean distance rather than Hamming distance.

⸻

🧠 Step-by-Step Plan
	1.	Leave the encoder and noise simulation unchanged
(We’ll still use add_awgn_noise() to generate noisy BPSK values.)
	2.	Update the Viterbi decoder to use Euclidean distance instead of bit mismatches.


⸻