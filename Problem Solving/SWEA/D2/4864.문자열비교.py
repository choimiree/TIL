## String-4864.문자열비교
#두개의 문자열 str1과 str2가 주어진다. 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.
#예를 들어 두 개의 문자열이 다음과 같이 주어질 때, 첫 문자열이 두번째에 존재하면 1, 존재하지 않으면 0을 출력한다.

# T=int(input())
# for tc in range(1, T+1):
#     N=input()
#     M=input()
#
#     result = 0
#     for i in range(len(M)-len(N)+1):
#         if M[i:i+len(N)] == N:
#             result += 1
#     print('#{} {}'.format(tc, result))


T=int(input())
for tc in range(1, T+1):
    N=input()
    M=input()
    result=0
    for i in range(len(M)-len(N)+1):
        if M[i:i+len(N)] == N:
            result += 1
    print('#{} {}'.format(tc, result))

