#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M,N = len(board),len(board[0])
        # tmp = [[None]*N for _ in range(M)]

        def check(r,c):
            p = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
            ch = 0
            for x,y in p:
                if 0<=y+r<M and 0<=c+x<N and board[r+y][c+x] >0:
                    ch +=1
            if board[r][c] >0:
                if ch <2:
                    return 2
                elif 2<=ch<=3:
                    return 1
                else:
                    return 2
            else:
                if ch ==3:
                    return -1
                else:
                    return 0
        
        for r in range(M):
            for c in range(N):
                board[r][c] = check(r,c)
        
        for r in range(M):
            for c in range(N):
                if board[r][c] ==2:
                    board[r][c] = 0       
                elif board[r][c] ==-1:
                    board[r][c] = 1
        
# @lc code=end

