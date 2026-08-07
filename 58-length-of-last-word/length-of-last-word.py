class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        emp =[]
        word = ""
        for char in s:
            if (65 <= ord(char) <= 90) or (97 <= ord(char) <= 122):
                word = word +char
            elif char == " ":
                if word != "":
                    emp = emp + [word]
                    word = ""
        if word != "":
            emp = emp + [word]
        print(emp)
        return len(emp[-1])

                

            
                

        