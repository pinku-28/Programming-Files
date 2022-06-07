# given two integer numbers return their product
# only if the product is equal to or lower than 1000
# else return their sum

first_num = int(input("number1: "))
second_num = int(input("number2: "))

if first_num * second_num <= 1000:
    print(f'Result: {first_num * second_num}')
else:
    print(f'Result: {first_num + second_num}')
