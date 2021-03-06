N = int(input())
lists = []
for _ in range(N):
    A = int(input())
    lists.append(A)
lists = sorted(lists)
for i in lists:
    print(i)