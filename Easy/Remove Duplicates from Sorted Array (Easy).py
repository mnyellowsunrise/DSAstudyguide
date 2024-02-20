class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #because array comes sorted we know that the first element will always be the same so we can start from the second elemnent
        leftpointer = 1
        
        #interate through array starting with index 1
        for rightpointer in range(1, len(nums)):
            #check if the value is new or one we've already see by comparing it to the one we've just seen
            if nums[rightpointer] != nums[rightpointer - 1]:
                #if a new value is found place it at the leftpointer
                nums[leftpointer] = nums[rightpointer]
                #increment the left pointer so that we can track how many unique values were added
                leftpointer += 1
        return leftpointer