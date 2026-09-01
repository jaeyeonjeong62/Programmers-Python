def solution(str1, str2):
    answer = ''
    total = str1+str2
    for i in range(len(total)):
        if i%2==0:
            answer += str1[i//2]
        else:
            answer += str2[i//2]
                
    return answer