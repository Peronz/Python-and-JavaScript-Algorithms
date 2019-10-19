class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        count = 0
        find = False
        
        # traverse from end to start
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ':
                count += 1
                find = True
            else:
                # we have found a word, stop traversing
                if find:
                    break
                  
        return count