#Documentation
http://www.somacon.com/p572.php
https://gist.github.com/aderowbotham/2889048
http://rogueleaderr.com/post/65157477648/the-idiomatic-guide-to-deploying-django-in#note_server_balance
http://www.holovaty.com/writing/aws-notes/
http://www.rackspace.com/knowledge_center/article/mysql-connect-to-your-database-remotely

#Heroku
https://devcenter.heroku.com/articles/getting-started-with-django

#set up mysql on ami instance
sudo yum install mysql
sudo mkdir /var/lib/mysql
sudo yum install mysql-server
sudo /etc/init.d/mysqld start
sudo yum install mysql-devel #MySQL-Python needs this

#set password for root user of mysql
/usr/bin/mysqladmin -u root password 'test'

#Security
DELETE FROM mysql.user WHERE user = ; #prevents login without username, generally without this you can log in w/o user and show up as user=ec2-user

#DON'T forget to open port 3306 in AWS console
GRANT ALL ON test2.* TO root@'67.170.202.3' IDENTIFIED BY ''; #allow yourself to hit from chosen ip. Can also do root@'%' to allow all ips.
mysql -u root -h ec2-54-152-43-137.compute-1.amazonaws.com #test to make sure you can connect


#MySQL notes
CREATE DATABASE test2 CHARACTER SET utf8;
CREATE USER 'joeben'@'localhost' IDENTIFIED BY 'joeben';
GRANT ALL ON test2.* TO joeben@'localhost' IDENTIFIED BY 'joeben';
GRANT ALL ON test2.* TO joeben@'67.170.202.3' IDENTIFIED BY 'joeben';
OR GRANT ALL ON test2.* TO joeben@'%' IDENTIFIED BY 'joeben';
flush privileges;
CREATE TABLE `test_table`(id int auto_increment primary key,`name` varchar(25),`score` int(11));
Insert into test_table values(`id`,'Ben',10),(`id`,'Molly',20);


#To get app running on AMI instance...if the app is running somewhere else you can still hit the database on this server because the mysql-server is running, just not mysql-client. Need to get that installed.
#MySQL-Python requires the following:
sudo yum install mysql
sudo yum install mysql-devel

#Heroku
sudo wget -c https://toolbelt.herokuapp.com/install.sh
echo 'PATH="/usr/local/heroku/bin:$PATH"' >> ~/.bash_profile
sh install.sh
sudo yum install git

#required to get foreman running
sudo gem install foreman
sudo yum -y install gcc ruby-devel rubygems
gem install io-console

#Python requirements:
Django==1.6
MySQL-python==1.2.5 #you may have to install gcc with `sudo yum install gcc`

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Start up django app so that it can accessed from a browser
python mysite/manage.py runserver 0.0.0.0:8000
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
