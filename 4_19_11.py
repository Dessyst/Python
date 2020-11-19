num = int(input())
sum = 0

while num > 1:
    if num > 1:

        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            sum = sum + num

    else:
        continue
    num = num - 1

print(sum)