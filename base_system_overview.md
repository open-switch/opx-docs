## OpenSwitch Base system overview
The OpenSwitch Base system is an innovative operating system for network systems. This information describes how it enables you to unleash new and creative ways to deploy, orchestrate, and manage your networking, servers, and storage solutions in your data centers and enterprise environments. 

OpenSwitch Base uses an unmodified Linux kernel and standard distribution to take advantage of rich ecosystem, and also provide flexibility in customizing your Base system according to your network needs.

This information describes how to obtain source code, build, install, and use the OpenSwitch system packages for hardware platforms (supports Dell S6000 only for release 1.0). Also provided are brief descriptions of the architecture, run-time environment, and code structure of the OpenSwitch project.

## Features

- Provides an abstraction of hardware devices of network switch platforms in a Linux OS environment
- Uses standard open source software including an ONIE installer, and an unmodified Linux kernel based on Debian Jessie distribution
- Provides a robust and flexible programmatic API - control plan services (CPS)
- Accesses OpenSwitch networking features using either the Linux standard API or the CPS
- Provides a rich set of networking features including full access to the NPU ACL and QoS functionality using the CPS

## Application programming
Provides an object-centric API for application development to implement custom applications using a well-defined object model, and set of programmatic APIs. The object model is defined using YANG modeling, and the APIs support Python and C/C++ programming languages. See [Application programming](https://github.com/amybuck/opx-docs/edit/master/application_programming.md) for more information.

## Hardware virtualization
The OpenSwitch software supports hardware virtualization (or simulation). Software simulation of basic hardware functionality is also provided (“white board”), and the higher layer software functionality can be developed and tested on generic PC/server hardware. See [Hardware virtualization](https://github.com/amybuck/opx-docs/edit/master/hardware_virtualization.md) for more information.

## Repositories
The repository structure is organized around the main architecture components:- NAS and SAI- PAS and SDI- Infrastructure

## Limitations
Only the Dell S6000-ON series is currently supported in this release, and other platforms may be supported in the future. OpenSwitch software uses an earlier version of the SAI specification. The OpenSwitch implementation will be compliant to the future SAI API v1.0 when available.
