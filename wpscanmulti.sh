#!/bin/bash

#
# Use WPScan to scan sites running Wordpress
# and Store the output somewhere
#

domains='domain1.com example2.com example.com'

# Where do you want output to go? Better without trailing slash
destination=~/

for n in $domains; do

    echo -e "\nScanning $n ... "
    ruby ~/scripts/wpscan/wpscan.rb  --url $n \
        --batch \
        --no-color > $destination/$n.wpscan.log

done
