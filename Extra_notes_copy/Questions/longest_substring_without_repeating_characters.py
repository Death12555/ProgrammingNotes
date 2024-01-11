class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_set= set()
        
        start= 0
        end= 0
        max_length= 0
        
        while end<len(s):
            if s[end] not in unique_set:
                unique_set.add(s[end])
                end+= 1
                max_length= max(max_length, len(unique_set))

            else:
                unique_set.remove(s[start])
                start+= 1

        return max_length 