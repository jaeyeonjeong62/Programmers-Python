def solution(arr):
    answer = [[]]
    row_num = len(arr)
    col_num = len(arr[0])
    
    if row_num > col_num:
        for i in range(row_num):
            arr[i].extend([0]*(row_num-col_num))
    elif row_num < col_num:
        for i in range(col_num-row_num):
            arr.append([0]*col_num)

    answer = arr   
    return answer