Olin College PowerChords
=======

The code behind olinpowerchords.com

## Installing Dependencies

### Required
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
sudo apt-get install git
sudo apt-get install python-pip3
sudo apt-get build-dep python-psycopg2
sudo pip3 install psycopg2
sudo pip3 install django-toolbelt

### Recommended
sudo pip3 install virtualenv
heroku plugins:install git://github.com/ddollar/heroku-accounts.git
