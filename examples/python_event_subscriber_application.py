#Python block code for CPS event subscriber application

import cps
import cps_utils

handle = cps.event_connect()

cps.event_register(handle, cps_api_object_key)

while True:
   ev = cps.event_wait(handle)

   if ev[‘key’] == ...:
       ...      elif ev['key'] == ...:
       ...
