def print_formatted(number+1):
    width = len(bin(number)[2:])
    for i in range(1,number):
        Bin = bin(i)[2:]
        Oct = oct(i)[2:]
        Hex = hex(i)[2:]
        print(f"{str(i).rjust(width, ' ')} {Oct.rjust(width, ' ')} {Hex.rjust(width, ' ').upper()} {Bin.rjust(width, ' ')}")

if __name__ == "__main__":
    n = int(input())
    print_formatted(n)


