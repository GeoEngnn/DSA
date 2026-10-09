class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        lenght=0
        max_freq=0  ## s= AAABABBC
        max_len=0
        map={}

        for r in range(len(s)):
            if s[r] in map:
                map[s[r]] += 1
            else:
               map[s[r]] = 1

            max_freq = max(max_freq, map[s[r]])
            
            lenght += 1

            

            if lenght - max_freq <= k:
                max_len=max(max_len , r -left +1)

            else:
                map[s[left]] -= 1
                left += 1
                lenght -= 1

        return max_len 

        