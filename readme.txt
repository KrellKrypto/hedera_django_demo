Built from tutorial by bobbystearman at didcoding on youtube. Localized to US and branding changed.
https://www.youtube.com/watch?v=-QqnXXuft0U


Django project demo that uses Hedera Hashgraph HBAR to pay for goods. NOT PRODUCTION READY, Hbar account and product information is hardcoded

Note: You need to create a testnet acount with Hedera to follow this tutorial and ensure virtualenvwrapper is installed to manage the
python VE

vist: https://portal.hedera.com/register

save your Acc number to your environment varibles as OPERATOR_ID

save your privte key to your environmanet variables as OPERATOR_KEY

Ensure you have JDK Installed at least version 11

Add JAVA_HOME to you environment variables and ensure the path is to your version of JDK - mine is C:\Program Files\Java\jdk-16.0.1

Edit 'Path' in environment variables and add %JAVA_HOME%\bin\server

cd to development directory

mkvirtualenv

mkdir hedera_django_demo

clone repository to new directory

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

https://localhost:8000 - To view the webserver
