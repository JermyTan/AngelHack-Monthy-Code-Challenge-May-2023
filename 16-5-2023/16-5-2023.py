def compute(board) -> None:
    m = len(board)
    n = len(board[0])
    copy = [row.copy() for row in board]
    
    def get(i, j):
        return copy[i][j] if 0 <= i < m and 0 <= j < n else 0
    
    def get_live_count(i, j):
        return sum(get(x, y) for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)))
    
    for i in range(m):
        for j in range(n):
            live_count = get_live_count(i, j)
            
            if copy[i][j] == 0:
                if live_count == 1 or live_count == 2:
                    board[i][j] = 1
                
                continue
            
            if live_count == 1:
                continue
            
            board[i][j] = 0

board = [
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1]
]

seen = set()
board_str = str(board)

while board_str not in seen:
    seen.add(board_str)
    
    compute(board)

    board_str = str(board)

score = 0
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j]:
            score += 2**(i * len(board[0]) + j)

print(score)