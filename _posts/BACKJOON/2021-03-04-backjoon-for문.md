---
layout: post
title:  "[완료]for문"
date:   2021-03-04 19:16:00 +0900
categories: BACKJOON
---

### 2739 구구단
```python
N = int(input())

for i in range(1, 9+1):
    print(str(N) + ' * ' + str(i) + ' = ' + str(N*i))
```
### 10950 A+B-3
```python
N = int(input())
for i in range(1, N+1):
    A, B = map(int, input().split())
    print(A+B)
```

### 8393 합
```python
N = int(input())
sum = 0
for i in range(1, N+1):
    sum += i
print(sum)
```

### 15552 빠른 A+B
```python
import sys
 
inp = int(input())
for i in range(inp):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)
```

### 2741 N 찍기
```python
N = int(input())
for i in range(N):
    print(i+1)
```

### 2742 기찍 N
```python
N = int(input())
for i in range(N, 0, -1):
    print(i)
```

### 11021 A+B-7
```python
N = int(input())
for i in range(N):
    A, B = map(int, input().split())
    print("Case #"+str(i+1)+": "+str(A+B))
```

### 11022 A+B-8
```python
N = int(input())
for i in range(N):
    A, B = map(int, input().split())
    C = A+B
    print("Case #%s: %s + %s = %s"%(i+1, A, B, C))
```

### 2438 별 찍기 - 1
```python
N = int(input())
for i in range(1, N+1):
    print("*"*i)
```

### 2439 별 찍기 -2
```python
N = int(input())
for i in range(1, N+1):
    print(" "*(N-i)+"*"*i)
```

### 10871 X보다 작은 수
```python
N, X = map(int,input().split())
A = list(map(int,input().split()))
answer = ""
for i in range(N):
    if A[i] < X :
        answer = answer + str(A[i])+ " "
print(answer)
```