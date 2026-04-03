class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ls = len(s)
        for i in range(1, ls):
            if ls % i != 0:
                continue
            
            if s[:i] * (ls // i) == s:
                return True
        
        return False

if __name__ == "__main__":
    A = Solution()

    s = "abab"

    result = A.repeatedSubstringPattern(s)

    print(result)
            