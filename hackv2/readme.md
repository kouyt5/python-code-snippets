# 钓鱼网站攻击

邮箱中总是遇到垃圾邮件，伪装成管理员让你输入密码。去网站上看了一下，数据上传比较简单，于是就想给他整点假数据，让他尝尝网络的险恶

基本思路如下:
+ 通过免费代理池获取代理（大小大概50个左右）https://github.com/jhao104/proxy_pool
+ 通过验证码识别库识别验证码 https://github.com/sml2h3/ddddocr
+ 构造学校邮箱后缀的伪数据请求接口

代理池docker封装:
```docker-compose.yml
version: '2'
services:
  proxy_pool:
    build: .
    container_name: proxy_pool
    ports:
      - "5010:5010"
    links:
      - proxy_redis
    environment:
      DB_CONN: "redis://@proxy_redis:6379/0"
  proxy_redis:
    image: "redis"
```
## 运行
1. 启动代理池(下载代码后 docker-compose up)
2. python main.py