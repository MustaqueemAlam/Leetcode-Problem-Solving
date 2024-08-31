class Solution(object):
    def replaceElements(self, arr):
        max_right = -1
        # firstly we need to traverse the list from right to left
        for i in range(len(arr) - 1, -1, -1):
            #len(arr) - 1 calculates the index of the last element in the array to determine the size of the array.
            #the next -1 means the loop will continue until it reaches -1 as the range stops before the stop value is reached, it will effectively stop when it reaches index 0.
            #the next -1 means that the loop will decrement the index by 1 after each iteration, moving from the end of the array towards the beginning.
            
            # now we Store the current element before it is replaced
            current = arr[i]
            # then we replace the current element with the maximum element to its right
            arr[i] = max_right
            # finally Update max right if the current element is greater
            if current > max_right:
                max_right = current
        
        return arr


sol = Solution()
arr = [17, 18, 5, 4, 6, 1]
print("Input:", arr)
output = sol.replaceElements(arr)
print("Output:", output)
