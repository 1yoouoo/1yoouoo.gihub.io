A = str(input())
word = []
for i in range(len(A)):
    word.append(A[i])


def groub_checker(word):
    k = 1
    start = 1
    end = len(word) - 1
    for i in range(end):
        while start < end:
            if word[i] == word[start]:
                if (start - i) == k: #연속되면
                    start += 1
                    k += 1
                else:               #연속되지않으면
                    break
            else: # word[i] != word[start]:
                start += 1

print(groub_checker(word))