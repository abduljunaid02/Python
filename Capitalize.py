import os
def solve(s):
    CapWords = []
    for i in range(len(s)):
        if s[i].isaplha() and (i==0 or s[i-1]== " "):
            cap= s[i].upper()
            CapWords.append(cap)
        

if __name__ == "__main__":
    #fptr = open(os.environ["OUTPUT_PATH"],"w")
    s = input()
    result = solve(s)
    print(result)
    #fptr.write(result+'\n')
    #fptr.close()
