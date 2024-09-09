from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        return [item for item, freq in count.most_common(k)]


solution = Solution()
test_nums = [1, 1, 1, 2, 2, 3]
test_k = 2
output = solution.topKFrequent(test_nums, test_k)

print("Output:", output) 
