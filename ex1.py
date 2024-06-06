def print_longest_name(filename):
    with open(filename) as file:
        names = file.read().splitlines()
    longest_name = max(names, key=len)
    print(longest_name)

def print_total_length(filename):
    with open(filename) as file:
        names = file.read().splitlines()
    total_length = sum(len(name) for name in names)
    print("Total length of all names in the file:", total_length)

def print_shortest_names(filename):
    with open(filename) as file:
        names = file.read().splitlines()
    min_length = min(len(name) for name in names)
    shortest_names = [name for name in names if len(name) == min_length]
    print("Shortest names in the file:")
    for name in shortest_names:
        print(name)

def create_name_length_file(input_filename, output_filename):
    with open(input_filename) as infile:
        names = infile.read().splitlines()
    with open(output_filename, 'w') as outfile:
        for name in names:
            outfile.write(f"{len(name)}\n")
    print(f"Name lengths written to {output_filename}")

def print_names_of_length(filename, length):
    with open(filename) as file:
        names = file.read().splitlines()
    filtered_names = [name for name in names if len(name) == length]
    print(f"Names of length {length} in the file:")
    for name in filtered_names:
        print(name)

def main():
    filename = "/Users/UriahCohen/Desktop/names.txt"
    output_filename = "C:\\Users\\User\\python2.txt"
    length_to_find = 4

    print_longest_name(filename)
    print_total_length(filename)
    print_shortest_names(filename)
    create_name_length_file(filename, output_filename)
    print_names_of_length(filename, length_to_find)

main()
