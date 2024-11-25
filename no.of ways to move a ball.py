# Given an m x n grid and a ball at a starting cell, find the number of ways to move the ball out of the grid boundary in exactly N steps.
def findPaths(m, n, N, i, j):
    MOD = 10**9 + 7
    dp = [[[0] * n for _ in range(m)] for _ in range(N+1)]
    dp[0][i][j] = 1
    count = 0
    for step in range(1, N + 1):
        new_dp = [[0] * n for _ in range(m)]
        for x in range(m):
            for y in range(n):
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        new_dp[x][y] = (new_dp[x][y] + dp[step-1][nx][ny]) % MOD
                    else:
                        count = (count + dp[step-1][x][y]) % MOD
        dp[step] = new_dp    
    return count
print(findPaths(1,3,3,0,1))
