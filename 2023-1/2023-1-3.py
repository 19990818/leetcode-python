

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l=s.split(" ")
        now=0
        for c in l:
           if c.isdigit():
               if int(c)<=now:
                   return False
               now=int(c)
        return True 