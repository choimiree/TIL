# 2차원 List

## 2차원 List(1)

- List 탐색
  - 행 우선 탐색, 열 우선 탐색, 지그재그 탐색, 델타를 이이용한 탐색

1. 행 우선 탐색

   - 행을 차례대로 탐색해 나가는 방법.

   ```python
   #행 우선 탐색
   
   A = [['{0:2d}'.format(i) for i in range(j, j+5)] for j in range(1, 26, 5)]
   
   for i in range(5):
       print(*A[i])
       
   #행 우선 탐색
   for i in range(5):
       for j in range(5):
           print(A[i][j], end=' ')
   print()
   
   # 출력
    1  2  3  4  5
    6  7  8  9 10
   11 12 13 14 15
   16 17 18 19 20
   21 22 23 24 25
   >>>  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
   ```

   

2. 열 우선 탐색

   - 열을 차례대로 탐색해 나가는 방법이다.

```python
# 열 우선 탐색

A = [['{0:2d}'.format(i) for i in range(j, j+5)] for j in range(1, 26, 5)]

for i in range(5):
    print(*A[i])
    
#열 우선 탐색
for i in range(5):
    for j in range(5):
        print(A[j][i], end=' ')
print()

#출력
 1  2  3  4  5
 6  7  8  9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
>>>  1  6 11 16 21  2  7 12 17 22  3  8 13 18 23  4  9 14 19 24  5 10 15 20 25
```



3. 지그재그 탐색

   - 지그재그로 행 또는 열을 탐색해 나가는 방법이다.

     a. 행 우선 지그재그 탐색

     ```python
     #행 우선 지그재그 탐색
     A = [['{0:2d}'.format(i) for i in range(j, j+5)] for j in range(1, 26, 5)]
     
     for i in range(5):
         print(*A[i])
         
     #지그재그 탐색 - 행
     for i in range(5):
         for j in range(5):
             print(A[i][j+(5 - 1 - 2 * j) * (i % 2)], end=' ')	#5 = 행의 길이
     print()
     
     # 출력
      1  2  3  4  5
      6  7  8  9 10
     11 12 13 14 15
     16 17 18 19 20
     21 22 23 24 25
     >>>  1  2  3  4  5 10  9  8  7  6 11 12 13 14 15 20 19 18 17 16 21 22 23 24 25
             
     ```

     a. 열 우선 지그재그 탐색

     ```python
     #열 우선 지그재그 탐색
     A = [['{0:2d}'.format(i) for i in range(j, j+5)] for j in range(1, 26, 5)]
     
     for i in range(5):
         print(*A[i])
         
     #지그재그 탐색 - 열
     for i in range(5):
         for j in range(5):
             print(A[j+(5 - 1 - 2 * j) * (i % 2)][i], end=' ')
     print()
     
     # 출력
      1  2  3  4  5
      6  7  8  9 10
     11 12 13 14 15
     16 17 18 19 20
     21 22 23 24 25
     # python 예시 - 열 우선 지그재그 탐색
         
         A = [['{0:2d}'.format(i) for i in range(j, j+5)] for j in range(1, 26, 5)]
         
         for i in range(5):
             print(*A[i])
             
         # 지그재그 탐색 - 열
         for i in range(5):
             for j in range(5):
                 print(A[j + (5 - 1 - 2 * j) * (i % 2)][i], end=' ')
         print()
         
         # 출력
          1  2  3  4  5
          6  7  8  9 10
         11 12 13 14 15
         16 17 18 19 20
         21 22 23 24 25
         >>>  1  6 11 16 21 22 17 12  7  2  3  8 13 18 23 24 19 14  9  4  5 10 15 20 25
             
     ```



