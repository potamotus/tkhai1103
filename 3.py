'python 3.9'
file = open('vacancy.csv',encoding = 'utf8')
ma = []
for st in file:
    ma.append(st.split(';'))
inp = input()
while inp != 'None':
    f = False
    for el in ma:
        if inp == el[-1]:
            print(f'В {el[-1][:-2]} найдена вакансия: {el[-2]}. З/п составит: {el[0]}')
            f = True
            break
    if not f:
        print('К сожалению, ничего не удалось найти')
    inp = input()
