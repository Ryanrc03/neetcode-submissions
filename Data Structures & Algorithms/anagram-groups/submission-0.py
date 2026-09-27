class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {} # hash table: str
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key not in map: 
                map[key] = []
            map[key].append(s)
            # print
        return list(map.values())           
        