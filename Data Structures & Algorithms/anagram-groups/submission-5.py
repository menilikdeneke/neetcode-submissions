class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            letters = [0] * 26
            for c in string:
                letters[ord(c) - ord('a')] += 1
            res[tuple(letters)].append(string)
        
        return list(res.values())