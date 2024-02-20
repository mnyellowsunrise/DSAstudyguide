class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Check if the needle is an empty string, in which case it is always present at index 0.
        if needle == "":
            return 0
        
        # Iterate through the haystack using a sliding window approach.
        for i in range(len(haystack) + 1 - len(needle)):
            # Check if the substring of haystack from current index i to i + len(needle)
            # is equal to the needle. If yes, return the current index i.
            if haystack[i: i + len(needle)] == needle:
                return i
                
        # If the loop completes without finding a match, return -1 indicating needle is not part of haystack.
        return -1