4. 델타를 이용한 탐색

   - x축 방면의 진행방향과 y축 방면의 진행 방향을 각각 dx, dy로 하여 특정한 조건을 만나면 idx라는 변수를 사용하여 방향을 바꾸도록 설정했따. 그래서 위치 x,y를 조절할 수 있고 이를 이용하여 2차원 배열에서 원하는 위치의 요소에 접근할 수 있다.
   - 이 코드에서 +x, +y의 방향은 직교좌표계에서 +x, -y 방향이다.

   ```python
   # 달팽이 모양으로 출력
   
   def Inbox(lst, y, x, xmax, ymax):
       # 0 <= x < xmax, 0 <= y < ymax 일때 True 반환, IndexError를 방지할 수 있다.
       if x >= 0 and x < xmax and y >= 0 and y < ymax:
           if lst[y][x] == 0:
               return True
       return False
   
   result = [[0 for i in range(5)] for j in range(5)]
   
   dx = [1,0,-1,0] #우하좌상
   dy = [0,1,0,-1]
   idx = 0
   x,y=0,0
   
   for i in range(1, 26):
       result[y][x] = '{0:2d}'.format(i)
       if not Inbox(result, y+dy[idx], x+dx[idx], 5, 5):
           idx = (idx + 1)%4
       x, y = x + dx[idx], y + dy[idx]
       
   for _ in range(len(result)):
       print(*result[_])
       
   # 출력
    1  2  3  4  5
   16 17 18 19  6
   15 24 25 20  7
   14 23 22 21  8
   13 12 11 10  9
   ```




## 2차원 List(2)

- 전치행렬 - i,j 성분이 j,i성분으로 바뀐 행렬이다. 2차원 리스트로 구현하면 다음과 같다.

  a. 새로운 2차원 List에 할당하여 만드는 방법

  ```python
  #새로운 2차원 List에 할당
  
  A = [['{0:2d}'.format(i) for i in range(j, j+5)] for j in range(1, 26, 5)]
  
  for i in range(5):
      print(*A[i])
      
  transA = [[0 for i in range(5)] for j in range(5)]
  
  for i in range(5):
      for j in range(5):
          transA[j][i] = A[i][j]
          
  for _ in range(5):
      print(*transA[_])
      
  # 출력
   1  2  3  4  5
   6  7  8  9 10
  11 12 13 14 15
  16 17 18 19 20
  21 22 23 24 25 # A
   1  6 11 16 21
   2  7 12 17 22
   3  8 13 18 23
   4  9 14 19 24
   5 10 15 20 25 # transA
  ```



​	b. 기존 List에서 자리 재배치 하는 방법

```python
#기존 list에서 자리 재배치

A = [['{0:2d}'.format(i) for i in range(j, j+5)] for j in range(1, 26, 5)]

for i in range(5):
    print(*A[i])

for i in range(5):
    for j in range(5):
        A[i][j], A[j][i] = A[j][i], A[i][j]
        
for i in range(5):
    print(*A[i])
    
# 출력
 1  2  3  4  5
 6  7  8  9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25 # A
 1  6 11 16 21
 2  7 12 17 22
 3  8 13 18 23
 4  9 14 19 24
 5 10 15 20 25 # 변경 후 A
```



c. 내장함수 zip을 사용하는 방법

```python
# zip 함수 사용

A = [['{0:2d}'.format(i) for i in range(j, j+5)] for j in range(1, 26, 5)]

for i in range(5):
    print(*A[i])
    
transA = list(zip(*A))

for i in range(5):
    print(*transA[i])
    
# 출력
 1  2  3  4  5
 6  7  8  9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25 # A
 1  6 11 16 21
 2  7 12 17 22
 3  8 13 18 23
 4  9 14 19 24
 5 10 15 20 25 # transA
```

zip함수를 통해 A의 각 행이 언패킹되어 zip함수의 인자로 들어간다.

다시 zip함수에 의해 패킹된 요소는 튜플 형식으로 transA에 들어간다.



```python
# zip 함수 요소 형태

A = [['{0:2d}'.format(i) for i in range(j, j+5)] for j in range(1, 26, 5)]

for i in range(5):
    print(*A[i])
    
transA = list(zip(*A))

print(transA)
	print(type(transA[0]))
    
# python 예시 - zip 함수 요소 형태
      
    A = [['{0:2d}'.format(i) for i in range(j, j+5)] for j in range(1, 26, 5)]
      
    for i in range(5):
        print(*A[i])
          
    transA = list(zip(*A))
      
    print(transA)
      print(type(transA[0]))
      
# 출력
>>> [(' 1', ' 6', '11', '16', '21'), (' 2', ' 7', '12', '17', '22'), (' 3', ' 8', '13', '18', '23'), (' 4', ' 9', '14', '19', '24'), (' 5', '10', '15', '20', '25')]
    >>> <class 'tuple'>
```







출처: SW Expert Academy - Learn - Course - Programming Intermediate

[SW Expert Academy - Programming Intermediate course](https://swexpertacademy.com/main/learn/course/subjectList.do?courseId=AVuPDN86AAXw5UW6)