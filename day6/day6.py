def to_number(numList):
    s = map(str, numList)
    s = "".join(s)
    s = int(s)
    return s

def day6_diff():
    with open("input.txt", "r") as file:
        matrix = [line.replace("\n", "") for line in file]
        rows = len(matrix) - 1 
        cols = len(matrix[0])      
        
        matrix_sol = []
        for col in range(cols):
            num = []
            for row in range(rows):
                a = matrix[row][col]
                num.append(a)
            matrix_sol.append(num)
        
        op = matrix[-1].split()
        i_op = 0
        operator = op[0]
        sol, row_sol = 0, 0
        for row in range(len(matrix_sol)):
            empty = True
            for col in range(len(matrix_sol[row])):
                if matrix_sol[row][col] != ' ':
                    empty = False
                    break
                    
            if empty == True:
                i_op += 1
                operator = op[i_op]
                sol += row_sol
                row_sol = 0
                empty = False
                continue
            
            if operator == "+":
                row_sol += to_number(matrix_sol[row])
            else:
                if row_sol == 0:
                    row_sol = 1
                row_sol *= to_number(matrix_sol[row])
            
        print(sol + row_sol)

    
def day6_easy():
    with open("input.txt", "r") as file:
        matrix = [line.rstrip().split() for line in file]
        
        sol = 0
        for col in range(len(matrix[0])):
            i, sol_col = 0, 0
            operador = matrix[len(matrix) - 1][col]
            if operador == "*":
                sol_col = 1
            while i < len(matrix) - 1:
                if operador == "+":
                    sol_col += int(matrix[i][col])
                else:
                    sol_col *= int(matrix[i][col])
                i += 1   
            sol += sol_col                        
        print(sol)
                
        
if __name__ == "__main__":
    day6_easy()
    day6_diff()
