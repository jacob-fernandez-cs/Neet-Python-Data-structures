class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create two hashmaps (dictionaries) one to count the occurences of letters in the string S
        #another to do the same for the string T
        countS = {}
        countT = {}
        #if the length of both strings are not the same it is impossible for them to be anagrams.
        if len(s) != len(t):
            return False

        #loop through the length of string S since the hash map needs to add all characters and their occurence to map, (creation of hashmaps)
        for i in range(len(s)):
            
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
    
        #check to make sure each key and value are the same, if they are not they cannot be anagram otherwise the function returns true
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False


        return True

s = "anagram"
t = "nagaran"

Solution = Solution()

print(Solution.isAnagram(s,t))

