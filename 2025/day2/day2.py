def day2_diff():
    with open("input.txt", "r") as f:
        x = f.read().replace("\n", "").split(",")
        sol = 0
        for item in x:
            a = item.split("-")
            i = 0
            while int(a[0]) + i <= int(a[1]):
                number = str(int(a[0]) + i)
                i += 1
                length = len(number)
                for j in range(1, int(length / 2) + 1):
                    if length % j == 0:
                        part = number[:j]
                        times = length // j
                        if part * times == number:
                            sol += int(number)
                            break
        print(sol)

def day2_easy():
    with open("input.txt", "r") as f:
        x = f.read().replace("\n", "").split(",")
        sol = 0
        for item in x:
            a = item.split("-")
            i = 0
            while int(a[0]) + i <= int(a[1]):
                number = str(int(a[0]) + i)
                i += 1
                left = number[: int((len(number)) / 2)]
                right = number[int((len(number)) / 2) :]
                if left == right:
                    sol += int(number)

        print(sol)


if __name__ == "__main__":
    day2_easy()
    day2_diff()
