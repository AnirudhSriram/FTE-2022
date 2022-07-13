class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(nlogn) time and O(n) space
        # s = list(s)
        # s.sort()
        # t = list(t)
        # t.sort()
        # if len(s)!=len(t):
        #     return False
        # for i in range(len(s)):
        #     if t[i] != s[i]:
        #         return False
        # return True
        
        # O(n) time and O(1) space
        dicts = collections.Counter(s)
        dictt = collections.Counter(t)
        if dicts == dictt:
            return True
        return False
                