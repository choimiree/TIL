##[flatten(D3)]
#높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격 줄이는 작업을 평탄화라 한다.
#평탄화를 모두 수행하고 나면, 가장 높은 곳과 낮은 곳의 차이가 최대 1 이내가 된다.
#평탄화를 위해 상자를 옮기는 작업 횟수에 제한이 있을 때, 최고점과 최저점의 차이 반환.
#가장 높은 곳에서 가장 낮은 곳으로 옮기는 작업을 덤프라고 정의.
#가로100 세로 100이하, 덤프 1000이하.
T = 10
for tc in range(10):
N = int(input()) #덤프횟수
h_ls = list(map(int, input().split()))
dump_max = []
dump_min = []
for i in range(len(h_ls)):
    if h_ls[i] == max(h_ls):
        dump_max.append(h_ls[i])
for i in range(len(h_ls)):
    if h_ls[i] == min(h_ls):
        dump_min.append(h_ls[i])

result = dump_max[i] - dump_min[i]
print(result)
