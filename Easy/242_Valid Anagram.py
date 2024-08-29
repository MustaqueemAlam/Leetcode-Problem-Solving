class Solution:
    def isAnagram(self, s, t):
        # If the lengths are not equal they can't be anagrams
        if len(s) != len(t):
            return False
        
        # Sort both of the strings and compare them
        return sorted(s) == sorted(t)


solution = Solution()

print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram("pok", "meerKat"))          
