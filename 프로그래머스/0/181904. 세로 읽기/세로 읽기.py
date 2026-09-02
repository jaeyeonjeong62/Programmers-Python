def solution(my_string, m, c):
    answer = ''
    array = []

    for i in range(len(my_string) // m):
        row = []

        for j in range(m):
            row.append(my_string[i * m + j])

        array.append(row)

    for i in range(len(array)):
        answer += array[i][c - 1]

    return answer