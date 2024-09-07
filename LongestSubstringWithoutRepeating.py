class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() #all of the characters in our "sliding window"
        lP = 0 ##left pointer
        result = 0

        for rP in range(len(s)): #right pointer goes through every character
            while s[rP] in charSet: #if the character is already in the set then its a dupilcate remove the character and move the left pointer forward
                charSet.remove(s[lP])  #left most character has to be removed
                lP += 1
            charSet.add(s[rP])
            result = max(result, rP - lP + 1)
        return result




Solution = Solution()
s = "abcabcbb"
print(Solution.lengthOfLongestSubstring(s))