s=input("Enter the String:")
res=""
count=1
for i in range(len(s)):
    if(i+1 <len(s) and s[i]==s[i+1]):
        count=count+1
    else:
        res=res+s[i]
        res=res+str(count)
        count=1
print(res)