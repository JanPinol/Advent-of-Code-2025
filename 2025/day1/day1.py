def to_number(numList):
    s = map(str, numList)
    s = "".join(s)
    s = int(s)
    return s


def day1_easy():
    sol = 0
    pt = 50
    with open("input.txt", "r") as f:
        for line in f:
            number = to_number(line[1:])
            if line[0] == "L":
                pt = (pt - number) % 100
            else:
                pt = (pt + number) % 100

            if pt == 0:
                sol += 1
    print(sol)


def day1_diff():
    sol = 0
    pt = 50
    with open("input.txt", "r") as f:
        for line in f:
            number = to_number(line[1:])
            if line[0] == "L":
                while number != 0:
                    pt -= 1
                    pt %= 100
                    number -= 1
                    if pt == 0:
                        sol += 1
            else:
                while number != 0:
                    pt += 1
                    pt %= 100
                    number -= 1
                    if pt == 0:
                        sol += 1
    print(sol)


if __name__ == "__main__":
    day1_easy()
    day1_diff()
