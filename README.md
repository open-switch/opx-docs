# Welcome to the OpenSwitch Base project
This OpenSwitch repo contains the manifest file for the repo tool used to pull down sources for the OpenSwitch Base project. The OpenSwitch Base project is the switch abstraction interface (SAI) host-adapter originally written by Dell, and contributed to the OpenSwitch project. It is assumed that you are familiar with Linux and have basic development knowledge.

## Read the documentation
See [OpenSwitch Base documentation](https://github.com/amybuck/opx-docs/wiki) for complete information.

## Get OpenSwitch NAS
There are two ways to get the OpenSwitch Base:
- **Download and install binaries** - see Installation below for complete information, **or**
- **Build from scratch** - see the step-by-step instructions below to build the project.

## Build environment recommendations
- Intel multi-core
- Ubuntu 16.04 or later (desktop edition with Python installed)
- 20G available free disk space
- bash (most shell commands refer to bash commands - we like csh as well)

## The build environment
Updated environment: `sudo apt-get update`
- GIT: `sudo apt-get install git`
- Repo: See http://source.android.com/source/downloading.html to install the `repo`.

        Make sure you have a bin/ directory in your home directory and that it is included in your path:
        $ mkdir ~/bin
        $ PATH=~/bin:$PATH
    
        Download the Repo tool and ensure that it is executable:
        $ curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
        $ chmod a+x ~/bin/repo
    
- apt-utils: `sudo apt-get install apt-utils` 
- See [Docker environment setup guide](https://docs.docker.com/engine/installation/linux/ubuntulinux/
    ) for complete information.
    
        sudo apt-get install docker.io
        sudo apt-get install docker-engine
        sudo service docker start    

- To avoid running Docker commands as root (with `sudo`):

        sudo groupadd docker ### The 'docker' group might already exist
        sudo gpasswd -a ${USER} docker ### Add your user id to the 'docker' group
        sudo service docker restart

- You may need to log out/in to activate the changes to groups
- Ensure that you have proper permissions to close the source file (ssh keys must be installed)

> **NOTE**: Setup your ssh keys with GitHub [Settings > keys](https://github.com/settings/keys) (we are using git over ssh).
    
## Clone the source code
To get the source files for the OpenSwitch Base, run the commands in an empty directory (root directory). For example: _~/dev/opensiwtch/_:

        repo init -u ssh://git@github.com/Azure/sonic-nas-manifest.git
        repo sync
        
## Build the code
Setup your path to include _base-build-tools/scripts_ folder (if you plan to run this command often, you could optionally add it to the `.bashrc`):

       cd base-build-tools/scripts
       export PATH-=$PATH:$PWD
       
## OpenSwitch Base Docker environment
To setup your Docker Base image, use the script in the _base-build-tools/scripts_ folder called `base_setup`. This script builds a Docker container called `docker-base` which will be used by the build scripts:

        cd base-build-tools/scripts/
        base_setup
        
## Test your environment
You can run `base_build` in the _base-logging_ directory (opx-logging repo):

        cd base-logging
        base_build -- clean binary
        
## Build one repository
See the corresponding README.md file associated with the repo for the specific build commands, along with package dependencies.

## Build all repositories
Issue the `base_build_all` command from the root directory to build all repos and create packages in the same root directory.

        base_build_all
        
## Installation
Once all of the repos have been built, you can install the created ONIE Debian x86_64 image. You can then install all of the build packages, along with other Debian files you downloaded earlier in the root directory.

See [Install OpenSwitch Base on Dell S6000 Platform](https://github.com/amybuck/opx-docs/wiki/Install-Base-on-Dell-S6000-ON-platform) for complete information.

(c) 2017 Dell
