class Solution:
    def lengthOfLIS(self, nums:list[int]) -> int:
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size

s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
