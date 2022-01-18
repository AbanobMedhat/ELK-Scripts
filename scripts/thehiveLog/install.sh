#!/bin/bash
sudo mkdir /var/log/thehive
cd /var/log
chown thehive:thehive thehive
sudo service thehive restart
