class student:
    pass
students =[]
n = int(input())
for i in range(n):
    students.append(student())
for i in range(n):
    inpt = int(input())
    students[i].fname = inpt[0]
    students[i].name = inpt[1]
    students[i].sname = inpt[2]
    students[i].ball = inpt[3]
    students[i].clas = inpt[4]


