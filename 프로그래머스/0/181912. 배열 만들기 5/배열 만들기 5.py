def solution(intStrs, k, s, l):
    answer = []
    for i in range(len(intStrs)):
        num = int(intStrs[i][s:s+l:])
        if num>k:
            answer.append(num)
    return answer