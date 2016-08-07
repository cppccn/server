# Installing Virtualenv
pip install virtualenv

# Creating and Activating Virtualenv
virtualenv env
source env/bin/activate

# Installing Django pip requirements
pip install -r requirements.txt

# Installing Web Client
git clone git@github.com:cappuccino-app/cappuccino-web.git .

# Collecting Static Files for serving Web Client Resources
python manage.py collectstatic

# Creating Static Files Directory for django
mkdir -p owndrive/static

# Creating MySql database
mysql -uroot -e "create database 'cappuccino'"