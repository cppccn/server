# Installing Virtualenv
echo -e "Installing virtualenv ..."
pip install virtualenv

# Creating and Activating Virtualenv
echo -e "Creating new Virtual Environment ..."
virtualenv env
source env/bin/activate

# Installing Django pip requirements
echo -e "Installing PIP requirements ..."
pip install -r requirements.txt

# Installing Web Client
echo -e
echo -e "Cloning Cappuccino-Web ..."
git clone git@github.com:cappuccino-app/cappuccino-web.git

# Creating Static Files Directory for django
echo -e "Creating Static Files Directory ..."
mkdir -p owndrive/static

# Collecting Static Files for serving Web Client Resources
echo -e "Collecting Static Files ..."
python manage.py collectstatic

# Creating MySql database
echo -e "Creating MySql Database ..."
mysql -u root -e "CREATE DATABASE IF NOT EXISTS cappuccino" -p

# Setting Password inside local_settings.py
echo -n "Enter the Password for MySql database, User Root [ENTER]: "
read passwd
sed -i "s/'PASSWORD': '',/'PASSWORD': '$passwd',/g" owndrive/local_settings.py

# Making Migrations
echo -e "Applying Migrations ..."
python manage.py migrate

# Creating Super User
echo -e "Creating Super User for Cappuccino-App ..."
python manage.py createsuperuser --username=admin_user --email=admin@cappuccino.com