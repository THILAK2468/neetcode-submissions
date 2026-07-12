class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s =="":
            return True
        c=''
        for char in s:
            if char.isalnum():
                c+=char.lower()
        st,ed=0,len(c)-1
        while(st<ed):
            if c[st]!=c[ed]:
                return False
            st+=1
            ed-=1

        return True