class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        tab = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            tab[i][0] = 1
            
        for i in range(n):
            tab[0][i] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                tab[i][j] = tab[i-1][j]+tab[i][j-1]
        return tab[m-1][n-1]