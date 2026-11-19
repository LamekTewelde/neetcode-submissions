class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = {}
        pairs = {}
        final = []
        for string in strs:
            string_sorted = "".join(sorted(string))
            if string_sorted in pairs:
                pairs[string_sorted].append(string)
            else:
                pairs[string_sorted] = [string]
        
        for key in pairs:
            final.append(pairs[key])
        
        return final




        