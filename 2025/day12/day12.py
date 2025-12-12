def read_input():
    shapes = {}
    regions = []
    with open("input.txt", "r") as file:
        content = file.read().strip()
    
    parts = content.split("\n\n")
    
    for part in parts[:-1]:
        lines = part.strip().split("\n")
        idx = int(lines[0].rstrip(":"))
        shape = set()
        for r, line in enumerate(lines[1:]):
            for c, ch in enumerate(line):
                if ch == "#":
                    shape.add((r, c))
        shapes[idx] = shape
    
    for line in parts[-1].strip().split("\n"):
        size_part, counts_part = line.split(": ")
        w, h = map(int, size_part.split("x"))
        counts = list(map(int, counts_part.split()))
        regions.append((w, h, counts))
    
    return shapes, regions


def day12_easy():
    shapes, regions = read_input()
    sol = 0
    
    shape_areas = {}
    for idx, shape in shapes.items():
        shape_areas[idx] = len(shape)
    
    for w, h, counts in regions:
        region_area = w * h
        
        pieces_area = 0
        for idx, count in enumerate(counts):
            pieces_area += count * shape_areas[idx]
        
        if pieces_area <= region_area:
            sol += 1
    
    print(sol)


def day12_diff():
    shapes, regions = read_input()
    sol = 0
    print(sol)


if __name__ == "__main__":
    day12_easy()
    day12_diff()
