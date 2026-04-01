class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = len(s)
        lt = len(t)

        # 1. 条件限制
        if ls < 1 or ls > 5 * (10 ** 4):
            raise ValueError("s length must be between 1 and 5 * 10^4")
        if lt < 1 or lt > 5 * (10 ** 4):
            raise ValueError("t length must be between 1 and 5 * 10^4")
        if not s.islower() or not t.islower():
            raise ValueError("s and t must consist of only lowercase English characters")
        
        # 2. 逻辑实现

        if ls != lt:
            return False

        # # 方法一，利用26位长度的数组统计字母出现次数
        # count = [0] * 26
        # for char in s:
        #     count[ord(char) - ord("a")] += 1
        # for char in t:
        #     count[ord(char) - ord("a")] -= 1
        #         if count[ord(char) - ord("a")] < 0:
        #             return False
        # return True

        # 方法二，哈希表（适用于 Unicode 字符，进阶答案），包含Unicode字符时，用字典代替数组
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        for char in t:
            count[char] = count.get(char, 0) - 1
            if count[char] < 0:
                return False
        return True
    
if __name__ == "__main__":
    A = Solution()

    s = "rat"
    t = "car"

    result = A.isAnagram(s, t)
    print(result)

    
        

