class student:
    pass
students =[]
f = open('students.csv')
name = f.readline()
ball = [0] * 12
k= 0
for i in f:
    s = i.strip().split()
    students.append(student())
    inpt = int(input())
    students[k].fname = inpt
    students[k].name = inpt
    students[k].sname = inpt
    students[k].clas = inpt
    students[k].score = inpt
    k += 1
for i in students:
    s = 0
    d= 0
    if i.score == 'None':
        for k in students:
            if k.clas == i.clas and k.score!='None':
                d +=1
                s += int(k.score)
        i.score == f'{s/d:.3f}'
f = open('studentis_n.csv','w')
for i in studentis_n:
