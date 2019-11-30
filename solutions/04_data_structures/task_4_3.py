config = 'switchport trunk allowed vlan 1,3,10,20,30,100'

confg1 = config.split()
vlans = config1[-1].split(',')
print(vlans)
type(vlans)
