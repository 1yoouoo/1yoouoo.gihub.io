---
layout: post
title:  "while문"
date:   2021-03-04 20:00:00 +0900
categories: BACKJOON
---

### 10952 A+B-5
```python
while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break

    print(A+B)
```
### 10951 A+B-4
```python
while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break
```
### 1110 더하기 사이클
```python
num = int(input())
check = num
new_num = 0
temp = 0
count = 0
while True:
    temp = num//10 + num%10
    new_num = (num%10)*10 + temp%10
    count += 1
    num = new_num
    if new_num == check:
        break
print(count)
```