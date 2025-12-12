
def read_matrix(path="input.txt"):
    with open(path, "r") as f:
        return [list(line.rstrip()) for line in f]


def dfs(start_row, start_col, matrix, rows, cols, mem):
    # Terminal case: already computed
    if (start_row, start_col) in mem:
        return mem[(start_row, start_col)]

    # Terminal case: reached bottom
    if start_row + 1 >= rows:
        mem[(start_row, start_col)] = 1
        return 1

    # Terminal case: no obstacle below
    if matrix[start_row + 1][start_col] != "^":
        mem[(start_row, start_col)] = dfs(start_row + 1, start_col, matrix, rows, cols, mem)
        return mem[(start_row, start_col)]

    sol = 0

    # Explore
    sol += dfs(start_row + 1, start_col - 1, matrix, rows, cols, mem)
    sol += dfs(start_row + 1, start_col + 1, matrix, rows, cols, mem)

    mem[(start_row, start_col)] = sol
    
    return sol


def day7_diff():
    matrix = read_matrix("input.txt")
    rows = len(matrix)
    cols = len(matrix[0])

    for col in range(cols):
        if matrix[0][col] == "S":
            start_row, start_col = 0, col
            break

    mem = {}
    sol = dfs(start_row, start_col, matrix, rows, cols, mem)
    print(sol)


def day7_easy():
    matrix = read_matrix("input.txt")
    rows = len(matrix)
    cols = len(matrix[0])
    sol = 0
    for row in range(rows - 1):
        for col in range(cols):

            if matrix[row][col] == "S":
                matrix[row + 1][col] = "|"

            if matrix[row][col] == "|":
                below = matrix[row + 1][col]

                if below == "^":
                    sol += 1
                    if col - 1 >= 0 and matrix[row + 1][col - 1] != "^":
                        matrix[row + 1][col - 1] = "|"
                    if col + 1 < cols and matrix[row + 1][col + 1] != "^":
                        matrix[row + 1][col + 1] = "|"
                else:
                    matrix[row + 1][col] = "|"
    print(sol)

if __name__ == "__main__":
    day7_easy()
    day7_diff()
