class student:
    pass
students =[]
f = open('students.csv')
name = f.readline().strip()
k= 0
for i in f:
    s = i.strip().split(',')
    students.append(student())
    students[k].fname = s[0]
    students[k].name = s[1]
    students[k].sname = s[2]
    students[k].clas = s[3]
    students[k].score = s[4]
    k += 1
for i in students:
    s = 0
    d = 0
    if i.score == 'None':
        for k in students:
            if k.clas == i.clas and k.score!='None':
                d +=1
                s += int(k.score)
        i.score == f'{s/d:.3f}'
f = open('studentis_n.csv','w')
print(name,file = f)
for i in students:
    print(i.fname,',',i.name,',',i.sname,',',i.clas,',',i.score)
f.close()