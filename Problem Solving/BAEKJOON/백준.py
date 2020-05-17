#1. <조건문> 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
score = int(input())
grade = 'A' if score >=90 else 'B' if score >= 80 else 'C' ...
#1-1.
score = int(input())
grade = ''
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'

# 1-2.
score = int(input())
if 90 <= score <= 100:
    print('A')
elif 80 <= score < 90:
    print('B')
elif 70 <= score < 80:
    print('C')
elif 60 <= score < 70:
    print('D')
else:
    print('F')

#2. <반복문> N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.
gugu = int(input())
i = 0
while i <= 9:
    print('{} * {} = {}'.format(gugu, i, gugu * i))
    i+=1

#3. <For문>
# 0~10까지의 합
sum = 0
for i in range(0, 10+1):
    sum += i
print(sum)
# 0~10까지 짝수의 합
sum = 0
for i in range(0, 10+1, 2):
    sum += i
print(sum)
'''
*
**
***
****
***** 만들기
'''
for j in range(5+1):
    for i in range(j):
        print('*', end='')
    print()

#4. <2차원배열>