#Python code block to remove MAC table entries from multiple VLANs

import cps_utils

#Define VLANs to remove MAC address entries from
vlan_list = [1, 2, 3, 4, 5]

#Create the CPS object
obj = cps_utils.CPSObject('base-mac/flush')

#Add the VLAN list to the CPS object
count = 0
el = ['input/filter', '0', 'vlan']

for vlan in vlan_list:
    obj.add_embed_attr(el, vlan)
    count = count + 1

el[1] = str(count)

#Associate the operation to the CPS object
tr_obj = ('rpc', obj.get())

#Create a transaction object
transaction = cps_utils.CPSTransaction([tr_obj])

#Check for failure
ret = transaction.commit()
if not ret:
    raise RuntimeError('Error   Flushing   entries   from   MAC   Table'
                       )
print 'Successfully removed'
