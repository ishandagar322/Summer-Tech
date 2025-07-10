board =[["__","__","__","__","__","__","__"],["__","__","__","__","__","__","__"],["__","__","__","__","__","__","__"],["__","__","__","__","__","__","__"],["__","__","__","__","__","__","__"],["__","__","__","__","__","__","__"]]
for i in range(6):
    print(board[i])
tracker_column0 = 5 
tracker_column1 = 5
tracker_column2 = 5
tracker_column3 = 5
tracker_column4 = 5
tracker_column5 = 5
tracker_column6 = 5
winner = False
while winner == False:
    y = int(input("What column do you want to put your piece?")) 
    if y == 2: 
        board[tracker_column2][y] = "🔴"
        tracker_column2 -= 1
    if y == 0: 
        board[tracker_column0][y] = "🔴"
        tracker_column0 -= 1
    if y == 5: 
        board[tracker_column5][y] = "🔴"
        tracker_column5 -= 1
    if y == 1: 
        board[tracker_column1][y] = "🔴"
        tracker_column1 -= 1
    if y == 4: 
        board[tracker_column4][y] = "🔴"
        tracker_column4 -= 1
    if y == 3: 
        board[tracker_column3][y] = "🔴"
        tracker_column3 -= 1
    if y == 6: 
        board[tracker_column6][y] = "🔴"
        tracker_column6 -= 1  
    for i in range(6):
        for x in range(3):
            if board[i][x] == "🔴" and board[i][x+1] == "🔴" and board[i][x+2] == "🔴" and board[i][x+3] == "🔴":
                winner = True
                break 
    for i in range(2):
        for x in range(6):
            if board[i+1][x] == "🔴" and board[i+2][x] == "🔴" and board[i+3][x] == "🔴" and board[i+4][x] == "🔴":
                winner = True
                break 
    for i in range(3):
         for x in range(4): 
              if board[i][x] == "🔴" and board[i+1][x+1] == "🔴" and board[i+2][x+2] == "🔴" and board[i+3][x+3] == "🔴":
                   winner = True
                   break
    for i in range(3,6):
         for x in range(3):
              if board[i][x] == "🔴" and board[i-1][x+1] == "🔴" and board[i-2][x+2] == "🔴" and board[i-3][x+3] == "🔴":
                   winner = True
                   break
    for i in range(6):
        print(board[i])
    t = int(input("What column do you want to put your piece?")) 
    if t == 2: 
            board[tracker_column2][t] = "🟡"
            tracker_column2 -= 1
    if t == 0: 
            board[tracker_column0][t] = "🟡"
            tracker_column0 -= 1
    if t == 5: 
            board[tracker_column5][t] = "🟡"
            tracker_column5 -= 1
    if t == 1: 
            board[tracker_column1][t] = "🟡"
            tracker_column1 -= 1
    if t == 4: 
            board[tracker_column4][t] = "🟡"
            tracker_column4 -= 1
    if t == 3: 
            board[tracker_column3][t] = "🟡"
            tracker_column3 -= 1
    if t == 6: 
            board[tracker_column6][t] = "🟡"
            tracker_column6 -= 1     
    for i in range(6):
        print(board[i])
    

