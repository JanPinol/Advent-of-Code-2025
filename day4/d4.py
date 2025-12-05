def process_matrix(matrix, rows, cols, total):
    for row_idx in range(rows):
        for col_idx in range(cols):
            if matrix[row_idx][col_idx] == "@":
                count = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        new_row = row_idx + i
                        new_col = col_idx + j
                        
                        if 0 <= new_row < rows and 0 <= new_col < cols:
                            if matrix[new_row][new_col] == "@":
                                count += 1
                
                if count < 4:
                    matrix[row_idx][col_idx] = "."
                    total += 1

    return total

        

def day4_diff():
    with open("input.txt", "r") as f:
        matrix = [list(line.strip()) for line in f]
    
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    total = 0
    while True:
        prev_total = total
        total = process_matrix(matrix, rows, cols, total)
        if total == prev_total:
            break
    print(total)
    


def day4_easy():
    with open("input.txt", "r") as f:
        matrix = [line.strip() for line in f]
    
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    total = 0
    
    for row_idx in range(rows):
        for col_idx in range(cols):
            if matrix[row_idx][col_idx] == "@":
                count = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        new_row = row_idx + i
                        new_col = col_idx + j
                        
                        if 0 <= new_row < rows and 0 <= new_col < cols:
                            if matrix[new_row][new_col] == "@":
                                count += 1
                
                if count < 4:
                    total += 1
    
    print(total)


if __name__ == "__main__":
    day4_easy()
    day4_diff()
