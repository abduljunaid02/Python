import os
def solve(s):
    return "".join(c.upper() if i==0 or s[i-1] == " " else c for i,c in enumerate(s))

if __name__ == "__main__":
    #fptr = open(os.environ["OUTPUT_PATH"],"w")
    s = input()
    result = solve(s)
    print(result)
    #fptr.write(result+'\n')
    #fptr.close()
