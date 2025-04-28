if __name__ == '__main__':
    N = int(input())
    myList = []
    for _ in range(N):
        readInp = input().split()
        command = readInp[0]
        args = list(map(int, readInp[1:]))
        if command == "print":
            print(myList)
        else:
            getattr(myList, command)(*args)
