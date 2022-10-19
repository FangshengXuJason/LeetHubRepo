from collections import deque
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        d = {1: '', 2: 'abc',3: 'def',4: 'ghi',5: 'jkl',6: 'mno',7: 'pqrs',8: 'tuv',9: 'wxyz'}
        q = deque(d[int(digits[0])])
        
        for i in range(1,len(digits)):
            for s in range(len(q), 0, -1):
                out = q.popleft()
                for j in d[int(digits[i])]:
                    q.append(out + j)
               
                
        return q
    