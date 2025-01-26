def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    print(n ,"is Prime Number")    
    return True

n = 1
for n in range (1,50,+1):
   is_prime(n)
     