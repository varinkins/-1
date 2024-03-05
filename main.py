class student:
    pass
mx = 0
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
a = []
for i in range(n):
    if students[i].ball == mx and students[i].clas == 10:
        a.add(i)
print('1 место:',students[0].name, students[0].fname)
print('2 место:',students[1].name, students[1].fname)
print('3 место:',students[2].name, students[2].fname)
