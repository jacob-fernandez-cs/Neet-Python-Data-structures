class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        #loop through nums array add nums to hashmap 
        #increament value to represent multiple occurences
        #return keys which have values greater than or equal to k
        from heapq import nlargest
        hashMap = {}
        
        
        
        for i in nums:
            hashMap[i] = 1 + hashMap.get(i,0)
        
        #kKeys = [x for x, v in hashMap.items() if v >= k ]
        kHighest = nlargest(k, hashMap, key = hashMap.get)
        return kHighest

    def neetCodeSolution(self, nums: list[int], k: int) -> list[int]:
        #bucket sort solution this is big O of N the above solution is klogn 
        countHash = {}
        freq = [[] for i in range(len(nums) + 1)] #index is the frequency of an element aka count, 
        #and the value will be the list of values which occur in the frequency, also length is the size of input array plus 1 (position 0 will not be used)
        
        #counts each numbers occurence 0 is the default value if it doesnt exist
        for i in nums:
            countHash[i] = 1 + countHash.get(i,0)
        for i, c in countHash.items():
            freq[c].append(i) #at index c (count) the value i occurs c times

        result = []

        for i in range(len(freq) - 1, 0, -1): #backwards for loop that stops at 0
            for n in freq[i]: #if n at freq[i] is not empty add it to result, eventually result will be as long as K thus return result
                result.append(n)
                if len(result) == k:
                    return result

Solution = Solution()

nums = [1,1,1,2,2,3]

print(Solution.neetCodeSolution(nums, 2))