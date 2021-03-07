N = int(input())
lists = []
for i in range(N):
    i = float(input())
    lists.append(i)

# 산술평균
aver = sum(lists)/N
print(round(aver,1))
# 중앙값
print(sorted(lists)[round(N/2,1)])
# 최빈 값
print(round(sorted(lists)[1],1))
#범위
print(round(max(lists)-min(lists),1))