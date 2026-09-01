def solution(a, b):
    answer = 0
    res1 = str(a)+str(b)
    res2 = str(b)+str(a)
    if int(res1)>int(res2):
        answer = int(res1)
    else:
        answer = int(res2)
    return answer