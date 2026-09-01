def solution(arr, queries):
    answer = []
    for i in range(len(queries)):
        k = 1000001
        for j in range(queries[i][0],queries[i][1]+1):
            if arr[j] < k and arr[j] > queries[i][2]:
                k = arr[j]
        if k == 1000001:
            answer.append(-1)
        else:
            answer.append(k)
        
    return answer