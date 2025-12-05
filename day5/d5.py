
def day5_diff():
    with open("input.txt", "r") as file:
        lines = [line.rstrip() for line in file.readlines()]

    ranges = []
    for line in lines[:lines.index("")]:
        low, high = map(int, line.split("-"))
        ranges.append((low, high))

    ranges.sort()

    total = 0
    start, end = ranges[0]
    for s, e in ranges[1:]:
        if s <= end + 1:
            end = max(end, e)
        else:
            total += end - start + 1
            start, end = s, e

    total += end - start + 1

    print(total)



    
def day5_easy():
    with open("input.txt", "r") as file:
        lines = [line.rstrip() for line in file.readlines()]
        numbers = lines[lines.index("") + 1:]
        sol = 0
        for n in numbers:
            for line in lines[:lines.index("")]:
                min = int(line.split("-")[0])
                max = int(line.split("-")[1])
                if int(n) in range(min, max + 1):
                    sol += 1
                    break
        print(sol)
        
if __name__ == "__main__":
    day5_easy()
    day5_diff()
