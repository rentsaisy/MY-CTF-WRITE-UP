# Black Ice Cipher - Sanitized Specification
# This file describes the cipher's structure for analysis.
# The actual flag and seed are NOT included.

class NLFSR:
    """
    Non-Linear Feedback Shift Register
    - State size: 36 bits
    - Feedback function: b(35) XOR b(30) XOR b(21) XOR (b(15) AND b(7)) XOR (b(5) AND b(2) AND b(0))
    - Output: LSB of state (bit 0)
    - Shift: right-shift by 1, feedback bit inserted at position (size-1)
    - Byte output: 8 consecutive bits, LSB first
    """
    def __init__(self, seed, size=36):
        self.state = seed & ((1 << size) - 1)
        self.size = size

    def next_bit(self):
        s = self.state
        b = lambda i: (s >> i) & 1
        fb = b(35) ^ b(30) ^ b(21) ^ (b(15) & b(7)) ^ (b(5) & b(2) & b(0))

        out = s & 1
        self.state = (s >> 1) | (fb << (self.size - 1))
        return out

    def next_byte(self):
        byte = 0
        for i in range(8):
            byte |= (self.next_bit() << i)
        return byte


# Encryption: plaintext XOR keystream_byte for each byte
# Keystream is generated sequentially from the NLFSR
# The seed (initial state) is unknown and must be recovered.
