def minion_game(s):
    vowels = ["A","E","I","O","U"]
    StuartList = set([c for c in s if c not in vowels])
    KevinList = set([c for c in s if c in vowels])
    print("Kevin list is", (KevinList))
    print("Stuart list is ", (StuartList))

    kevinWords = []
    stuartWords =  []

    for i in range(len(s)):
        if s[i] in StuartList:
            for j in range(i+1, len(s)+1):
                stuartWords.append(s[i:j])
    print("Stuart Words are ", stuartWords)

    for i in range(len(s)):
        if s[i] in KevinList:
            for j in range(i+1,len(s)+1):
                kevinWords.append(s[i:j])
    print("Kevin Words are", kevinWords)

    if len(kevinWords) > len(stuartWords):
        print("Kevin", len(kevinWords))
    else:
        print("Stuart", len(stuartWords))




if __name__ == "__main__":
    s = input()
    minion_game(s)