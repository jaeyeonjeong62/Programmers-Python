def solution(a, b):
    answer = ''
    num_a = 0
    for i in range(len(a)):
        num_a = num_a*10 + int(a[i])
    num_b = 0
    for i in range(len(b)):
        num_b = num_b*10 + int(b[i])
    answer_int = num_a + num_b
    if answer_int == 0: return '0'
    while answer_int != 0:
        answer += str(answer_int%10)
        answer_int = answer_int//10
    answer = answer[::-1]
    return answer