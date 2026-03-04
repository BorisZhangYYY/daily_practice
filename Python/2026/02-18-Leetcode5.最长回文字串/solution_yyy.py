class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expand(i:int, j:int) -> str:
            while i>=0 and j<n and s[i]==s[j]:
                i, j = i-1, j+1     # 区间左右扩散
            return s[i+1:j]         # 多扩散了一次到非法区间，因此返回上个扩散的合法区间

        ans = ''
        for i in range(n):
            odd = expand(i, i)      # 奇数回文子串
            even = expand(i, i+1)   # 偶数
            tmp = odd if len(odd) > len(even) else even     # tmp更新为长度更长的子串

            if len(tmp) > len(ans):
                ans = tmp
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('babad'))