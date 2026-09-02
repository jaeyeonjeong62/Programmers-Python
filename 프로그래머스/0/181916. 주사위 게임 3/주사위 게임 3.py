def solution(a, b, c, d):
    answer = 0
    row = [a,b,c,d]
    row = sorted(row)
    s = set(row)
    s = sorted(s)
    if len(s)==1:
        answer = s[0]*1111
    elif len(s)==2:
        if row[1]!=row[2]:
            answer = (s[0]+s[1])*abs(s[0]-s[1])
        else:
            if row[0]!=row[1]:
                answer = (10*row[-1]+row[0])**2
            else:
                answer = (10*row[0]+row[-1])**2
    elif len(s)==4:
        answer = s[0]
    else:
        if a==b:
            answer = c*d
        elif a==c:
            answer = b*d
        elif a==d:
            answer = b*c
        elif b==c:
            answer = a*d
        elif b==d:
            answer = a*c
        elif c==d:
            answer = a*b
        
    return answer