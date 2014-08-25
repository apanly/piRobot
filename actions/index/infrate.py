import zmq


class innerInfrated:
    def __init__(self):
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect ("tcp://localhost:5555")
        self.socket=socket

    def gogo(self,command):
        self.socket.send (command)
        return self.socket.recv()
