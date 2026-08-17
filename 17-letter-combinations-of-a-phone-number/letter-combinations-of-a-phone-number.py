class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"}
        emp = []
        string = ""
        def backtrack(index,string):
            if index == len(digits):
                emp.append(string)
                return emp
            for letter in phone[digits[index]]:
                backtrack(index+1,string+letter)
        backtrack(0,string)
        return emp