class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}

        if len(s) != len(t) :
            return False

        for char in s :
            if char in sMap :
                sMap[char] = sMap[char] + 1
            else :
                sMap[char] = 1
        
        for char in t :
            if char in tMap :
                tMap[char] = tMap[char] + 1
            else:
                tMap[char] = 1
        
        return tMap == sMap