class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # Determine sign
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:

            shift = 0

            # Find the largest divisor * 2^shift
            while dividend >= (divisor << (shift + 1)):
                shift += 1

            # Subtract divisor * 2^shift
            dividend -= divisor << shift

            # Add 2^shift to quotient
            quotient += 1 << shift

        # Apply sign
        if negative:
            quotient = -quotient

        # 32-bit overflow handling
        if quotient > 2**31 - 1:
            return 2**31 - 1

        if quotient < -2**31:
            return -2**31

        return quotient