class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s =="":
            return True
        st,ed=0,len(s)-1
        while(st<ed):
            if not s[st].isalnum():
                st+=1
            elif not s[ed].isalnum():
                ed-=1
            elif s[st].lower()!=s[ed].lower():
                return False
            else:
                st+=1
                ed-=1
        return True