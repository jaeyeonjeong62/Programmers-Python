def solution(order):
    answer = 0
    for menu in order:
        if menu == "anything":
            answer += 4500
        elif "americano" in menu:
            answer += 4500
        elif "cafelatte" in menu:
            answer += 5000
    return answer