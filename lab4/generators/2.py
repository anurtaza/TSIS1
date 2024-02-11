def even_separate(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

n = int(input())

print(*even_separate(n), sep = ', ')
