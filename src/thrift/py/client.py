import sys, os.path
sys.path.insert(0, "/usr/lib/python2.6/site-packages")
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'gen-py'))

import example.UserStorage

from example.ttypes import MartialArt
from example.ttypes import UserProfile

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = example.UserStorage.Client(protocol)

    for i in range(1000):
        transport.open()
        for j in range(9):
            user = client.retrieve(26)
            assert(user.uid == 26)

        user = UserProfile(
            uid=26,
            name="Ralph Waldo Emerson",
            style=MartialArt.KARATE
        )
        client.store(user)
        if i % 100 == 0:
            print i
        transport.close()

except Thrift.TException, tx:
    print '%s' % (tx.message)
