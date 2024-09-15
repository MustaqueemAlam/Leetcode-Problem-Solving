class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        s_to_t = {}
        t_to_s = {}
        for char_s, char_t in zip(s, t):
            # Check mapping from s to t
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                s_to_t[char_s] = char_t
            # Check reverse mapping from t to s
            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s
        return True
    
sol = Solution()
# Example 1
s1 = "egg"
t1 = "add"
print(sol.isIsomorphic(s1, t1))  

# Example 2
s2 = "foo"
t2 = "bar"
print(sol.isIsomorphic(s2, t2)) 

# Example 3
s3 = "paper"
t3 = "title"
print(sol.isIsomorphic(s3, t3))  
