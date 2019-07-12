#################### MYSQL ####################################
1) Install MYSQL

2) Create a DB named "users"

3) In "Users" DB, create a table named "users"
CREATE TABLE users(  
   name VARCHAR(100) NOT NULL,  
   address VARCHAR(100) NOT NULL,
   phoneNo VARCHAR(15)
)

4) Create a DB user named "manager". Set password of user: "manager": password:  "manager"

5) Grant db user "manager" all privileges to newly create db "users"
GRANT ALL PRIVILEGES ON * . * TO 'manager'@'localhost';

Above cmd will grant root privileges to user "manager"
#################### MYSQL ####################################

###################### STATIC HTML ############################

1) All files present in "html" directory should be kept in same directory and served by front-end/back-end web server.

###################### STATIC HTML ############################


############################### PYTHON APP ###############################

1) Install python 2.x.x.x

2) Use this link to install uWSGI server for serving python based app since it can't be served by web servers

	a) apt-get install build-essential python-dev

	b) pip install uwsgi


3) Deploy python app stored in app directory using:

cd app

uwsgi --http :9090 --wsgi-file userManagement

This will deploy the python app on port 9090 using http.

You can either connect this uWSGI server to front-end apache or you can install a backend apache/nginx that will act as a reverse proxy for python app.

############################### PYTHON APP ###############################


############################### BACKEND NGINX CONFIG ######################

1) Redirect all app requests to uWSGI server running on port 9090 which is serving put python app

location ~ /app {
                        proxy_pass http://127.0.0.1:9090;
                }
2) Implement SSL between front-end apache and backend Nginx. Communication between Nginx and uWSGI server (serving our python app) need not be secure since both are in same private subnet.

############################### BACKEND NGINX CONFIG ######################
