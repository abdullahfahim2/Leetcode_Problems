class Solution:
    def numberOfBeams(self, bank: int) -> int:
        ans = 0
        m = 0
        for i in bank:
            n = i.count('1')
            
            if n == 0:
                continue
            ans += (m * n)
            m = n
        return ans
    
x = Solution()
bank = ["011001","000000","010100","001000"]
print(x.numberOfBeams(bank))