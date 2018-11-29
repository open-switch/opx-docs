# Python code block to delete VLAN

import cps
import cps_object

#Create CPS object
cps_obj = \
    cps_object.CPSObject('dell-base-if-cmn/if/interfaces/interface')

#Populate the VLAN attributes VLAN_ID='br100'
VLAN_ID = 'br100'
cps_obj.add_attr('if/interfaces/interface/name', VLAN_ID)

#Associate a CPS set operation with the CPS object
cps_update = {'change': cps_obj.get(), 'operation': 'delete'}

#Add the CPS operation,obj pair to a new CPS transaction
transaction = cps.transaction([cps_update])

#Check for failure
if not transaction:
    raise RuntimeError('Error in deleting Vlan')
print 'successful'
