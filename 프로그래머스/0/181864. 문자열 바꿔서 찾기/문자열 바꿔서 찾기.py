def solution(myString, pat):
    answer = 0
    s = ''
    for i in range(len(myString)):
        if myString[i] == "A":
            s += "B"
        else:
            s += "A"
    if pat in s:answer=1
    return answer