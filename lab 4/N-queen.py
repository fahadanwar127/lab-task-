def solve_n_queens(N):
    
    board = [-1] * N
    solutions = []

    
    columns = set()
    positive_diag = set()
    negative_diag = set()

    
    def place_queen(row):
        
        if row == N:
            solution = []
            for i in range(N):
                solution.append("." * board[i] + "Q" + "." * (N - board[i] - 1))
            solutions.append(solution)
            return

        for col in range(N):
            
            if col in columns or (row - col) in positive_diag or (row + col) in negative_diag:
                continue

        
            board[row] = col
            columns.add(col)
            positive_diag.add(row - col)
            negative_diag.add(row + col)

            
            place_queen(row + 1)

            
            columns.remove(col)
            positive_diag.remove(row - col)
            negative_diag.remove(row + col)

    
    place_queen(0)

    return solutions


N = 4
solutions = solve_n_queens(N)


print(f"Total solutions for {N}-Queens: {len(solutions)}")
for sol in solutions:
    for row in sol:
        print(row)
    print()
