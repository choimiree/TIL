# 문자열 패턴매칭(1) - Brute force

## 문자열(1)

- 패턴 매칭 - 브루트 포스

  - 문자열 내의 글자 하나하나를 일일이 비교하는 방법.
  - 시간복잡도: O(mn)

  ```python
  #문자열 패턴 매칭(1): 브루트 포스
  
  def ComparePattern(string, target):
      cnt = 0
      loc = 0
      for i in range(len(string) - len(target)+1):
          loc += 1
          for j in range(len(target)):
              cnt += 1
              if string[i+j] != target[j]:
                  break
          else:
              print('matched')
              print(f'{cnt} times')
              break
      else:
          print('not matched')
          print(f'{cnt} times')
          
  string = 'Contrary to popular belief, Lorem Ipsum# python 예시 - 문자열 패턴 매칭(1): 브루트 포스
      
      def ComparePattern(string, target):
          cnt = 0
          loc = 0
          for i in range(len(string) - len(target)+1):
              loc += 1
              for j in range(len(target)):
                  cnt += 1
                  if string[i+j] != target[j]:
                      break
              else:
                  print('matched')
                  print(f'{cnt} times')
                  break
          else:
              print('not matched')
              print(f'{cnt} times')
      
      
      string = 'Contrary to popular belief, Lorem Ipsum is not simply random text.'
      target1 = 'random' # 본문에 있는 문자열
      target2 = 'randm' # 본문에 없는 문자열
      
      ComparePattern(string, target1)
      ComparePattern(string, target2)
      
      
      # 출력
      >>> matched
      >>> 65 times
      >>> not matched
      >>> 71 times
  ```

  







출처: SW Expert Academy - Learn - Course - Programming Intermediate

[SW Expert Academy - Programming Intermediate course](https://swexpertacademy.com/main/learn/course/subjectList.do?courseId=AVuPDN86AAXw5UW6)

