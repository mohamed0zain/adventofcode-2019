with open("input/day06.txt") as file:
    input = file.read().splitlines()

orbit_map = {}

for line in input:
    orbited = line[: line.index(")")]
    orbiting = line[line.index(")") + 1 :]
    orbit_map[orbiting] = orbited


def count_orbits(planet):
    if planet == "COM":
        return 0
    return 1 + count_orbits(orbit_map[planet])


def get_orbited(planet, orbited):
    orbited.append(planet)
    if planet != "COM":
        get_orbited(orbit_map[planet], orbited)


def part1():
    total = 0
    for planet in orbit_map.keys():
        total += count_orbits(planet)
    return total


def part2():
    you_orbiting = []
    san_orbiting = []
    get_orbited(orbit_map["YOU"], you_orbiting)
    get_orbited(orbit_map["SAN"], san_orbiting)

    for planet in you_orbiting:
        if planet in san_orbiting:
            common_planet = planet
            break

    return you_orbiting.index(common_planet) + san_orbiting.index(common_planet)


print(part1())
print(part2())
