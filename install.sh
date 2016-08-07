# Installing Virtualenv
pip install virtualenv

# Creating and Activating Virtualenv
virtualenv env
source env/bin/activate

# Installing Django pip requirements
pip install -r requirements.txt

# Installing Web Client
git clone git@github.com:cappuccino-app/cappuccino-web.git .

mkdir -p owndrive/static