def countSubstring(s):

    # Length of string
    n = len(s)

    # Frequency counters
    cntA = cntB = cntC = 0

    # Left pointer
    l = 0

    # Store result
    ans = 0

    # Traverse with right pointer
    for r in range(n):

        # Include current character
        if s[r] == 'a':
            cntA += 1
        if s[r] == 'b':
            cntB += 1
        if s[r] == 'c':
            cntC += 1

        # Shrink window while valid
        while cntA > 0 and cntB > 0 and cntC > 0:

            # Count substrings ending at r
            ans += (n - r)

            # Remove left character
            if s[l] == 'a':
                cntA -= 1
            if s[l] == 'b':
                cntB -= 1
            if s[l] == 'c':
                cntC -= 1

            # Move left pointer
            l += 1

    return ans

print(countSubstring('bbacba'))