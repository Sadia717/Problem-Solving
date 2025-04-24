students={ 4: {"name": "Neha","cgpa":"8.6","dept":"CSE","gen":"Female"},
          5: {"name": "Aarushi","cgpa":"8.5","dept":"CAI","gen":"Female"},
          6: {"name": "Rahin","cgpa":"9.5","dept":"CSD","gen":"Female"},
          7: {"name": "Ashick","cgpa":"8.6","dept":"CSE","gen":"Male"},
          8: {"name": "Shasitha","cgpa":"8.0","dept":"IT","gen":"Female"},
}
print("-"*38)
print("{:<5}{:<12}{:<7}{:<7}".format("ID","NAME","CGPA","DEPT","GENDER"))

print("-"*38)
for id,info in students.items():
    print("{:<5}{:<12}{:<7}{:<7}".format((id),info["name"],info["cgpa"],info["dept"],info["gen"]))
