nat = 'ip nat inside source list ACL interface FastEthernet0/1 overload'

nat_new_string = nat.replace('Fast', 'Gigabit')
print(nat_new_string)

