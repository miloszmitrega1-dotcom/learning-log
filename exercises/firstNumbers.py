
N = int(input("Podaj liczbe: "))


for n in range(2, N+1):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
            print(n)
        