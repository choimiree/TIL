# 문자열 패턴매칭(2) - KMP

## 문자열(2)

- 패턴 매칭 - KMP

  - 문자열과 패턴을 비교할 때 이미 세어놓은 정보를 활용하는 방법.
    - 비교하고자 하는 문자열의 앞에서 세었을 때와 뒷부분에서 세었을 때 똑같은 부분의 개수를 저장한다.
  - 시간복잡도: O(n)

- 이미 세어놓은 정보 저장할 리스트(infolst) 만드는 알고리즘

  - 시작점을 start, 앞부분의 시작점에서 비교할 뒷 부분까지의 거리를 dist라고 하자.
    - start = 0, dist = 1, 문자열의 길이가 leng일 때 start + dist < leng
    - 앞,뒤 똑같은 부분의 **길이**를 세는 건 전적으로 **시작점(start)**과만 관련이 있다..
    - infolst에 저장된 값은 해당 지점까지 문자열을 끊었을 때 글자를 앞에서 셀 때와 뒤에서 셀 때 같은 글자의 개수이다. 즉, 앞 - 뒤가 똑같은 길이다.

  1. infolst[start] == infolst[start + dist]일 때:

     시작점(start)을 움직이며 거리가 dist일 때 중복되는 개수를 세어준다.

     - start: 앞에서 --> 방향으로 세어준다 // Start + dist: 뒤에서 --> 방향으로 세어준다.

     ![image-20200412234641893](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20200412234641893.png)

     

  2. 다를 때(즉, infolst[start] != infolst[start + dist] 일때)

     (1) **start가 0일 때**: dist만 늘려준다.

     - 중복되는 문자열을 찾기 시작하는 지점을 더 멀리 지정해준다.

     ![image-20200412234657073](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20200412234657073.png)

     - ex. ABCA

       dist = 1: AB	앞: A에서 탐색 시작// 뒤: B에서 탐색 시작

       dist = 2: A C 앞:A에서 탐색 시작// 뒤: C에서 탐색 시작

       dist = 3: A A  앞: A에서 탐색 시작// 뒤: A에서 탐색 시작(뒤의 A)

     (2) **start가 0이 아닐 때**: 뒤에서 비교하는 지점은 그대로 두고 start지점만 앞으로 당긴다.

     - start = infolst[start -1]

       (start에 infolst[start - 1]을 할당함으로써 [start-1]에 들어있는 값의 위치로 Start를 이동한다.

       ![image-20200412235721816](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20200412235721816.png)

     : **이동한 위치에서 비교해서 같으면** infolst[start + dist]에 infolst[start - 1]+1을 할당

     (infolst[start - 1]번째까지는 중복으로 세었다는 의미이므로 더해주는 것이다.)

     : **비교해서 다르면** 2-(2) 과정을 start가 0이 될 때까지 반복한다.

     --> start = 0일 때 비교한 게 같으면 1을 infolst[start + dist]에 할당

     --> 다르면 0을 할당

  ```python
  #KMP - infolst 만들기
  
  def infolst(string):
      if len(string) == 1: return [0]
      infolst = [0 for i in range(len(string))]
      start = 0
      dist = 1
      
      while start + dist < len(string):
          if string[start] == string[start + dist]:
              infolst[start + dist] = start + 1
              start += 1
          else:
              if start == 0:
                  dist += 1
              else:
                  dist += start - infolst[start - 1]
          # 현재 start + dist의 위치를 고정시키기 위함
          		start = infolst[start - 1]
              
      return infolst
  
  string = 'abcdabcdabcdabcdabcdabcef'
  target1 = 'abcdabcef' # 본문에 있는 문자열
  target2 = 'abcdabcf' # 본문에 없는 문자열
  print(Infolst(target1))
  print(Infolst(target2))
  
  # 출력
  >>> [0, 0, 0, 0, 1, 2, 3, 0, 0]
  >>> [0, 0, 0, 0, 1, 2, 3, 0]
  ```



- KMP 알고리즘 구현

  - 본문을 string, 찾을 문자열을 target이라고 하자.
  - 위에서 만들어둔 infolst 함수를 사용하여 target의 infolst를 구한다.
  - 본문 내에서 target을 찾아나가다가, 불일치하는 지점을 만나면 그 바로 전 인덱스에 해당하는 정보를 infolst에서 꺼내 활용한다.
    - target을 찾아 나갈 때마다 step을 센다. 불일치하는 지점을 만나면 step - infolst[step - 1]지점에서 다시 탐색을 시작한다.

  ```python
  # KMP 패턴 매칭 알고리즘 구현
  
  def KMP(string, target):
      idx = 0
      info = Infolst(target)
      cnt = 0
      while idx < len(string) - len(target) +1:
          step = 0
          for i in range(len(target)):
              cnt += 1
              if target[i] != string[idx + i]:
                  if step == 0:
                      idx += 1
                      break
                  else:
                      idx += step - info[step - 1]
                      break
              step += 1
          else:
              return f'matched, {cnt} times'
      return f'not matched, {cnt} times'
  
  string = 'abcdabcdabcdabcdabcdabcef'
  target1 = 'abcdabcef' # 본문에 있는 문자열
  target2 = 'abcdabcf' # 본문에 없는 문자열
  print(KMP(string, target1))
  print(KMP(string, target2))
  
  # 출력
  >>> matched, 41 times
  >>> not matched, 40 times
  ```



**전체코드**

```python
# 문자열 패턴 매칭(2) : KMP

def Infolst(string):
    if len(string) == 1: return[0]
    infolst = [0 for i in range(len(string))]
    start = 0
    dist = 1
    
    while start+dist < len(string):
        if string[start] == string[start+dist]:
            infolst[start+dist] = start+1
            start+=1
        else:
            if start == 0:
                disdt += 1
            else:
                dist += start - infolst[start - 1]
                #현재 start+dist의 위치를 고정시키기 위함
                start = infolst[start-1]
     return infolst

def KMP(string, target):
    idx = 0
    info = Infolst(target)
    cnt = 0
    while idx < len(string) - len(target) + 1:
        step = 0
        for i in range(len(target)):
            cnt += 1
            if target[i] != string[idx + i]:
                if step == 0:
                    idx += 1
                    break
                else:
                    idx += step - info[step - 1]
                    break
            step += 1
        else:
            return f'matched, {cnt} times'
    return f'not matched, {cnt} times'

string = 'abcdabcdabcdabcdabcdabcef'
target1 = 'abcdabcef' # 본문에 있는 문자열
target2 = 'abcdabcf' # 본문에 없는 문자열
print(Infolst(target1))
print(Infolst(target2))
print(KMP(string, target1))
print(KMP(string, target2))

# 출력
>>> [0, 0, 0, 0, 1, 2, 3, 0, 0]
>>> [0, 0, 0, 0, 1, 2, 3, 0]
>>> matched, 41 times
>>> not matched, 40 times
```



> Brute-force와 성능 비교 예시

```python
# 문자열 패턴 매칭: KMP 알고리즘과 Brute-force 비교

def Infolst(string):
    if len(string) == 1: return[0]
    infolst = [0 for i in range(len(string))]
    start = 0
    dist = 1
    
    while start + dist < len(string):
        if string[start] == string[start+dist]:
            infolst[start+dist] = start + 1
            start += 1
        else:
            if start == 0:
                dist += 1
            else:
                dist += start - infolst[start-1]
                #현재 start+dist의 위치를 고정시키기 위함
                start = infolst[start-1]
     return infolst

def KMP(string, target):
    idx = 0
    info = Infolst(target)
    cnt = 0
    while idx < len(string) - len(target) + 1:
        step = 0
        for i in range(len(target)):
            cnt += 1
            if target[i] != string[idx+i]:
                if step ==0:
                    idx += 1
                    break
                else:
                    idx += step - info[step - 1]
                    break
            step += 1
        else:
            return f'matched, {cnt} times'
     return f'not matched, {cnt} times'

def ComparePattern(string, target):
    cnt = 0
    loc = 0
    for i in range(len(string) - len(target) + 1):
        loc += 1
        for j in range(len(target)):
            cnt += 1
            if string[i+j] != target[j]:
                break
        else:
            print('matched', end=', ')
            print(f'{cnt} times')
            break
    else:
        print('not matched', end=', ')
        print(f'{cnt} times')
        
string1 = 'Contrary to popular belief, Lorem Ipsum is not simply random text.'
target1 = 'random' 
string2 = 'abcdabcdabcdabcdabcdabcef'
target2 = 'abcdabcef'

ComparePattern(string1, target1)
print(KMP(string1, target1))
print(f'infolst of target1: {Infolst(target1)}')
ComparePattern(string2, target2)
print(KMP(string2, target2))
print(f'infolst of target2: {Infolst(target2)}')

# 출력
>>> matched, 65 times
>>> matched, 64 times
>>> infolst of target1: [0, 0, 0, 0, 0, 0]
>>> matched, 53 times
>>> matched, 41 times
>>> infolst of target2: [0, 0, 0, 0, 1, 2, 3, 0, 0]   
            
```





출처: SW Expert Academy - Learn - Course - Programming Intermediate

[SW Expert Academy - Programming Intermediate course](https://swexpertacademy.com/main/learn/course/subjectList.do?courseId=AVuPDN86AAXw5UW6)