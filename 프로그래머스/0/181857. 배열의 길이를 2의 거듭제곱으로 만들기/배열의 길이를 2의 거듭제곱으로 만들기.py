def solution(arr):
    answer = arr
    k = -1
    while not(len(arr) >= 2**k and len(arr) <= 2**(k+1)):
        k += 1
    while len(arr) != 2**(k+1):
        answer.append(0)
    return answer