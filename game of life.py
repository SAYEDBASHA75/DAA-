def gameOfLife(board):
    m = len(board)
    n = len(board[0])
    
    copyBoard = [row[:] for row in board]
   
    def countLiveNeighbors(board, i, j):
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        liveNeighbors = 0
        
        for direction in directions:
            newRow, newCol = i + direction[0], j + direction[1]
            if 0 <= newRow < m and 0 <= newCol < n:
                liveNeighbors += board[newRow][newCol]
        
        return liveNeighbors
    
    for i in range(m):
        for j in range(n):
            liveNeighbors = countLiveNeighbors(copyBoard, i, j)
            
            # Rule 1 and Rule 3: Any live cell with fewer than 2 or more than 3 neighbors dies
            if copyBoard[i][j] == 1 and (liveNeighbors < 2 or liveNeighbors > 3):
                board[i][j] = 0
            
            # Rule 2: Any live cell with 2 or 3 neighbors survives
            elif copyBoard[i][j] == 1 and (liveNeighbors == 2 or liveNeighbors == 3):
                board[i][j] = 1
                
            # Rule 4: Any dead cell with exactly 3 live neighbors becomes a live cell
            elif copyBoard[i][j] == 0 and liveNeighbors == 3:
                board[i][j] = 1

board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]
gameOfLife(board)
print(board)

Output:[[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
