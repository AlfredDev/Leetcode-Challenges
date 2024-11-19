class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        start = 0
        current_sum = 0
        max_sum = 0
        unique_elements = set()
        
        for end in range(len(nums)):
           
            while nums[end] in unique_elements:
                unique_elements.remove(nums[start])
                current_sum -= nums[start]
                start += 1

           
            unique_elements.add(nums[end])
            current_sum += nums[end]
            
           
            if end - start + 1 == k:
                max_sum = max(max_sum, current_sum)
                
                current_sum -= nums[start]
                unique_elements.remove(nums[start])
                start += 1
        
        return max_sum
