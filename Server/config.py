# ---------Server相关配置--------

SERVER_IP = '127.0.0.1'         # Server IP
SERVER_PORT = 8090              # Server 端口(port)


# ---------Database相关配置------
DB_HOST = '127.0.0.1'           # Database连接地址
DB_USER = 'root'                # Database登录用户名
DB_PASS = '123456'              # Database登录密码
DB_PORT = 3306                  # Database 端口
DB_NAME = 'mini_chat'           # Database name


# ----------数据协议相关配置------
REQUEST_LOGIN = '0001'          # 登录请求
REQUEST_CHAT = '0002'           # 聊天请求
RESPONSE_LOGIN_RESULT = '1001'  # 登录结果响应
RESPONSE_CHAT = '1002'          # 聊天响应
DELIMITER = '|'                 # 自定义协议数据分隔符
#