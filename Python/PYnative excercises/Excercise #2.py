# write a program to iterate the first 10 numbers
# and in each iteration, print the sum of the current
# and previous number

previous = 0
current = 0
sum_num = 0

for i in range(10):
    print(f'c: {current} p: {previous} s: {sum_num}')
    current += 1
    previous = current - 1
    sum_num = current + previous
