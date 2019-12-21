#!/usr/bin/env python


london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}

key1 = input('Введите номер устройства: ')

#После ввода номера устройства формируем перечен его параметров в текстовую строку
dev_params = ','.join(list(london_co[key1].keys()))

#Выводим на стандартный поток вывода запрос параметров устройства с подсказкой
key2 = input('Введите имя параметра: (' + dev_params + '): ')

print(london_co[key1][key2])

