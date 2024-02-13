class student:
    pass
students =[]
n = int(input())
for i in range(n):
    students.append(student())
for i in range(n):
    inpt = int(input())
    students[i].fname = inpt
    students[i].name = inpt
    students[i].sname = inpt
    students[i].ball = inpt
    students[i].clas = inpt
    students[i].score = inpt
for i in range(n):
    if students[i].ball > mx:
        mx = students[i].ball
for i in range(n):
    if students[i].ball == mx and students[i].clas == 10:
        print (students[i].name, students[i].fname)

