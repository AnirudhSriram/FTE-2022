# https://leetcode.com/problems/group-anagrams/solution/
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(NKlogK) time O(NK) space
        # anagrams = defaultdict(list)
        # for s in strs:
        #     anagrams[tuple(sorted(s))].append(s)
        # return(anagrams.values())
        # O(NK) time and space       
        anagrams = defaultdict(list)
        for s in strs:
            count = [0]*26 
            for c in s:
                count[ord(c)-ord('a')]+=1
            anagrams[tuple(count)].append(s)
        return anagrams.values()
                
                