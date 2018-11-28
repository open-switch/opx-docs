#!/usr/bin/python
# Python code to publish events

import cps
import cps_utils

# Create a handle to connect to the event service

handle = cps.event_connect()

# Create a CPS object

obj = cps_utils.CPSObject('base-port/interface', qual='observed',
                          data={'ifindex': 23})

# Publish the CPS object

cps.event_send(handle, obj.get())
