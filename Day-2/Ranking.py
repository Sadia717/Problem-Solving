def percentage(person):
    total=sum(person["marks"])
    return total/4

a=[
    {"name":"RAJU","age":23,"marks":[45,50,40,60]},
    {"name":"ROSE","age":12,"marks":[75,85,80,90]},
    {"name":"RAVI","age":52,"marks":[65,70,60,80]},
    {"name":"JACK","age":22,"marks":[55,75,65,70]}
]
b=sorted(a,key=percentage,reverse=True)
print(b)

l=["fIRST","SECOND","THIRD","FOURTH"]
pos=0
for i in b:
    print("{} has scored {} % -----> stands {}".format(i["name"],percentage(i),l[pos]))
    pos=pos+1
