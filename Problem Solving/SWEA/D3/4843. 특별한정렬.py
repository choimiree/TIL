for tc in range(1, int(input())+1):
    N=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    #선택정렬
    for i in range(N-2+1): #최소값을 찾을 범위의 시작
        if i % 2 == 0: #짝수일때는 큰 값 순서로 배열
            idx = i
            for j in range(i+1, N):
                if arr[idx] < arr[j]: idx=j
            arr[i], arr[idx] = arr[idx], arr[i]
        else: #홀수는 작은 값 순서로 배열
            idx = i
            for j in range(i+1,N):
                if arr[idx] > arr[j]: idx = j
            arr[i], arr[idx] = arr[idx], arr[i]
    final_arr = ' '.join(map(str, arr))
    print('#{} {}'.format(tc, final_arr))