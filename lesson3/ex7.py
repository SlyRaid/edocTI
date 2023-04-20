a = 1
b = 1

num = int(input())

print(a, b, end=' ')

for i in range(2,num):
    a, b = b, a + b
    print(b, end=' ')