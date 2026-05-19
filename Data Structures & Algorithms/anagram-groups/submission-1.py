class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            counts = [0]*26
            for y in s:
                counts[ord(y)-97] += 1
            
            try:
                groups[tuple(counts)].append(s)
            except:
                groups[tuple(counts)] = [s]

        return list(groups.values())