class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #pointer for position in array 
        k = 0
        #iterate through array
        for i in range(len(nums)):
            # if the element is not equal to value we perform the swap otherwise we ignore the value
            if nums[i] != val:
                #since the element isn't equal to the value we put it at position k 
                nums[k] = nums[i]
                #increment pointer to count non sepcial value elements in the aray
                k += 1
        return k
