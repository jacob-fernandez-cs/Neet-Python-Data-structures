class solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        #convert the list nums to a set
        numSet = set(nums)
        longest = 0

        for n in nums:
            #check if its the start of a sequence
            if (n - 1) not in numSet: #if the number does not have a left nieghbor it is the start of a sequence
                length = 0 #length of sequence
                while(n + length) in numSet:
                    length += 1
                longest = max(length,longest)
        return longest
    

solution = solution()
input = [100, 4, 200, 1 , 3, 2]
print(solution.longestConsecutive(input))