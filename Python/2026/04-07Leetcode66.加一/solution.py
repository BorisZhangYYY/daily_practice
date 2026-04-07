from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp_number = "".join(str(digit) for digit in digits)
        final_number = int(temp_number) + 1
        result = [int(num) for num in str(final_number)]

        return result


if __name__ == "__main__":

    A = Solution()

    digits = [9, 9, 9, 9]

    result = A.plusOne(digits)
    print(result)

        