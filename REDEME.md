# 项目介绍

### 部署

+ 使用nginx部署静态页面

```bash
    # 修改配置
    vi /etc/nginx/nginx.conf
```

```bash
server {
        # 系统web界面
        listen 8080;
        server_name  _;
        root  /home/py_project/ScuBor1.0/www/RobotWang;
        index index-2.html;
        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;
        location / {
        }
        error_page 404 /404.html;
            location = /40x.html {
        }
        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    }
    
server {
        # 管理员页面 
        listen 8081;
        server_name  manage;
        root  /home/py_project/Scubot1.0/www/manager;
        index index.html;
        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;
        location / {
        }
        error_page 404 /404.html;
            location = /40x.html {
        }
        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    }
```

启动nginx
```bash
systemctl restart nginx
```


+ 部署falsk

```sybase
cd /home/py_project/ScuBot1.0
ls
```

在项目目录里面新建 `myproject.ini`

```ini
[uwsgi]

socket=127.0.0.1:5000

# Point to the main directory of the Web Site
chdir=/home/py_project/ScuBot1.0/

# Python startup file
wsgi-file=app.py

# The application variable of Python Flask Core Oject
callable=app

# The maximum numbers of Processes
processes=1

# The maximum numbers of Threads
threads=2
```
```sybase
nohup uwsgi myproject.ini &
```

