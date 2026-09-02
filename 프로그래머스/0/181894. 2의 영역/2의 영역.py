def solution(arr):
    answer = []
    s = 0
    e = 0
    for i in range(len(arr)):
        if arr[i] == 2:
            s = i
            break
    for i in range(len(arr) -1, -1, -1):
        if arr[i] == 2:
            e = i
            break
    if 2 not in arr:
        answer = [-1]
    else:
        answer = arr[s:e+1]
    return answer