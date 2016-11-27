sudo yum -y install git python-pip mysql-devel rpm-build gcc automake autoconf python-devel vim sshpass lrzsz readline-devel
sudo yum -y install mariadb-server mariadb-devel
sudo systemctl enable mariadb.service
sudo systemctl start mariadb.service

mysql -u root -e "CREATE DATABASE jumpserver default charset utf8 "
mysql -u root -e "GRANT ALL ON jumpserver.* TO 'jumpserver'@'*' IDENTIFIED BY '123'"
sudo systemctl restart mysqld

#disable firewall
systemctl status firewalld 2> /dev/null 1> /dev/null
systemctl stop firewalld
systemctl disable firewalld
which setenforce 2> /dev/null 1> /dev/null && setenforce 0

sudo pip install -r /jumpserver/install/requirements.txt -i http://mirrors.aliyun.com/pypi/simple/
python /jumpserver/manage.py syncdb --noinput
python /jumpserver/vagrant/bootstrap.py