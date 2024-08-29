class Solution(object):
    def twoSum(self, nums, target):
        num_indices = {}
        # Dictionary to store numbers and their indices
        for i, num in enumerate(nums):
            complement = target - num
            # Calculate the required complement
            if complement in num_indices:
                return [num_indices[complement], i]
                # If complement found, return indices
            num_indices[num] = i  
            # Otherwise, store the current number with its index
        return None  

    
solution = Solution()
#pass nums and target
print(solution.twoSum([2, 7, 11, 15], 9))
#index of 7 and 2 is 0,1 and it fills upmthe given target 9
print(solution.twoSum([3, 2, 4], 6))
#index of 2 and 4 is 1,2 and it fills upmthe given target 6
print(solution.twoSum([3, 3], 6))  
#index of 3 and 3 is 0,1 and it fills upmthe given target 6