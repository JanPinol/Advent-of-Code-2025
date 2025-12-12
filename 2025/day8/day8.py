def read_input():
    with open("input.txt", "r") as file:
        points = []
        for line in file:
            coords = line.strip().split(",")
            points.append([int(coords[0]), int(coords[1]), int(coords[2])])
        return points

def distance(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def day8_easy():
    points = read_input()
    n = len(points)
    
    distances = []
    for i in range(n):
        for j in range(i+1, n):
            dist = distance(points[i], points[j])
            distances.append((dist, i, j))
    
    distances.sort()
    
    parent = list(range(n))
    size = [1] * n
    
    for k in range(n):
        _, i, j = distances[k]
        pi = find(parent, i)
        pj = find(parent, j)
        if pi != pj:
            parent[pj] = pi
            size[pi] += size[pj]
    
    circuit_sizes = []
    for i in range(n):
        if parent[i] == i:
            circuit_sizes.append(size[i])
    
    circuit_sizes.sort(reverse=True)
    result = circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]
    print(result)


def day8_diff():
    points = read_input()
    n = len(points)
    
    distances = []
    for i in range(n):
        for j in range(i+1, n):
            dist = distance(points[i], points[j])
            distances.append((dist, i, j))
    
    distances.sort()
    
    parent = list(range(n))
    size = [1] * n
    num_circuits = n
    sol = 0
    for k in range(len(distances)):
        _, i, j = distances[k]
        pi = find(parent, i)
        pj = find(parent, j)
        if pi != pj:
            parent[pj] = pi
            size[pi] += size[pj]
            num_circuits -= 1
            
            if num_circuits == 1:
                sol = points[i][0] * points[j][0]
                break
    print(sol)

if __name__ == "__main__":
    day8_easy()
    day8_diff()