N = int(input())
lists = sorted(list(str(N)))
print(lists)

for i in range(len(lists)):
    print(lists[-i-1],end='')