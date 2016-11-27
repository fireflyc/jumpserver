sudo cp -f /vagrant/sources.list /etc/apt/sources.list
sudo apt-get -y update
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password 123'
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password 123'
sudo apt-get -y install git python-pip gcc automake autoconf sshpass libmysqld-dev python-all-dev lrzsz libreadline-dev
sudo apt-get -y update
sudo apt-get -y install mysql-server
sed -i "s/^bind-address/#bind-address/" /etc/mysql/my.cnf
#mysql -u root -p123 -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'root' WITH GRANT OPTION; FLUSH PRIVILEGES; SET GLOBAL max_connect_errors=10000;"
sudo /etc/init.d/mysql restart
mysql -u root -p123 -e "CREATE DATABASE jumpserver default charset utf8 "
mysql -u root -p123 -e "CREATE USER 'jumpserver'@'%' IDENTIFIED BY '123'"
mysql -u root -p123 -e "GRANT ALL ON jumpserver.* TO 'jumpserver'@'%'"

which iptables && iptables -F
which setenforce && setenforce 0

sudo pip install -r /jumpserver/install/requirements.txt -i http://mirrors.aliyun.com/pypi/simple/

python /jumpserver/manage.py syncdb --noinput

python /jumpserver/vagrant/bootstrap.py