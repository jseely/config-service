# Config Service

A configuration service that is fault tolerant using ceph as a backend storage provider.

## Activating python environment

All management of this service is done through a python environment provided as part of this repository. You can either use the `init.sh` script to set up the virtual environment and install all the modules required or if you know your environment is already installed you can use the `reactivate.sh` script. For either of these options you need to `source <script>` the script instead of executing it.

Dependencies:
- python3-dev (`sudo apt-get install python3-dev`)
- virtualenv (`sudo apt-get install virtualenv`)
