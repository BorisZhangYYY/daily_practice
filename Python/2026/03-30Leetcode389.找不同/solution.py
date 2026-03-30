import re

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ls = len(s)
        lt = len(t)

        # 条件判断
        if ls < 0 or ls > 1000:
            raise ValueError("s length must be between 0 and 1000.")
        if lt != ls + 1:
            raise ValueError("Not regulated.")
        if not re.match(r'^[a-z]*$', s):
            raise ValueError("s must contain only lowercase letters.")
        if not re.match(r'^[a-z]*$', t):
            raise ValueError("t must contain only lowercase letters.")
        
        # 逻辑实现
        result = 0
        for char in s:
            result ^= ord(char)
        for char in t:
            result ^= ord(char)
        return chr(result)
                          
if __name__ == "__main__":
    A = Solution()
    # result = A.findTheDifference("a", "aa")
    result = A.findTheDifference("", "y")
    print(result)


