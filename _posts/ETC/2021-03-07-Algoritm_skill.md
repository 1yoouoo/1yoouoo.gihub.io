---
layout: post
title:  "Algoritm_skill"
date:   2021-03-07 10:08:00 +0900
categories: Algoritm_skill
---

## 리스트 컨프리헨션
--------------------
### 리스트 생성하기
** 기본 **
```python
numbers = []
for n in range(1, 10+1):
    numbers.append(n)
```

** 리스트 컨프리헨션 **
```python
[x for x in range(10)]
```

2의 배수 표현
```python
[2*x for x in range(1, 10+1)]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

** 조건 걸기 **
짝수만 담기
```python
[x for x in range(1, 10+1) if x % 2 == 0]
[2, 4, 6, 8, 10]
```

** 중복 표현 **
** for **
```python
[ (x, y) for x in ['강아지', '고양이', '이지윤'] for y in ['사료', '츄르', '커피']]
[('강아지', '사료'),
 ('강아지', '츄르'),
 ('강아지', '커피'),
 ('고양이', '사료'),
 ('고양이', '츄르'),
 ('고양이', '커피'),
 ('이지윤', '사료'),
 ('이지윤', '츄르'),
 ('이지윤', '커피')]
 ```
** if **
```python
>>> [ x for x in range(10) if x < 5 if x % 2 == 0 ]
[0, 2, 4]
```



카운터

딕셔너리 key,value 뒤집기

range 응용

각 자리 수의 합
