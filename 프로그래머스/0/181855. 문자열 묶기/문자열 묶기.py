def solution(strArr):
    cnt = {}

    for i in range(len(strArr)):
        length = len(strArr[i])
        cnt[length] = cnt.get(length, 0) + 1

    return max(cnt.values())