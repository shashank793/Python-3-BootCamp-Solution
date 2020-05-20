# def ran_check(num,low,high):
#     if num in range(low,high):
#         return True
#     else:
#         False
#
# print(ran_check(int(input()),int(input()),int(input())))

num = int(input())
low = int(input())
high = int(input())

x = lambda num,low,high : True if num in range(low,high) else False

print(x(num,low,high))

