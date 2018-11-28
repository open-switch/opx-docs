#!/usr/bin/python
# Python code to delete MAC address table entry

import cps_utils

# Register the attribute type to convert between string and byte-array format

cps_utils.add_attr_type('base-mac/table/mac-address', 'mac')

# Define the MAC address interface index, and VLAN to delete the static address entry

d = {'mac-address': '00:0a:0b:cc:0d:0e', 'ifindex': 18, 'vlan': '100'}

# Create a CPS object

obj = cps_utils.CPSObject('base-mac/table', data=d)

# Add the operation to the CPS object

tr_obj = ('delete', obj.get())

# Create a transaction object

transaction = cps_utils.CPSTransaction([tr_obj])

# Check for failure

ret = transaction.commit()
if not ret:
    raise RuntimeError('Error   deleting   entry   from   MAC   Table')

print 'Successfully deleted'
