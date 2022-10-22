import os
os.system('rm -rf ./migrations')
os.system('mysql -u root -e "DROP DATABASE example";')
os.system('mysql -u root -e "CREATE DATABASE example";')
os.system('pipenv run init')
os.system('pipenv run migrate')
os.system('pipenv run upgrade')