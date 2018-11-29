# Python code block to create ACL table entry

# Import the CPS utility library
import   cps_utils
import   nas_os_utils

# Define the enum map
e_stg = {'INGRESS': 1, 'EGRESS': 2}
e_ftype = {'SRC_MAC': 3, 'DST_MAC': 4, 'SRC_IP': 5, 'DST_IP': 6, 'IN_PORT': 9, 'DSCP': 21}
e_atype = {'PACKET_ACTION': 3, 'SET_TC': 10}
e_ptype = {'DROP': 1}

# Register the attribute type with the CPS utiity
type_map = {
    'base-acl/entry/SRC_MAC_VALUE/addr': 'mac',
    'base-acl/entry/SRC_MAC_VALUE/mask': 'mac',
}
for key,val in type_map.items():
    cps_utils.cps_attr_types_map.add_type(key, val)

# Create the CPS object based on the dell-base-acl.yang model, then define the leaf attributes
cps_obj = cps_utils.CPSObject(module='base-acl/table')
cps_obj.add_attr('stage', e_stg['INGRESS'])
cps_obj.add_attr('priority', 99)

# Define the filters that the packets are matched to
# Filter 1 - match packets with specific source MAC address
cps_obj.add_embed_attr (['match','0','type'], e_ftype['SRC_MAC'])
cps_obj.add_embed_attr (['match','0','SRC_MAC_VALUE','addr'], '50:10:6e:00:00:00', 2)

# Filter 2 - match packets received on a specific port
cps_obj.add_embed_attr (['match','1','type'], e_ftype['IN_PORT'])
cps_obj.add_embed_attr (['match','1','IN_PORT_VALUE'], nas_os_utils.if_nametoindex('e101-001-0'))

# Define actions to apply on matched packets
cps_obj.add_embed_attr (['action','0','type'], e_atype['PACKET_ACTION'])
cps_obj.add_embed_attr (['action','0','PACKET_ACTION_VALUE'], e_ptype['DROP'])

# Associate the CPS object
cps_update = ('create', cps_obj.get())

# Add the CPS operation and object pair to a new transaction
cps_trans = cps_utils.CPSTransaction([cps_update])

# Verify the return value
ret = cps_trans.commit()
if not ret:
    raise RuntimeError ("Error creating MAC ACL Entry")

# Retrieve CPS objectID from ACL table
cps_get_val = cps_utils.CPSObject (module='base-acl/entry', obj=r[0]['change'])
mac_eid = cps_get_val.get_attr_data ('id')
print "Successfully created MAC ACL Entry " + str(mac_eid)
