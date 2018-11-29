#!/usr/bin/python
# Python code to create ACL entry to drop all packets received on specific port from specific source MAC address

# Import the CPS library
import cps_utils
import nas_os_utils

# Define the enum name to number map
e_stg = {'INGRESS': 1, 'EGRESS': 2}
e_ftype = {'SRC_MAC': 3, 'DST_MAC': 4, 'SRC_IP': 5, 'DST_IP': 6, 'IN_PORT': 9, 'DSCP': 21}
e_atype = {'PACKET_ACTION': 3, 'SET_TC': 10}
e_ptype = {'DROP': 1}

# Register the attribute type with the CPS utility for non-integer values
type_map = {
    'base-acl/entry/SRC_MAC_VALUE/addr': 'mac',
    'base-acl/entry/SRC_MAC_VALUE/mask': 'mac',
}
for key,val in type_map.items():
    cps_utils.cps_attr_types_map.add_type(key, val)

# Create the CPS object and populate the attributes
cps_obj = cps_utils.CPSObject(module='base-acl/table')

# Set the stage and priority
cps_obj.add_attr('stage', e_stg['INGRESS'])
cps_obj.add_attr('priority', 99)

# Populate the leaf-list attribute
cps_obj.add_list ('allowed-match-fields', [e_ftype['SRC_MAC'], e_ftype['DST_IP'], e_ftype['DSCP'], e_ftype['IN_PORT']])

# Define the CPS object
cps_update = ('create', cps_obj.get())

# Define an add operation and object pair to the CPS transaction
cps_trans = cps_utils.CPSTransaction([cps_update])

# Verify return value
ret = cps_trans.commit()
if not ret:
    raise RuntimeError ("Error creating ACL Table")
ret = cps_utils.CPSObject (module='base-acl/table', obj=r[0]['change'])
    
# Retrieve the CPS objectID from the ACL table
cps_get_val = cps_utils.CPSObject (module='base-acl/table', obj=r[0]['change'])
tbl_id = ret.get_attr_data ('id')
print "Successfully created ACL Table " + str(tbl_id)
