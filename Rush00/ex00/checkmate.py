# helper function
def find_king(grid):
    size = len(grid)
    for r in range(size):
        for c in range(size):
            if grid[r][c] == 'K':
                return r, c
    return -1, -1 #ถ้าไม่เห็น King ให้คืนค่าเป็น -1

#main function
def checkmate(board):
    #เปลี่ยน string ให้เป็น list 2 มิติ และตรวจความถูกต้องของหมาก
    rows = board.strip().split('\n')
    allowed_pieces = {'.', 'K', 'P', 'B', 'R', 'Q'}
    grid = []
    for row_idx, row_str in enumerate(rows):
        row_list = list(row_str)
        for col_idx, char in enumerate(row_list):
            if char not in allowed_pieces:
                #ให้แสดง error ถ้ามีหมากผิด
                print(f"Error: Invalid character '{char}' detected at position (row {row_idx}, col {col_idx}).") 
                print(f"Allowed pieces are: K (King), Q (Queen), R (Rook), B (Bishop), P (Pawn), and '.' (empty square).")
                print(f"Note: All pieces must be in UPPERCASE.")
                return 
        grid.append(row_list)

    size = len(grid)

    if not rows or rows == ['']:
        print("Error: Empty board.")
        return
    if any(len(row) != size for row in grid):
        print("Error: Board must be square.")
        return
    king_count = sum(row.count('K') for row in grid)
    if king_count != 1:
        print("Error: There must be exactly one King.")
        return
    
    #หาตำแหน่ง King
    k_row, k_col = find_king(grid)
    if k_row == -1:
        print("Error: No King found on the board!")
        return

    #เช็คแนวตรง
    def check_straight(grid,k_row,k_col):
        size=len(grid)
        directions=[
            (-1,0), #ขึ้น
            (1,0),  #ลง
            (0,-1), #ซ้าย
            (0,1)   #ขวา
        ]

        for change_row,change_col in directions:
            row=k_row+change_row
            col=k_col+change_col
            while 0<=row<size and 0<=col<size:
                if grid[row][col] in ['R','Q']:
                    return True
                if grid[row][col] != '.': #เพิ่มการเช็คตัวขวาง
                    break
                row+=change_row
                col+=change_col
        return False
    
    #เช็คแนวทแยง
    def check_diagonal(grid,k_row,k_col):
        size=len(grid)
        directions=[
            (-1,-1), #ซ้ายบน
            (-1,1),  #ขวาบน
            (1,-1),  #ซ้ายล่าง
            (1,1)    #ขวาล่าง
        ]

        for change_row,change_col in directions:
            row=k_row+change_row
            col=k_col+change_col
            while 0 <= row < size and 0 <= col < size:
                if grid[row][col] in ['B','Q']:
                    return True
                if grid[row][col] != '.': #เพิ่มการเช็คตัวขวาง
                    break
                row+=change_row
                col+=change_col
        return False
    
    #เช็คเบี้ย เพียงตำแหน่งใต้ทแยงซ้ายและขวา
    def check_pawn(grid, k_row, k_col):
        size = len(grid)
        pawn_directions = [(1, -1), (1, 1)] 
        for dr, dc in pawn_directions:
            r, c = k_row + dr, k_col + dc
            if 0 <= r < size and 0 <= c < size:
                if grid[r][c] == 'P':
                    return True
        return False
    
    #เรียกเช็ค
    if check_straight(grid,k_row,k_col):
        print("Success")
        return
    elif check_diagonal(grid,k_row,k_col):
        print("Success")
        return
    elif check_pawn(grid, k_row, k_col):
        print("Success")
        return
    else:
        print("Fail")
        return
