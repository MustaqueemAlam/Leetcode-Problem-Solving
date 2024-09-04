class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {} # Init an empty dict to hold the grouped anagrams
        for word in strs: # Iterate through each string in the input list
            # Sort the characters in the string to create a key
            sorted_word = ''.join(sorted(word)) # Adds original string to the dictionary based on the sorted key
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        return list(anagrams.values())

solution = Solution()

test_input = ["eat","tea","tan","ate","nat","bat"]
output = solution.groupAnagrams(test_input)

print(output)
