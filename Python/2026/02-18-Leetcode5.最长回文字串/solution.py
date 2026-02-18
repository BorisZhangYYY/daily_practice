class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not 1 <= len(s) <= 1000:
            raise ValueError("s的长度必须在1到1000之间")
        elif len(s) == 1:
            return s
        
        res = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1): # 针对每一个子串，进行判断其是否是回文串
                if s[i:j] == s[i:j][::-1]:
                    res = s[i:j] if len(s[i:j]) > len(res) else res  # 确保res是最长的回文子串
        return res
    
if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("babad"))






# 思路:
# 1. 遍历字符串s，找到其所有子串
# 2. 遍历所有子串，判断是否为回文子串，若为回文子串，则记录其长度
# 3. 选择其中的一个作为结果返回