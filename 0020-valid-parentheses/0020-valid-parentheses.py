class Solution:
    def isValid(self, s: str) -> bool:
        ans=[]
        pairs = {')': '(',']': '[','}': '{'}
        for ch in s:
            if ch in "({[":
                ans.append(ch)
            else:    
                if not ans:
                    return False
                if ans[-1] != pairs[ch]:
                    return False

                ans.pop()

        return len(ans) == 0   




           
           

        