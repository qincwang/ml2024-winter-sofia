def get_index(n, numbers, input):
    for i in range(n):
        if numbers[i] == input:
            return i + 1
    return -1


n = int(input("please give a positive integer N: "))

numbers = []
for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

input = int(input("Enter an integer"))

res = get_index(n, numbers, input)

if res == -1:
    print(-1)
else:
    print(f"index of{input} is {res}")
