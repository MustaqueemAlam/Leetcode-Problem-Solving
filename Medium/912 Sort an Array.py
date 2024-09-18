class Solution(object):
    def sortArray(self, nums):
        def heapify(nums, n, i):
            # Assume the largest element is at the root (index i)
            largest = i
            left = 2 * i + 1  # Left child index
            right = 2 * i + 2  # Right child index
            
            # If left child exists and is greater than the root
            if left < n and nums[left] > nums[largest]:
                largest = left
                
            # If right child exists and is greater than the largest element so far
            if right < n and nums[right] > nums[largest]:
                largest = right
                
            # If the largest element is not the root
            if largest != i:
                # Swap the root with the largest element
                nums[i], nums[largest] = nums[largest], nums[i]
                
                # Recursively heapify the affected subtree
                heapify(nums, n, largest)
        
        def heap_sort(nums):
            n = len(nums)
            
            #                  Build a max heap (rearrange the array)
            for i in range(n // 2 - 1, -1, -1):
                heapify(nums, n, i)
            
            #                 One by one, extract elements from the heap
            for i in range(n - 1, 0, -1):
                #             Move the current root (largest element) to the end of the array
                nums[i], nums[0] = nums[0], nums[i]
                
                #             Call heapify on the reduced heap
                heapify(nums, i, 0)
        
        #                     Call heap_sort on the input array
        heap_sort(nums)
        
        return nums
sol = Solution()

# Example 1
nums1 = [5, 2, 3, 1]
print(sol.sortArray(nums1))  # Output: [1, 2, 3, 5]

# Example 2
nums2 = [5, 1, 1, 2, 0, 0]
print(sol.sortArray(nums2))  # Output: [0, 0, 1, 1, 2, 5]
