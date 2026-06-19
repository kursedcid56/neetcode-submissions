class Solution:

    def encode(self, strs: List[str]) -> str:
        rs = ""
        for i in strs:
            rs += str(len(i)) + "#" + i
        return rs    
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j +=1
            length = int(s[i:j])
            tu_goc = s[j+1:j+1+length]
            result.append(tu_goc)
            i = j + 1 + length
        return result

            
