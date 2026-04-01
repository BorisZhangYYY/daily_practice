class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 1. 条件满足
        if len(haystack) < 1 or len(haystack) > 10 ** 4:
            raise ValueError("haystack length must be between 1 and 10^4")
        if len(needle) < 0 or len(needle) > 10 ** 4:
            raise ValueError("needle length must be between 0 and 10^4")
        if not haystack.islower() or not needle.islower():
            raise ValueError("haystack and needle must consist of only lowercase English characters")
        
        # 2. 逻辑实现
        l1 = len(haystack)
        l2 = len(needle)
        for i in range(0, l1 - l2 + 1): # 遍历haystack寻找满足条件的needle子串，只需遍历 l1 - l2 + 1 次即可
            if haystack[i:i+l2] == needle:
                return i
        return -1 # 遍历结束也没返回，所以肯定是-1不存在子串
    
if __name__ == "__main__":
    A = Solution()

    haystack = "hello"
    needle = "ll"

    result = A.strStr(haystack, needle)

    print(result)



        