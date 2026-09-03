def solution(myString, pat):
    answer = ''
    n = myString.rfind(pat)
    for i in range(n+len(pat)):
        answer += myString[i]
    return answer