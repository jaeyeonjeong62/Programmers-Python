def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if "1" in str(i) or "2" in str(i) or "3" in str(i) or "4" in str(i) or "6" in str(i) or "7" in str(i) or "8" in str(i) or "9" in str(i):
            continue
        else:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    return answer