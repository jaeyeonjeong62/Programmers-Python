def solution(myStr):
    myStr = myStr.replace("b", "a")
    myStr = myStr.replace("c", "a")

    answer = myStr.split("a")

    while "" in answer:
        answer.remove("")

    if len(answer) == 0:
        answer = ["EMPTY"]

    return answer