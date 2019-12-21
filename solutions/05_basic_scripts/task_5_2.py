#!/usr/bin/env python

user_input1 = input('Введите IP адрес и маску в формате IP/prefix: ')

#Разделение IP адреса и Маски на две временные переменные по /
ip_address, mask = user_input1.split('/')

#Распаковка переменных ip адреса через разделитель точку
oct1, oct2, oct3, oct4 = ip_address.split('.')

#Операции по вычислению маски. Принцип вычисления: вычислить сумму 1 и 0 в маске
mask = int(mask)
host = 32 - mask
mask_bin = ('1' * mask) + ('0' * host)
#Распаковака переменных маски через срезы строки
octb1, octb2, octb3, octb4 = mask_bin[0:8],mask_bin[8:16],mask_bin[16:24],mask_bin[24:32]


#Формирование шаблонов для Network и для Mask с использованием классического способа
#форматирования format

network_template = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''

mask_template = '''
Mask:
/{4}
{0:<8} {1:<8} {2:<8} {3:<8}
{0:<08b} {1:<08b} {2:<08b} {3:<08b}
'''

print(network_template.format(int(oct1),int(oct2),int(oct3),int(oct4)))
print(mask_template.format(int(octb1,2),int(octb2,2),int(octb3,2),int(octb4,2),mask))


