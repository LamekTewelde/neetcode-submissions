class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pairs = {}
    
        for string in strs:
            string_sorted = "".join(sorted(string))
            if string_sorted in pairs:
                pairs[string_sorted].append(string)
            else:
                pairs[string_sorted] = [string]
        
    
        
        return list(pairs.values())




        