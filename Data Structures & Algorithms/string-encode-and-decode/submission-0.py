class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for i in strs:
            res += str(len(i)) +'@'+i
        return res
    def decode(self, s: str) -> List[str]:
        res =[]
        i=0

        while i<len(s):
            j=i

            while s[j]!='@':
                j+=1
            length = int(s[i:j])

            word_start = j+1
            word_end = word_start+length

            res.append(s[word_start:word_end])

            i = word_end
        return res
