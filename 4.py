fin = open('vacancy.csv', encoding = 'utf8')
dell = fin.readline()
a = [st.split(';') for st in fin]
a1 = []
a1.append(['Salary', 'Work_type', 'Company_Siz', 'Role', 'Company' ])
ds = {}
dc = {}
for el in a:
    ds[el[1]] = ds.get(el[1], 0) + int(el[0])
    dc[el[1]] = dc.get(el[1], 0) + 1
for el in a:
    a1.append([el[0], el[1], el[2], el[3], el[4], el[0]/ds[el[1]]*dc[el[1]]])
print(a1[1])