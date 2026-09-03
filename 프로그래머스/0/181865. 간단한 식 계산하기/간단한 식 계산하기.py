def solution(binomial):
    answer = 0
    l = binomial.split()
    if l[1] == "+":
        answer = int(l[0])+int(l[2])
    elif l[1] == "-":
        answer = int(l[0])-int(l[2])
    else:
        answer = int(l[0])*int(l[2])
    return answer