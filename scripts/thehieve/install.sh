sudo add-apt-repository ppa:openjdk-r/ppa
sudo apt-get update
sudo apt-get install openjdk-8-jre-headless -y
sudo apt-get install unzip -y
cd /opt
sudo wget wget https://download.thehive-project.org/thehive-latest.zip
sudo unzip thehive-latest.zip
sudo ln -s thehive-3.3.0-1 thehive
