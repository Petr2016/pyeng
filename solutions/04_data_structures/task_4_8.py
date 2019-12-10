ip = '192.168.3.1'

ip_template = '''
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
'''

ip_new = ip.split('.')

print(ip_template.format(int(ip_new[0]),int(ip_new[1]),
		int(ip_new[2]),int(ip_new[3])))
		
