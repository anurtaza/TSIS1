def return_to_0(n):
        while n >= 0:
            yield n
            n -= 1

n = int(input())

for num in return_to_0(n):
      print(num)