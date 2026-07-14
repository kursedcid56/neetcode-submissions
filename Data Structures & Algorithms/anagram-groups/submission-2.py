class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        gr = {}
        for i in strs:
            tag = "".join(sorted(i))       
            if tag not in gr:
                gr[tag] = [i]
            else:
                gr[tag].append(i)
    
        return list(gr.values())    
