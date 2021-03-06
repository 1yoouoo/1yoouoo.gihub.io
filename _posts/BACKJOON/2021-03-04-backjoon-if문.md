---
layout: post
title:  "[완료]if문"
date:   2021-03-04 19:08:00 +0900
categories: BACKJOON
---

### 1330 두 수 비교하기 
```python
a, b = map(int,input().split())

if a > b :
    print(">")
elif a < b :
    print("<")
else :
    print("==")
```

### 9498 시험 성적
```python
num = int(input())

if 90 <= num <= 100:
    print("A")
elif 80 <= num < 90:
    print("B")
elif 70 <= num < 80:
    print("C")
elif 60 <= num < 70:
    print("D")
else:
    print("F")
```

### 2753 윤년
```python
year = int(input())

if (year%4 == 0 and year%100 != 0) or year%400 == 0 : 
    print("1")
else :
    print("0")
```

### 14681 사분면 고르기
```python
X = int(input())
Y = int(input())
if X > 0 and Y > 0 :
    print(1)
elif X < 0 and Y > 0 :
    print(2)
elif X < 0 and Y < 0 :
    print(3)
else :
    print(4)
```

### 2884 알람시계
```python
hour,minute = map(int, input().split())

if minute > 44:
    print(hour, minute-45)
elif minute <= 44 and hour >= 1:
    print(hour-1, minute+15)
else:
    print(23, minute+15)
```
