class Solution:
    def isPalindrome(self, s: str) -> bool:
        #remove all non alphanumeric characters
        newStr = ""
        for c in s:
            if c.isalnum(): #check if character is 
                #alphanumerical if it is change it to lowercase and add it to the string
                newStr += c.lower()
        return newStr == newStr[::-1] #check if the new string is the same if reversed, this will return true if
    #it is a palidrone otherwise it will return false, [::-1] is how you reverse a string

    #helper function, this will determine if a character is alphanumeric or not using ASCI code values

    def alphaNum(self, c):
        #the ord function will return a characters ascii value
        #check if the value is between A and Z, or between a and z, or 0 and 9, all these values are contiguous 
        return (ord('A') <= ord(c) <= ord('Z') or 
         ord('a') <= ord(c) <= ord('z') or 
         ord('0') <= ord(c) <= ord('9')) 
    #this function returns true if this long statement is true at any point otherwise it returns false
    
    def two_pointer(self, s: str) -> bool:
        left_pointer = 0
        right_pointer = len(s) - 1

        while left_pointer < right_pointer: #making sure the pointers have not met or crossed each other
            
            
            #make sure both the left and right pointers are alphanumeric otherwise move the pointer forward/backwards 1
            #make sure pointer is never out of bounds
            while left_pointer < right_pointer and not self.alphaNum(s[left_pointer]): #make sure left pointer never crosses right pointer, and the character is alphanumeric
                left_pointer += 1
            while right_pointer > left_pointer and not self.alphaNum(s[right_pointer]):
                right_pointer -= 1
            #essentially checking in pairs, if the left pointer character does not equal the right pointer
            #character return false, also converting each character to lowercase
            if s[left_pointer].lower() != s[right_pointer].lower():
                return False
            #comparison has been made thus we must move the pointers respectively
            left_pointer += 1
            right_pointer -= 1
            debugL = s[left_pointer]
            debugR = s[right_pointer]
            
        return True #the if statement is never triggered thus the string must be a valid palindrome
    

Solution = Solution()

String = "A man, a plan, a canal: Panama"

print(Solution.two_pointer(String))
