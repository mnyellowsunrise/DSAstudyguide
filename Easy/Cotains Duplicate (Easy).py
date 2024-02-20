class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #create data structure to hold values
        hashset = set()
    
        #iterate through the hashset
        for n in nums:
            #check if duplicate
            if n in hashset:
                return True
            #otherwise add the value to the hashset
            hashset.add(n)

#This 