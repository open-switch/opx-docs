#!/usr/bin/python
# Python code to register for events

import cps

# Create a handle to connect to the event service

handle = cps.event_connect()

# Register a key with the event service to receive notification when an event is published

cps.event_register(handle, cps.key_from_name('observed',
                   'base-port/interface'))
while True:
    obj = cps.event_wait(handle)
    print obj
