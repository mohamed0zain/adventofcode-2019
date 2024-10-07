def validate_input(input_data, expected_size):
    if len(input_data) % expected_size != 0:
        raise ValueError("Input data size is not a multiple of the expected layer size.")
    return input_data

def parse_layers(input_data, width, height):
    layer_size = width * height
    return [input_data[i:i + layer_size] for i in range(0, len(input_data), layer_size)]

def part1(layers):
    min_zeros = float('inf')
    result = 0
    for layer in layers:
        zeros = layer.count('0')
        if zeros < min_zeros:
            min_zeros = zeros
            result = layer.count('1') * layer.count('2')
    print(result)

def part2(layers, width, height):
    layer_size = width * height
    image = ['2'] * layer_size
    for layer in layers:
        for i, pixel in enumerate(layer):
            if image[i] == '2':  # Only replace transparent pixels
                image[i] = pixel
    for i in range(0, layer_size, width):
        print("".join(image[i:i + width]).replace('1', '#').replace('0', '.'))

# Main script
with open("input/day08.txt") as file:
    input_data = validate_input(file.read().strip(), 25 * 6)

width = 25
height = 6
layers = parse_layers(input_data, width, height)

part1(layers)
part2(layers, width, height)
