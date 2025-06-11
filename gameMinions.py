def minion_game(s):

    vowels = "AEIOU"
    kevin_score = 0
    stuart_score = 0
    l = len(s)

    for i in range(l):
        if s[i] in vowels:
            kevin_score += l-i
        else:
            stuart_score += l-i

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")






if __name__ == "__main__":
    s = input()
    minion_game(s)