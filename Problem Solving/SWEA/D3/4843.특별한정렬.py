#[4843. 특별한정렬]
#보통 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.
#N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.
#예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
#10 1 9 2 8 3 7 4 6 5
#주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오.

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     Ai = list(map(int, input().split()))
#     New_Ai = sorted(Ai)
#     result = []
#     while len(result) < 10:
#         result.append(New_Ai.pop(-1))
#         result.append(New_Ai.pop(0))
#     print(result)
#     final_result = ' '.join(map(str, result))
#     print('#{} {}'.format(tc, final_result))

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    ls=list(map(int,input().split()))
    #일단 오름차순으로 정렬
    new_ls=sorted(ls)
    # print(new_ls)
    #오름차순 한 거에서 가장 뒤에꺼[-1], 가장 첫번째꺼[0] pop 반복하면 원하는 값대로 정렬할 수 있음.
    result=[]
    while len(result) < 10:
        result.append(new_ls.pop(-1))
        result.append(new_ls.pop(0))
    #리스트형태를
    final_result=' '.join(map(str, result))
    print('#{} {}'.format(tc, final_result))


















