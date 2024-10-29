class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        longestStreak = 0
        unique = set(nums)
        for n in nums:
            currentStreak = 0
            current =  n
            while current in unique:
                currentStreak += 1
                
                if current * current > 1e5:
                    break
                current *= current
            longestStreak = max(longestStreak, currentStreak)
        return longestStreak  if longestStreak >= 2 else -1
