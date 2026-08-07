class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        emp = []
        for i,j in enumerate(words):
            if x in j:
                emp.append(i)
        return emp