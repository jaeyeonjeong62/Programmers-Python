def solution(arr):
    answer = []
    for i in range(len(arr)):
        num = arr[i]
        for j in range(num):
            answer.append(num)
    return answer