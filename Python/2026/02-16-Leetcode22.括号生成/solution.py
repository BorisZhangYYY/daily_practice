from typing import List

class Solution():
    def __init__(self, n: int):
        # Leetcode提交时需要删除掉__init__方法
        if n < 1 or n > 8:
            raise ValueError("n must be between 1 and 8.")
        self.res = self.generateParenthesis(n)
    
    def generateParenthesis(self, n: int) -> List[str]:
        dp: List[set[str]] = [set() for _ in range(n + 1)]
        dp[0].add("")
        if n >= 1:
            dp[1].add("()")
        for total in range(2, n + 1): # 用于保存total个括号的所有情况，total从2开始，因为1个括号只有1种情况
            current: set[str] = set()  # dp[total]的所有情况
            for removed_pairs in range(1, total): # 拿走removed_pairs个括号 1
                base_pairs = total - removed_pairs # 剩余base_pairs个括号 2
                removed_set = dp[removed_pairs]  # 拿走的removed_pairs个括号的总情况 ()
                base_set = dp[base_pairs]  # 剩余base_pairs个括号的总情况 ()() (())
                for base in base_set:
                    for removed in removed_set:
                        for pos in range(len(base) + 1): # 每个base种的每个位置插入removed, 集合去重()()() (())() ()(()) (()()) ((())) 
                            current.add(base[:pos] + removed + base[pos:])
            dp[total] = current
        return sorted(dp[n])

if __name__ == "__main__":
    # 测试方法, 在1 <= n <= 8时, 分别输出n个括号的所有情况, 下为n=4时的情况:
    s = Solution(4)
    print(s.res)


"""Thinking Process:
想法:
n=1 时, 有1种情况:  ()
n=2 时, 有2种情况:  ()() (())
n=3 时, 有5种情况:  
        拿走0个:    ()()() 
        拿走1个:    (())() ()(()) 
        拿走2个:    (()()) ((()))
n=4 时, 有14种情况: 
        拿走0个:    ()()()() 
        拿走1个:    (())()() ()(())() ()()(()) 
        拿走2个:    (()())() ()(()()) ((()))() ()((())) (())(()) 
        拿走3个:    (()()()) ((())()) (()(())) ((()())) (((())))
...

规律:
n等于x时, 迭代x-1次, 先把x个括号展开, 形如"()()()()...()"随后:
1. 第1次取走1个括号遍历放入x-1个展开的括号种的每种情况;
2. 第2次取走2个括号遍历放入x-2个展开的括号种的每种情况; 同时考虑2个括号的情况;
3. 第3次取走3个括号遍历放入x-3个展开的括号种的每种情况; 同时考虑3个括号的情况;
...
x-1. 第x-1次取走x-1个括号遍历放入1个展开的括号种的每种情况; 同时考虑x-1个括号的情况;
从第2次迭代开始, 每次都需要考虑额外考虑取走括号的情况, 再往后, 还需要考虑取走括号内部还存在嵌套的情况。
"""

