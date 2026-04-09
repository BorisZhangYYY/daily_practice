from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[0] < nums[-1]:
            for i in range(0, len(nums) - 1):
                if nums[i + 1] - nums[i] < 0:
                    return False
        elif nums[0] > nums[-1]:
            for i in range(0, len(nums) - 1):
                if nums[i + 1] - nums[i] > 0:
                    return False
        else:
            for i in range(0, len(nums) - 1):
                if nums[i + 1] - nums[i] != 0:
                    return False
        return True


if __name__ == "__main__":
    A = Solution()
    # nums = [1, 3, 2]
    # nums = [1, 2, 2, 3]
    nums = [6, 5, 4, 4]
    print(A.isMonotonic(nums))
