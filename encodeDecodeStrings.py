class Solution:
    def encode(self, strs):
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result
    
    
    def decode(self,str):
        result, i = [], 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j]) #this is the string from index I up until index J but not including j
            test = str[j + 1 : j + 1 + length]
            result.append(test)   
            i = j + 1 + length
        return result 
    
Solution = Solution()

list = ["poopity", "scoop", "da", "poop"]

res = Solution.encode(list)
print(Solution.decode(res))