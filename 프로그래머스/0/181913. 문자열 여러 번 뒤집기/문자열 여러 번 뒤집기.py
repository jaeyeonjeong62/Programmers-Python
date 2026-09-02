def solution(my_string, queries):
    for i in range(len(queries)):
        s = queries[i][0]
        e = queries[i][1]
        answer = ''

        # s 이전 부분
        for j in range(0, s):
            answer += my_string[j]

        # s부터 e까지 역순
        for j in range(e, s - 1, -1):
            answer += my_string[j]

        # e 이후 부분
        for j in range(e + 1, len(my_string)):
            answer += my_string[j]

        my_string = answer

    return my_string