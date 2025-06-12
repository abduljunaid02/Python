def merge_the_tools(string,k):

    stringList = [string[i:i+k] for i in range(0, len(string), k)]
    for word in stringList:
        result = ""
        uniqueWord = set()
        for char in word:
            if char not in uniqueWord:
                uniqueWord.add(char)
                result+=char
        print(result)

if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string,k)