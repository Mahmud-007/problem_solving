def sieve_prime(n):
    check= [True for i in range(n+1)]
    primes=[2]
    i=3
    while(i<=n):

        if(check[i]):
            j=i*i

            while(j<=n):
                check[j]=False
                j=j+i

        i=i+2
    
    p=3
    while(p<=n):
        if (check[p]):
            primes.append(p)
        p=p+2

    for i in primes:
        print(i)

def main():
    n = int(input("Enter N: "))
    sieve_prime(n)

if __name__ == "__main__":
    main()