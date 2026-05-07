class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        for i, x in enumerate(strs):
            num = str(sorted(x))
            if num in count:
                count[num] += [x]
            else:
                count[num] = [x]
        return list(count.values())
        
