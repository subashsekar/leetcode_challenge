class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == ' ':
                continue
            elif s[i] != ' ':
                count += 1
                if s[i-1] == ' ':
                    break 
            else:
                break

        return count

                

            
                

        