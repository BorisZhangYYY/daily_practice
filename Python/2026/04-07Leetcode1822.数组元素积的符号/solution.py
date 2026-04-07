from typing import List

class Solution:
    def signFunc(self, num: int) -> int:
        if num > 0:
            return 1
        elif num == 0:
            return 0
        else:
            return -1 
    
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for num in nums:
            product = product * num
        
        return self.signFunc(product)
    
if __name__ == "__main__":
    A = Solution()

    nums = [-1,-2,-3,-4,3,2,1]

    result = A.arraySign(nums)
    print(result)

