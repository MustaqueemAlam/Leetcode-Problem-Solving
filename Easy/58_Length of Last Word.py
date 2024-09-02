class Solution:
    def lengthOfLastWord(self, s):
        # Trim trailing spaces 2 avoid counting extra spaces
        s = s.strip()
        # Split  string by spaces
        words = s.split(' ')
        # Return  length of the last word
        return len(words[-1])

enter = "Hello World"
solution = Solution()
print(solution.lengthOfLastWord(enter)) 
