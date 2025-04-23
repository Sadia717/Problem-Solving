def prime(n, i =2):
    if n== 1:
        return
    if n % i == 0:
        print(i, end=' ')
        prime(n//i, i)
    else:
        prime(n, i+1)
n=int(input("Enter any number:"))
print(prime(n))
#Another solution
'''def prime(n,a):
    if(n==1):
        return
    i=2
    while(n%i !=0):'''