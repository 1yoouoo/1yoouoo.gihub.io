nums = input()
nums = [int(n)  for n in nums]

ordered_nums = sorted(nums, reverse=True)

for n in ordered_nums : 
    print(n, end="")