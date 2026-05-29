class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping: dict[tuple, list] = {} # tuple of counts -> list of strs
        for s in strs:
            c_counts = [0] * 26 # a - z
            for c in s:
                c_counts[ord(c) - ord('a')] += 1
            mapping[tuple(c_counts)] = mapping.get(tuple(c_counts), []) + [s]
        return list(mapping.values())