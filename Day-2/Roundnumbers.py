def roundnumbers(n):
    res=[]
    while(n!=1):
        if(n in res):
            return False
        res.append(n)
        n=sum(int(i)*int(i) for i in str(n))
    return True
print(roundnumbers(19))
print(roundnumbers(10))
print(roundnumbers(34))