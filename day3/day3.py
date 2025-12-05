def day3_diff():
    K = 12
    total = 0

    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            remove = len(line) - K
            stack = []
            for char in line:
                while stack and remove > 0 and stack[-1] < char:
                    stack.pop()
                    remove -= 1
                stack.append(char)
            if remove > 0:
                stack = stack[:-remove]
            total += int("".join(stack[:K]))

    print(total)
        
def day3_easy():
    with open("input.txt", "r") as f:
        sol = 0
        for line in f:
            t = 0
            line = line.replace("\n","")
            for i in range(len(line)):
                for j in range(i + 1,len(line)):
                    if (int(line[i]) * 10) + int(line[j]) > t:
                        t = (int(line[i]) * 10) + int(line[j])    
            sol += t 
        print(sol)

if __name__ == "__main__":
    day3_easy()
    day3_diff()
