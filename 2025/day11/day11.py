def read_input():
    graph = {}
    with open("input.txt", "r") as file:
        for line in file:
            parts = line.strip().split(": ")
            source = parts[0]
            destinations = parts[1].split() if len(parts) > 1 else []
            graph[source] = destinations
    return graph


def day11_easy():
    graph = read_input()
    sol = 0
    stack = [("you", ["you"])]
    
    while stack:
        node, path = stack.pop()
        
        if node == "out":
            sol += 1
            continue
        
        if node not in graph:
            continue
            
        for neighbor in graph[node]:
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor]))
    
    print(sol)


def count_recursive(graph, node, has_dac, has_fft, cache):
    if node == "dac":
        has_dac = True
    if node == "fft":
        has_fft = True
    
    key = (node, has_dac, has_fft)
    if key in cache:
        return cache[key]
    
    if node == "out":
        result = 1 if (has_dac and has_fft) else 0
        cache[key] = result
        return result
    
    if node not in graph:
        cache[key] = 0
        return 0
    
    total = 0
    for neighbor in graph[node]:
        total += count_recursive(graph, neighbor, has_dac, has_fft, cache)
    
    cache[key] = total
    return total


def day11_diff():
    graph = read_input()
    cache = {}
    sol = count_recursive(graph, "svr", False, False, cache)
    print(sol)


if __name__ == "__main__":
    day11_easy()
    day11_diff()