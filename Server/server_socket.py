from socket import socket, AF_INET, SOCK_STREAM
from config import SERVER_IP, SERVER_PORT


class ServerSocket(socket):
    """包装服务器端套接字类"""
    def __init__(self):
        # 初始化套接字
        super(ServerSocket, self).__init__(AF_INET, SOCK_STREAM)
        # 绑定IP和PORT
        self.bind((SERVER_IP,SERVER_PORT))
        # 设置为被动监听套接字
        self.listen(128)