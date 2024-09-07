class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = [] #list of lists
        nums.sort() #sort the nums list to make the problem similar to twoSum_two 

        for i, a in enumerate(nums): #use each number in the input array as a possible value, loop through index and value
            if i > 0 and a == nums[i- 1]: #we want to make sure we dont use the same value for a twice, taking advantage of the array being sorted, continue to next loop iteration
                continue
        
        #above a is the part making this three sum, below is essentially preforming two sum on the remaining portion of the array
            l, r = i +1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0: #if threeSum is too large move the right pointer to the left (the largest value is the rightmost value because the array is sorted)
                    r -= 1
                elif threeSum < 0: #if threeSum is too small move the left pointer to the right
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1 #only left pointer needs shifted
                    while nums[l] == nums[l - 1] and l < r: #if the left pointer is the same value as before shift again, make sure it doesn't cross the right pointer either
                        l += 1
        return result
            

Solution = Solution()

nums = [-1,0,1,2,-1,-4]

print(Solution.threeSum(nums))