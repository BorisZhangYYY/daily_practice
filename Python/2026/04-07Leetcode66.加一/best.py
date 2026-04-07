from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pos = len(digits) - 1
        add = True
        while pos >= 0 and add:
            if digits[pos] + 1 == 10:
                digits[pos] = 0
                pos = pos - 1
                add = True
                continue
            else:
                digits[pos] = digits[pos] + 1
                add = False
                break
    
        if pos < 0:
            digits.insert(0, 1)

        return digits

if __name__ == "__main__":
    A = Solution()

    digits = [2, 3, 4, 9]

    result = A.plusOne(digits)
    print(result)

