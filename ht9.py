# 1
# n = int(input('n = '))
# sum = 0
# while n > 0:
#     sum += n % 10
#     n = n // 10
# print(sum)

# 2
# n = int(input('n = '))
# i = 1
# sum = 0
# while i <= n:
#     if n % i == 0:
#         sum += i
#     i += 2
# print(sum)


# 3
# n = int(input('n = '))
# sum = 0
# while n > 0:
#     sum += (n % 10)**2
#     n = n // 10
# print(sum)


# 4
# start, end = input().split(' ')
# start = int(start)
# end = int(end)
# sum = 0
# while start < end:
#     if (start % 4 == 0 and start % 100 != 0) or (start % 400 == 0):
#         sum += 366
#     else:
#         sum += 365
#     start += 1
# print(sum)


# 5
# n = int(input('n = '))
# a = 0
# c = 0
# while n > 0:
#     if n % 10 == 7:
#         a += 1
#     else:
#         c += 1
#     n = n // 10
# if a >= c:
#     print('YES')
# else:
#     print('NO')


# 6
# n = int(input('n = '))
# i = 0
# while n > 0:
#     if i < (n % 10):
#         i = n % 10
#     n = n // 10
# print(i)
