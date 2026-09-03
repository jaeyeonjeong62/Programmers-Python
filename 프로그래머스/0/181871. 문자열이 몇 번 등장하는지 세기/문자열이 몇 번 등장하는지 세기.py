def solution(myString, pat):
    answer = 0
    num = myString.find(pat)
    for i in range(num,len(myString)-len(pat)+1):
        if pat in myString[i:i+len(pat)]:
            answer += 1
    return answer