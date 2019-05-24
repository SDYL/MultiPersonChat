

class SocketWrapper(object):
    """包装客户端套接字"""
    def __init__(self, sock):
        self.sock = sock

    def recv_data(self):
        """接受数据请求"""
        return self.sock.recv(512).decode("utf-8")

    def send_data(self, messages):
        return self.sock.send(messages.encode("utf-8"))
