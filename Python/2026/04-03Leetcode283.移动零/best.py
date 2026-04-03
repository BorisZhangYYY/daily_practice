from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # 左指针：指向当前要放置非零元素的位置
        left = 0
        # 右指针：遍历数组，找非零元素
        for right in range(len(nums)):
            if nums[right] != 0:
                # 交换非零元素到左指针位置
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    Solution().moveZeroes(nums)
    print(nums)  # [1,3,12,0,0]