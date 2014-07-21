Olin College PowerChords
=======

The code behind olinpowerchords.com

## Installing Dependencies

First run:
```bash
sudo apt-get update
```

### Required
```bash
sudo apt-get install python-pip3
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
sudo apt-get install git / brew install git
sudo apt-get build-dep python-psycopg2 / brew install postgresql
sudo pip3 install psycopg2
sudo pip3 install django-toolbelt
```

### Recommended
```bash
sudo pip3 install virtualenv
heroku plugins:install git://github.com/ddollar/heroku-accounts.git
```
