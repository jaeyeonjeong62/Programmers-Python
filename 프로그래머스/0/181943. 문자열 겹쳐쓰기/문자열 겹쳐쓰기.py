def solution(my_string, overwrite_string, s):
    answer = ''

    for i in range(s):
        answer += my_string[i]

    for i in range(len(overwrite_string)):
        answer += overwrite_string[i]

    start = len(answer)

    for i in range(start, len(my_string)):
        answer += my_string[i]

    return answer