def longestPalindromeSubstring(s: str):
    maxLen = 0
    lastPos = 0
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range (1, n + 1):
        dp[i][i] = 1
        maxLen = 1
        lastPos = i
    for i in range (1, n):
        if s[i - 1] == s[i]:
            dp[i][i + 1] = 1
            maxLen = 2
            lastPos = i + 1
    for l in range (3, n + 1):
        for i in range (1, n - l + 2):
            j = l + i - 1
            if s[i - 1] == s[j - 1] and dp[i + 1][j - 1]:
                dp[i][j] = 1
                maxLen = l
                lastPos = j
    for i in range (1, n + 1):
        for j in range (1, n + 1):
            print(dp[i][j], end=" ")
        print("")
    for i in range (lastPos - maxLen, maxLen + 1):
        print(s[i], end="")
    print()
s = "bananas"
longestPalindromeSubstring(s)