def Factorization(number):
    num = number

    while num != 1:
        for i in range(2, num + 1, 1):
            if num % i == 0:
                print(i)
                num = int(num / i)
                break


num = int(input())
Factorization(num)
