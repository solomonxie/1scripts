## First Step
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install curl tree htop wget python-pip -y
sudo pip install virtualenv
```

## SSH Server
```
sudo apt-get install openssh-server
tree -a /home
```

## LAMP
```
sudo taskel
sudo apt-get install phpmyadmin
```

## LNMP
```
sudo apt-get install php5-fpm nginx mysql-server php5-mysql -y
sudo service nginx start
curl localhost
whereis nginx
```

## Wordpress
```
sudo wget https://wordpress.org/latest.zip
sudo wget https://cn.wordpress.org/wordpress-4.4.2-zh_CN.zip

mysql -u root -p
show databases;
create database 数据库名;
exit;
```

## Configure Nginx


## Shadowsocks Server
AWS EC2 Dashboard:
```
Security Groups -> Inbound -> Edit -> Add -> Custom TCP Rule, TCP, 8000 - 9000, 0.0.0.0/0
Security Groups -> Inbound -> Edit -> All traffic, All, All, 0.0.0.0/0
```

SSH 
```
sudo apt-get install python-pip python-m2crypto
sudo pip install shadowsocks
sudo nano /etc/shadowsocks.json
    配置文件
    {
        "local_address": "127.0.0.1",
        "local_port":1080,
        "server":"0.0.0.0",
        "port_password": {
            "8111":"123123",
            "8112":"123123"
        },
        "server_port":443,
        "password":"123123",
        "timeout":300,
        "method":"aes-256-cfb",
        "fast_open": false,
        "workers": 1
    }

sudo ssserver -c /etc/shadowsocks.json -d start

```

### Proxy Server
```
sudo apt-get install squid -y

sudo nano /etc/squid/squid.conf

  配置Port
      http_port 3128
      注：建议修改缺省Port
   权限控制
      acl localnet src 192.168.XXX.0/255.255.255.0
      把上面的XXX换成了自己内网想使用的网段
      添加
      http_access allow localnet

sudo /etc/init.d/squid3 start
或者
sudo service squid start
```

### FTP Server
```
sudo apt-get install vsftpd

```

