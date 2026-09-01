def solution(num_list):
    answer = 0
    mul = 1
    plus = 0
    for i in range(len(num_list)):
        mul *= num_list[i]
    for i in range(len(num_list)):
        plus += num_list[i]
    plus = plus**2
    if mul < plus:
        answer = 1
    return answer