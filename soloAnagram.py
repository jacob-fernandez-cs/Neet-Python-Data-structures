class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #first the strings must be checked to be the same length, if they are not they cannot be anagrams
        if (len(s) != len(t)): 
            return False
        #build two hashmaps, one for string s and one for t
        hashmapS = {}
        hashmapT = {}

        for i in range(len(s)):    
            hashmapS[s[i]] = 1 + hashmapS.get(s[i], 0)
            hashmapT[t[i]] = 1 + hashmapT.get(t[i], 0)
        
        #check each letter in hashmap against other hashmap if they are all equal it must be an anagram
        #return true otherwise return false

        for i in hashmapS:
            a = hashmapT.get(i, 0)
            if hashmapS[i] != hashmapT[i]:
                return False
            
        return True
        




Solution = Solution()
s = "anagram" 
t = "nagaram"
print(Solution.isAnagram(s,t))

