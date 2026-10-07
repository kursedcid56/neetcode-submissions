from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tag = {}
        for i in strs:
            sorted_i = "".join(sorted(i))
            if sorted_i not in tag:
                tag[sorted_i] = [i]
            else:
                 tag[sorted_i].append(i)    

        return list(tag.values()) 