def solution(n):
    answer = []

    for i in range(n):
        row = []

        for j in range(n):
            row.append(0)

        answer.append(row)

    x = 0
    y = 0

    turn_x = [1, 0, -1, 0]
    turn_y = [0, 1, 0, -1]
    flag = 0

    for i in range(1, n ** 2 + 1):
        answer[y][x] = i

        if i == n ** 2:
            break

        next_x = x + turn_x[flag]
        next_y = y + turn_y[flag]

        if (
            next_x < 0 or next_x >= n or
            next_y < 0 or next_y >= n or
            answer[next_y][next_x] != 0
        ):
            flag = (flag + 1) % 4

        x += turn_x[flag]
        y += turn_y[flag]

    return answer