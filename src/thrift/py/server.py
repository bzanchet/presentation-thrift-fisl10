#!/usr/bin/env python

import sys, os.path
sys.path.insert(0, "/usr/lib/python2.6/site-packages")
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'gen-py'))

import example.UserStorage

from example.ttypes import MartialArt
from example.ttypes import UserProfile
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from multiprocessing import freeze_support
import TPreForkServer

class UserStorageHandler:
    def __init__(self):
        pass

    def store(self, user):
        #print "stored " + str(user)
        pass

    def retrieve(self, id):
        #print "retrieved " + str(id)
        return UserProfile(
            uid=id,
            name="Ralph Waldo Emerson",
            style=MartialArt.KARATE
        )

      
if __name__ == '__main__':
    freeze_support()
    handler = UserStorageHandler()
    processor = example.UserStorage.Processor(handler)
    transport = TSocket.TServerSocket(9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TPreForkServer.TPreForkServer(processor, transport, tfactory, pfactory)

    print 'Starting the server...'
    freeze_support()
    server.serve()

    #server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    #server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
    #server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)
    #server = TServer.TForkingServer(processor, transport, tfactory, pfactory)
