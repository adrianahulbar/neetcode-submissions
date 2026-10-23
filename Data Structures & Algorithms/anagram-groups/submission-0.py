class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = dict()
        for s in strs:
            sorted_key = "".join(sorted(s))
            if sorted_key not in anagrams_map:
                anagrams_map[sorted_key]=[]
            anagrams_map[sorted_key].append(s)
        return list(anagrams_map.values())
        