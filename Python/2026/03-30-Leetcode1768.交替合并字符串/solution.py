import re

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        w1 = len(word1)
        w2 = len(word2)
        w = []

        # 限制条件满足
        if w1 < 1 or w1 > 100:
             raise ValueError("word1 length must be between 1 and 100.")
        if w2 < 1 or w2 > 100:
             raise ValueError("word2 length must be between 1 and 100.")
        if not re.match(r'^[a-z]+$', word1):
            raise ValueError("word1 must contain only lowercase English letters.")
        if not re.match(r'^[a-z]+$', word2):
            raise ValueError("word2 must contain only lowercase English letters.")
        
        # 逻辑实现
        if w1 >= w2:
            for i in range(0, w2):
                w.append(word1[i])
                w.append(word2[i])
            w.extend(word1[w2:])
        else:
            for i in range(0, w1):
                w.append(word1[i])
                w.append(word2[i])
            w.extend(word2[w1:])
        
        # 结果返回
        result = "".join(w)
        print(result)
        return result

if __name__ == "__main__":
    A = Solution()
    # A.mergeAlternately("ab", "pqrs")
    A.mergeAlternately("abc", "pqr")
    
