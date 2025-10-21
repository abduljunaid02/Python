if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    avgScore = 0
    arrscore = list(student_marks[query_name])
    for i in range(len(arrscore)):
        avgScore = avgScore + arrscore[i]
    print("%.2f" %float(avgScore/3))
    print("Here is a change to be made")
