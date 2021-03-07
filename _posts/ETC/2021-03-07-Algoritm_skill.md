---
layout: post
title:  "Algoritm_skill"
date:   2021-03-07 10:08:00 +0900
categories: Algoritm_skill
---

## list comprehension
--------------------

**기본**
```python
numbers = []
for n in range(1, 10+1):
    numbers.append(n)
```

**list comprehension**
```python
[x for x in range(10)]
```

2의 배수 표현
```python
[2*x for x in range(1, 10+1)]
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

**조건 걸기**
> 짝수만 담기
```python
[x for x in range(1, 10+1) if x % 2 == 0]
[2, 4, 6, 8, 10]
```

**중복 표현**

**for**
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
**if**
```python
>>> [ x for x in range(10) if x < 5 if x % 2 == 0 ]
[0, 2, 4]
```



## 카운터 정렬
--------------------
**과정**

1. 계수를 담아 둘 리스트 C를 만든다.
2. 리스트 C를 누적값으로 바꾼다.
3. C를 인덱싱해서 B에 저장한다.

**제한사항**

* 정수나 정수로 표현할 수 있는 자료에 대해서만 적용이 가능하다.
* 각 항목의 발생 횟수를 기록하기 위해, 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문이다.
* 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 **가장 큰 정수를 알아야 한다.**

```python
N = int(input())
A = []
for x in range(N):
    x = int(input())
    A.append(x)

def couting_sort(A, k):
    B = [0] * len(A)
    C = [0] * (k+1)

    for i in range(len(A)): # 각 element가 몇개있는지 C에 저장한다
        C[A[i]] += 1
    
    for i in range(1,len(C)): # C를 누적값으로 바꾼다
        C[i] += C[i-1]

    for i in range(len(A)): # C를 indexing해서 B에 저장한다
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

    return B
        
count = couting_sort(A, max(A))

for i in count:
    print(i)
```

**Counting Sort의 시간 복잡도**

Counting Sort의 시간 복잡도는 O(n+k)다.
이때 n은 정렬할 리스트의 길이이고, k는 리스트의 정수 최댓값을 의미한다.

데이터 개수가 n일 때 시간 복잡도는 O(n)이다. 정렬된 배열을 담을 B를 만들 때도 O(n)이다. =>(A의 요소를 역순으로 훑기 때문)

또한 C의 크기가 충분히 작을 때는 O(n)의 복잡도를 가지겠지만, k가 커질 경우 O(n+k)의 복잡도를 가진다. (즉 최댓값이 클수록 시간 복잡도가 커짐)


## 딕셔너리
--------------------
key, value 뒤집기

## range 응용
--------------------
## 각 자리 수의 합
--------------------
