sudo addgroup thehive
sudo adduser --system thehive
sudo cp /opt/thehive/package/thehive.service /usr/lib/systemd/system
sudo chown -R thehive:thehive /opt/thehive
sudo chgrp thehive /opt/thehive/conf/application.conf
sudo chmod 640 /opt/thehive/conf/application.conf
sudo systemctl enable thehive
sudo service thehive start
