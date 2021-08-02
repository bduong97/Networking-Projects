# Description
This project will be for running various show commands and saving their outputs to file. Devices supported are currently only Cisco. You may need to install some packages with Pip3 if you are missing any.

# Usage
To use this script in your own environment, modify devices.txt and password.txt to fit your local environment. Make sure SSH is already pre enabled on your devices.
Note that the `devices.txt` and `password.txt` are symlinks pointing to their respective files in `Network_Automation`
Make sure there are no spaces after commas in devices.txt and password.txt

# Functionality
- Saves arp cache to file per device
- Saves running config to file per device

# Potential functionality
-Incorporate multithreading for increased performance



