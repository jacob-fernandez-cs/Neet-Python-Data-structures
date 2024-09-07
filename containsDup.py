class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashSet = set()

        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)
        return False
    

Solution = Solution()
list = [1,7 ,2 ,4 , 5, 6,2]
print(Solution.containsDuplicate(list))