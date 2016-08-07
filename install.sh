# Installing Virtualenv
pip install virtualenv

# Creating and Activating Virtualenv
virtualenv env
source env/bin/activate

# Installing Django pip requirements
pip install -r requirements.txt

# Installing Web Client
git clone git@github.com:cappuccino-app/cappuccino-web.git .

# Creating Static Files Directory for django
mkdir -p owndrive/static

# Collecting Static Files for serving Web Client Resources
python manage.py collectstatic

# Creating MySql database
mysql -u root -e "create database 'cappuccino'" -p