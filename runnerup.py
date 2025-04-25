if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    sortArr =  sorted(set(arr))
    print("The runner up is ", sortArr[-2])