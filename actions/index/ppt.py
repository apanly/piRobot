import zmq


class innerppt:
    def __init__(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect ("tcp://localhost:5558")
        self.socket=socket

    def gogo(self,command):
        self.socket.send (command)
        return self.socket.recv()
