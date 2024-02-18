import requests
import json
log = input('Введите свой логин: ')
passwd = input('Введите свой пароль: ')
params =  {
        'start': '2022-09-01T00:00:00+04:00',
        'end': '2026-05-30T00:00:00+04:00'}
headers = {
        'Referer': 'https://lk.samgtu.ru/distancelearning/distancelearning/index'}
payload = {'LoginForm[username]': log,'LoginForm[password]': passwd}
url_json = 'https://lk.samgtu.ru/api/common/distancelearning'
url_login = 'https://lk.samgtu.ru/site/login'
D = {'Предмет': '', 'Препод': '', 'Дата': ''}
with requests.Session() as s:
        s.post(url_login, data=payload)
        r = s.post(url_json, params=params, headers= headers)
        print(r.status_code)
        qwe = json.loads(r.text)
        list=[]
        for i in range(len(qwe)):
                D = {'Предмет': '', 'Препод': '', 'Тип': '', 'Дата': '', 'Время': ''}
                D['Предмет']=qwe[i]['title']
                D['Препод']=qwe[i]['description'].split('<br>')[1]
                try:
                        D['Тип']=qwe[i]['description'].split('strong')[3][1:-2]
                except IndexError:
                        D['Тип'] = ''
                D['Дата']=qwe[i]['start'].split('T')[0]
                D['Время']=qwe[i]['start'].split('T')[1] + ' - ' + qwe[i]['end'].split('T')[1]
                list.append(D)
start = input('Какой тип сортировки делать(По дате: 1, По предмету: 2, По преподавателю: 3)')
def pr1nt():
        print(list[i]['Предмет'] + '   ' + list[i]['Тип'] + '   ' + list[i]['Препод'] + '   ' + list[i]['Время'])

print(list[0]['Препод'])
if start == '1':
        date = input('Введите дату(нарпимер: 2024-02-17): ')
        type = input('Введите тип занятия: ')
        for i in range(len(list)):
                if date == list[i]['Дата']:
                        if type == list[i]['Тип'] or type == 'Все':
                                pr1nt()
if start == '2':
        pr = input('Введите предмет: ')
        for i in range(len(list)):
                if pr == list[i]['Предмет']:
                        pr1nt()
if start == '3':
        tea = input('Введите ФИО преподавателя: ')
        for i in range(len(list)):
                if tea == list[i]['Препод']:
                        pr1nt()
