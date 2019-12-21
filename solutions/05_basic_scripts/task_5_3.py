#!/usr/bin/env python

#Запрос ввода от пользователя
interface_type = input('Введите режим работы интерфейса (access/trunk): ')
interface_number = input('Введите тип и номер интерфейса: ')
interface_vlan = input('Введите номер влан(ов): ')

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]


#Создание словаря где ключи соответствуют ввода от пользователя, для выбора
#темплейта обозначенного как значение ключа и являющегося переменной.
#темплейт должен быть создан до создания словаря
keys_dict = {'access' : access_template, 'trunk': trunk_template}




#Передача значений на стандартный поток вывода
print('\n' + '-' * 30)
print('interface {}'.format(interface_number))
#Ссылка на темплейт через значение словаря, в соотвествии с вводом от пользователя
print('\n'.join(keys_dict[interface_type]).format(interface_vlan))
