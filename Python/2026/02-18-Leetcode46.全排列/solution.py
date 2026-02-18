from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        res = []
        for i in range(len(nums)):
            tmp = [nums[i]]
            nums_left = nums[:i] + nums[i+1:]
            for j in self.permute(nums_left):
                res.append(tmp + j)
        return res
    
if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4]
    print(s.permute(nums))
                



# 思路:
# 1. 构造一个空列表res, 用于存储所有排列
# 2. 每次固定nums中的一个元素放在临时列表的第一个位置, 对nums中的其他元素实现全排列并将结果添加到res中
# 3. 重复以上步骤, 直到所有元素都被固定在临时列表的第一个位置, 且所有情况添加完毕

# 如何实现全排列:

# 举例:
# 情况1: 
# 0
# 0

# 情况2:
# 01
# 01 10

# 情况3:
# 012
# 012 021 102 120 201 210

# ...
# 本质上, 是每次固定一个元素在第一位, 对剩余元素实现全排列, 并将结果添加到res中, 
# 其余元素的全排列情况参考的是上一次的情况, 据此可以实现多次调用permute函数, 实现全排列.

