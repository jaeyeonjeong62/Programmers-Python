def solution(my_string):
    answer = []
    for i in range(26):
        num = 0
        if chr(ord('A')+i) in my_string:
            for j in range(len(my_string)):
                if my_string[j] == chr(ord('A')+i):
                    num +=1
        answer.append(num)
    for i in range(26):
        num = 0
        if chr(ord('a')+i) in my_string:
            for j in range(len(my_string)):
                if my_string[j] == chr(ord('a')+i):
                    num +=1
        answer.append(num)
        
    return answer