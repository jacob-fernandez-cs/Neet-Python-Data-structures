class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        #create a hashmap, where the key is the occurence of the letters in the string, an array?
        #  and the value is the number of strings which map the occurence of the letters
        from collections import defaultdict 

        res = defaultdict(list) #hashmap mapping character count to to a list of anagrams

        #loop through list of strings
        for x in strs:
            count = [0] * 26 #count occurence of letters in anagram, 26 possible letters a - z
            for i in x:
                count[ord(i) - ord("a")] += 1

            res[tuple(count)].append(x) #list cannot be a key, must be converted to tuple

        #testing append
        #res["test"].append("value")
        return res.values()
    
    #O(m+n)

Solution = Solution()

print(Solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))