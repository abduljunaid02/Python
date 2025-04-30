def swap_case(s):
    return  "".join(char.lower() if char.isupper() else char.upper() for char in s)

if __name__ == "__main__":
    inpStr = input()
    print(swap_case(inpStr))

#Learnings --- To check the case of the letter use isupper() islower()
#Join method to join the strings are only used when there is an iterator in the bracket. " ".join(iterator)
# To join here use +=  