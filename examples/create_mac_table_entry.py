#Configure MAC address table entry

import cps_utils

#Register the attribute type
cps_utils.add_attr_type('base-mac/table/mac-address', 'mac')

#Define the MAC address, interface index and VLAN attributes
d = {'mac-address': '00:0a:0b:cc:0d:0e', 'ifindex': 18, 'vlan': '100'}

#Create a CPS object
obj = cps_utils.CPSObject('base-mac/table', data=d)

#Associate the operation to the CPS object
tr_obj = ('create', obj.get())

#Create a transaction object
transaction = cps_utils.CPSTransaction([tr_obj])

#Check for failure
ret = transaction.commit()
if not ret:
    raise RuntimeError('Error   creating   MAC   Table   Entry') 
print 'Successfully created'
