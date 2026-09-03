def solution(myString):
    answer = myString.split("x")
    l = []
    for i in range(len(answer)):
        l.append(len(answer[i]))
    return l