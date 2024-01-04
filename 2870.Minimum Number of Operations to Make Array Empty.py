from collections import Counter
class Solution:
    def minOperations(self , nums: list[int]) -> int:
        count = 0
        h = Counter(nums)
        for i in h:
            if h[i] == 1:
                return -1
            count += h[i]//3 + (h[i]%3 != 0)
        
        return count
        
        
s = Solution()
i = [2,1,2,2,3,3]
print(s.minOperations(i))