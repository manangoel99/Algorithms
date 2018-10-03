n = int(input("Enter Number upto which you need Prime Numbers"))

sieve = [ True for i in range(1, n+1) ]

for i in range(2, n):
    for j in range(2 * i, n, i):
        sieve[j] = False

for i in range(len(sieve)):
    if sieve[i] is True:
        print(i)


