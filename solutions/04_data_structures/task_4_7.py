mac = 'AAAA:BBBB:CCCC'

mac_add = mac.split(':')
mac_bin_template = '{:08b}{:08b}{:08b}'

print(mac_bin_template.format(int(mac_add[0], 16),int(mac_add[1], 16),
int(mac_add[2],16)))


   
   
