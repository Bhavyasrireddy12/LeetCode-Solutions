class Solution:
    def smallestSubsequence(self, s: str) -> str:
            freq={}
            for i in range(len(s)):
                freq[s[i]]=i
            stack=[]
            visit=set()
            for i in range(len(s)):
                ch=s[i]
                if ch in visit:
                    continue
                while stack and stack[-1] > ch and freq[stack[-1]]>i:
                    visit.remove(stack.pop()) 
                stack.append(ch)
                visit.add(ch)      
            return "".join(stack)     

       




        