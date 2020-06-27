def solution(array, commands):
    answer = []
    for com in commands:
        answer.append(sorted(array[com[0]-1:com[1]])[com[2]-1])
    return answer

'''
def solution(array, commands):
    answer = []
    for i in commands:
        arr=sorted(array[i[0]-1:i[1]])
        answer.append(arr[i[2]-1])
    return answer


def solution(array, commands):
    answer = []
    for i in commands:
        temp = array[i[0]-1:i[1]]
        temp.sort()
        answer.append(temp[i[2]-1])
    return answer
'''
