#!/usr/bin/env python3

"""
An example illustrating IPC (Inter Process Communication)
between a Python script "modeling" shaka-show
and a C++ program "modeling" shaka-scheme

"""

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
port = "8989"
socket.connect('tcp://localhost:%s' % port)

for i in range(10):
    socket.send(b"Hello from Python application!")
    print("waiting to receive...")
    message = socket.recv()
    print("Server replied", message.decode('utf-8'))
    time.sleep(5)
