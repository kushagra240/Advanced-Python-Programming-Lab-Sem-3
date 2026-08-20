def lcs(x: str, y: str) -> str:
    m = len(x)
    n = len(y)
    lcs_table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lcs_table[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])

    index = lcs_table[m][n]
    lcs_chars = [""] * index
    i = m
    j = n

    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            lcs_chars[index - 1] = x[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif lcs_table[i - 1][j] > lcs_table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs_chars)


if __name__ == "__main__":
    x = "AGGTAB"
    y = "GXTXAYB"
    print("Longest Common Subsequence:", lcs(x, y))
