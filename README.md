# opx-docs
Welcome to the OpenSwitch OPX project!

This OpenSwitch repository contains the manifest file for the repository tool used to pull down sources for the OpenSwitch OPX project. The OpenSwitch OPX project is the switch abstraction interface (SAI) host-adapter originally written by Dell, and contributed to the OpenSwitch project. It is assumed that you are familiar with Linux and have basic development knowledge.

## Read the documentation
See [OpenSwitch OPX documentation](https://github.com/open-switch/opx-docs/wiki) for complete information.

## Get OpenSwitch
There are two ways to get the image:
- **Download and install binaries** — see Installation below for complete information, **or**
- **Build from scratch** — see the step-by-step instructions below to build the project.

## Build environment recommendations
- Intel multi-core
- Ubuntu 16.04 or later (desktop edition with Python installed)
- 20G available free disk space

## The build environment

### Prerequisites
Updated environment: `sudo apt-get update`
- GIT: `sudo apt-get install git`
- Repo: `sudo apt-get install repo`
- apt-utils: `sudo apt-get install apt-utils` 
- Docker: `sudo apt-get install docker.io`  

## Clone the source code
To get the source files for the OpenSwitch OPX repositories, run the commands in an empty directory (root directory). For example: _~/dev/opx/_:

    repo init -u https://github.com/open-switch/opx-manifest.git
    repo sync
        
The `repo sync` command downloads all of the source files that you need to build OpenSwitch. In addition to the source files, you will also need some binary libraries for the SAI. The SAI is currently not open sourced entirely, as it is based on Broadcom's SDK and there is no open source SAI implementation from Broadcom at this time.

All build scripts are find in the `opx_build` repo and will be dowloaded as part of the above `repo sync`.

## Build the code
Setup your path to include _opx-build/scripts_ folder (if you plan to run this command often, you could optionally add it to the `.bashrc`):

    cd opx-build/scripts
    export PATH-=$PATH:$PWD
       
## OpenSwitch Docker environment
To setup your Docker OPX image, use the script in the _opx-build/scripts_ folder called `opx_setup`. This script builds a Docker container called `docker-opx` which will be used by the build scripts:

    cd opx-build/scripts/
    opx_setup
            
## Build one repository
Go to the root directory where you installed the OPX repositories and run the OPX Docker container:

    cd ~/dev/opx
    docker run --privileged -i -t -v ${PWD}:/mnt docker-opx:lastest
    
Setup the builder environment inside the Docker container:

    root@077f7b30f8ef:/# DIST=jessie git-pbuilder create

To build a single repository, go to the repository and build. For example, to build `opx_logging`:

    root@077f7b30f8ef:/# cd /mnt/opx-logging
    root@077f7b30f8ef:/mnt/opx-logging# git-buildpackage --git-dist=jessie  --git-ignore-branch --git-pbuilder    

## Build all repositories
Issue the `opx_build_all` command from the root directory to build all repos and create packages in the same root directory.

    opx_build_all
       
## Installation
Once all of the repositories have been built, you can install the created ONIE Debian x86_64 image. You can then install all of the build packages, along with other Debian files you downloaded earlier in the root directory.

See [Install OpenSwitch OPX on Dell S6000 Platform](https://github.com/open-switch/opx-docs/wiki/Install-OPX-on-Dell-S6000-ON-platform) for complete information.

(c) 2017 Dell
