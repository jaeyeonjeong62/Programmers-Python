def solution(my_string, indices):
    answer = ''
    my_string = list(my_string)
    for i in range(len(indices)):
        my_string[indices[i]]='1'
    for i in range(len(my_string)):
        if my_string[i] != '1':
            answer += my_string[i]
    return answer