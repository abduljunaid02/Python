def count_substring(string, substring):
    count = 0
    string = "".join(string)
    substring = "".join(substring)
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count = count + 1
    return count

if __name__ == "__main__":
    string = input()
    substring = input()
    count = count_substring(string, substring)
    print(count)