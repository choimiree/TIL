T =int(input())
for tc in range(1, T+1):

    D31 = ['01', '03', '05', '07', '08', '10', '12']
    D30 = ['04', '06', '09', '11']
    D28 = ['02']
    Year = []
    Month = []
    Day = []

    N = list(map(str, input()))
#   N = list(map(int, input().split()))
    Year = ''.join(N[:4])
    Month = ''.join(N[4:6])
    Day = ''.join(N[6:8])
    #이제 D31에 속하고 Day가 32보다 작으면 print Year/Month/Day, 아니면 -1
    if Month in D31:
        if int(Day) < 32:
            print('#{} {}/{}/{}'.format(tc, Year, Month, Day))
        else:
            print('#{} {}'.format(tc, '-1'))
    elif Month in D30:
        if int(Day) < 31:
            print('#{} {}/{}/{}'.format(tc, Year, Month, Day))
        else:
            print('#{} {}'.format(tc, '-1'))
    elif Month in D28:
        if int(Day) < 29:
            print('#{} {}/{}/{}'.format(tc, Year, Month, Day))
        else:
            print('#{} {}'.format(tc, '-1'))
    else:
        print('#{} {}'.format(tc, '-1'))

    # if N[4][5] in D28 and N[6][7] in range(1,29):
    #     print(result)
    # elif N[4][5] in D30 and N[6][7] in range(1, 31):
    #     print(result)
    # elif N[4][5] in D30 and N[6][7] in range(1, 32):
    #     print(result)
    # else:
    #     print('-1')



'''

a = int(input())
k = []
year = []
month = []
day = []
 
 
 
D_31 = ['01', '03', '05', '07', '08', '10', '12']
D_30 = ['04', '06', '09', '11']
D_28 = ['02']
# 8개 짜리 스트링 받아오면 4개 ,2개 ,2개 순으로 짜르고
# 가운데 2개 우선 13보다 작은지 판별하고
# in 써서 저기에 들어가고 31보다 크면 false 조건문 여러개
 
for i in range(a):
    b = list(map(str, input()))
    year = ''.join(b[:4])
    month = ''.join(b[4:6])
    day =''.join(b[6:8])
    if month in D_31:
        if int(day) < 32:
            print('#{} {}/{}/{}'.format(i+1, year, month, day))
        else:
            print('#{} -1'.format(i+1))
    elif month in D_30:
        if int(day) < 31:
            print('#{} {}/{}/{}'.format(i+1, year, month, day))
        else:
            print('#{} -1'.format(i+1))
    elif month in D_28:
        if int(day) < 29:
            print('#{} {}/{}/{}'.format(i+1, year, month, day))
        else:
            print('#{} -1'.format(i+1))
    else:
        print('#{} -1'.format(i+1))
'''