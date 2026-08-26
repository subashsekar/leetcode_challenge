class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            bit = n & 1
            print("bit",bit)
            result = (result << 1) | bit
            print("result",result)
            print("n0",n)
            n >>= 1
            print("n",n)
        return result
        