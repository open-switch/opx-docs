# Python code block to delete IP address

import cps_utils

# Populate attributes for the CPS object

idx = 16
ip_addr = '10.0.0.1'
pfix_len = 16
ip_attributes = {'base-ip/ipv4/ifindex': idx, 'ip': ip_addr,
                 'prefix-length': pfix_len}

# Create CPS object

cps_utils.add_attr_type('base-ip/ipv4/address/ip', 'ipv4')
cps_obj = cps_utils.CPSObject('base-ip/ipv4/address',
                              data=ip_attributes)

# Create CPS transaction to delete the CPS object

cps_update = ('delete', cps_obj.get())
transaction = cps_utils.CPSTransaction([cps_update])

# Commit the transaction

ret = transaction.commit()

# Check for failure

if not ret:
    raise RuntimeError('Error   ')

print 'Successfully deleted'
