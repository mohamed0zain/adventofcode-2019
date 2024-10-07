with open("input/day03.txt") as file:
    input = file.read().splitlines()


def get_coords(wire_path):
    coords = {}
    step_count = 0
    x = 0
    y = 0

    for step in wire_path.split(","):
        direction = step[:1]
        distance = step[1:]

        for _ in range(int(distance)):
            step_count += 1
            if direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            elif direction == "U":
                y += 1
            elif direction == "D":
                y -= 1

            coords[(x, y)] = step_count

    return coords


def exec():
    wire1_coords = get_coords(input[0])
    wire2_coords = get_coords(input[1])

    intersections = set(wire1_coords) & set(wire2_coords)

    min_distance = 0
    min_steps = 0

    min_distance = min([abs(x) + abs(y) for (x, y) in intersections])
    min_steps = min([wire1_coords[(x, y)] + wire2_coords[(x, y)] for (x, y) in intersections])

    print(min_distance)
    print(min_steps)


exec()
