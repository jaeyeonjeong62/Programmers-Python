def solution(a, b):
    answer = 0
    res1 = str(a)+str(b)
    res2 = 2*a*b
    if int(res1)>res2:
        answer = int(res1)
    else:
        answer = res2
    return answer