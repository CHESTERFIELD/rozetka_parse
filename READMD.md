For start activate virtual env in new directory 
```
mkdir rozetka_items_crape 
python3 -m venv venv
cd rozetka_items_crape
```
Then copy project with 
```
git clone https://github.com/CHESTERFIELD/rozetka_parse.git
```
And extract requirements for it
```
pip install -r req.txt
```
After add new db in postgres and add new user for it 
```
create user diplom_user with password 'diplom_password';
alter role diplom_user set client_encoding to 'utf8';
alter role diplom_user set default_transaction_isolation to 'read committed';
alter role diplom_user set timezone to 'UTC';
create database django_db owner user_name; 
```
Don't forget migrate db after created new db in postgres and create superuser

If you will have any problems
```
sudo -u postgres psql postgres
```
For parse items use 
```
scrapy runspider spiders/rozetka_hrefs_spider.py -o items.json
```
