def read_input():
    points = []
    with open("input.txt", "r") as file:
        for line in file:
            coords = line.strip().split(",")
            points.append([int(coords[0]), int(coords[1])])
    return points


def calculate_area(p1, p2):
    width = abs(p1[0] - p2[0]) + 1
    height = abs(p1[1] - p2[1]) + 1
    return width * height


def build_segments(points):
    h_segments = []
    v_segments = []
    n = len(points)
    
    for i in range(n):
        p1 = points[i]
        p2 = points[(i + 1) % n]
        
        if p1[0] == p2[0]:
            x = p1[0]
            y_min = min(p1[1], p2[1])
            y_max = max(p1[1], p2[1])
            v_segments.append((x, y_min, y_max))
        else:
            y = p1[1]
            x_min = min(p1[0], p2[0])
            x_max = max(p1[0], p2[0])
            h_segments.append((y, x_min, x_max))
    
    return h_segments, v_segments


def get_interior_at_y(check_y, v_segments):
    crossings = []
    for x, y_min, y_max in v_segments:
        if y_min < check_y < y_max:
            crossings.append(x)
    crossings.sort()
    
    intervals = []
    for k in range(0, len(crossings), 2):
        if k + 1 < len(crossings):
            intervals.append((crossings[k], crossings[k + 1]))
    return intervals


def get_interior_at_x(check_x, h_segments):
    crossings = []
    for y, x_min, x_max in h_segments:
        if x_min < check_x < x_max:
            crossings.append(y)
    crossings.sort()
    
    intervals = []
    for k in range(0, len(crossings), 2):
        if k + 1 < len(crossings):
            intervals.append((crossings[k], crossings[k + 1]))
    return intervals


def merge_intervals(intervals):
    if not intervals:
        return []
    
    intervals.sort()
    merged = [list(intervals[0])]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    
    return [(s, e) for s, e in merged]


def get_intervals_at_y(y, v_segments, h_segments):
    h_at_y = []
    for hy, hx_min, hx_max in h_segments:
        if hy == y:
            h_at_y.append((hx_min, hx_max))
    
    interior_above = get_interior_at_y(y - 0.5, v_segments) if h_at_y else []
    interior_below = get_interior_at_y(y + 0.5, v_segments) if h_at_y else []
    interior_at = get_interior_at_y(y, v_segments)
    
    all_intervals = h_at_y + interior_at + interior_above + interior_below
    return merge_intervals(all_intervals)


def get_intervals_at_x(x, v_segments, h_segments):
    v_at_x = []
    for vx, vy_min, vy_max in v_segments:
        if vx == x:
            v_at_x.append((vy_min, vy_max))
    
    interior_left = get_interior_at_x(x - 0.5, h_segments) if v_at_x else []
    interior_right = get_interior_at_x(x + 0.5, h_segments) if v_at_x else []
    interior_at = get_interior_at_x(x, h_segments)
    
    all_intervals = v_at_x + interior_at + interior_left + interior_right
    return merge_intervals(all_intervals)


def is_range_covered(start, end, intervals):
    for iv_start, iv_end in intervals:
        if iv_start <= start and end <= iv_end:
            return True
    return False


def check_rectangle(p1, p2, h_segments, v_segments):
    x_min = min(p1[0], p2[0])
    x_max = max(p1[0], p2[0])
    y_min = min(p1[1], p2[1])
    y_max = max(p1[1], p2[1])
    
    for y in [y_min, y_max]:
        intervals = get_intervals_at_y(y, v_segments, h_segments)
        if not is_range_covered(x_min, x_max, intervals):
            return False
    
    for x in [x_min, x_max]:
        intervals = get_intervals_at_x(x, v_segments, h_segments)
        if not is_range_covered(y_min, y_max, intervals):
            return False
    
    critical_y = set()
    for hy, _, _ in h_segments:
        critical_y.add(hy)
    for _, vy_min, vy_max in v_segments:
        critical_y.add(vy_min)
        critical_y.add(vy_max)
    
    for y in critical_y:
        if y_min < y < y_max:
            intervals = get_intervals_at_y(y, v_segments, h_segments)
            if not is_range_covered(x_min, x_max, intervals):
                return False
    
    critical_x = set()
    for vx, _, _ in v_segments:
        critical_x.add(vx)
    for _, hx_min, hx_max in h_segments:
        critical_x.add(hx_min)
        critical_x.add(hx_max)
    
    for x in critical_x:
        if x_min < x < x_max:
            intervals = get_intervals_at_x(x, v_segments, h_segments)
            if not is_range_covered(y_min, y_max, intervals):
                return False
    
    return True


def day9_easy():
    points = read_input()
    n = len(points)
    
    max_area = 0
    for i in range(n):
        for j in range(i + 1, n):
            area = calculate_area(points[i], points[j])
            if area > max_area:
                max_area = area
    
    print(max_area)


def day9_diff():
    points = read_input()
    h_segments, v_segments = build_segments(points)
    n = len(points)
    
    max_area = 0
    for i in range(n):
        for j in range(i + 1, n):
            area = calculate_area(points[i], points[j])
            if area > max_area:
                if check_rectangle(points[i], points[j], h_segments, v_segments):
                    max_area = area
    
    print(max_area)


if __name__ == "__main__":
    day9_easy()
    day9_diff()
