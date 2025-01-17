class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        res = 0
        nums.sort() 
        n = len(nums)
        
        left, right = 0, n - 1
        while left < right:
            if nums[left] + nums[right] < target:
                # If the sum is less than target, all pairs from left to right are valid
                res += (right - left) 
                left += 1  # Move the left pointer to the right
            else:
                right -= 1  # Move the right pointer to the left to try a smaller sum

        return res

sol = Solution()

nums = [-1, 1, 2, 3, 1]
target = 2
print(sol.countPairs(nums, target))  

nums = [-6, 2, 5, -2, -7, -1, 3]
target = -2
print(sol.countPairs(nums, target))  
