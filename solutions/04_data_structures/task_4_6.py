ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

ospf_route_list = []
ospf_route_list = ospf_route.split()

ospf_route_template = '''
Protocol:		 	 {}
Prefix: 			 {}
AD/Metric: 			 {}
Next-hop: 			 {}
Last update: 		 {}
Outbound Interface:	 {}
'''


proto = str(ospf_route_list[0]).replace('O','OSPF')
prefix = ospf_route_list[1]
AD = str(ospf_route_list[2]).strip('[]')
next_hop = ospf_route_list[4].rstrip(',')
last_update = ospf_route_list[5].rstrip(',')
out_intf = ospf_route_list[6].strip()

print(ospf_route_template.format(proto,prefix,AD,next_hop,last_update,out_intf))

	
