import logging

from multiprocessing import Process
from multiprocessing import Queue
from multiprocessing import current_process

from thrift.transport import TTransport
from thrift.server import TServer

class TPreForkServer(TServer.TServer):
  def __init__(self, *args):
    TServer.TServer.__init__(self, *args)
    self.threads = 10

  def serveClient(self, client):
    """Process input/output from a client for as long as possible"""
    itrans = self.inputTransportFactory.getTransport(client)
    otrans = self.outputTransportFactory.getTransport(client)
    iprot = self.inputProtocolFactory.getProtocol(itrans)
    oprot = self.outputProtocolFactory.getProtocol(otrans)
    try:
      while True:
        self.processor.process(iprot, oprot)
    except TTransport.TTransportException, tx:
      pass
    except Exception, x:
      logging.exception(x)
    
    itrans.close()
    otrans.close()
    
  def doServe(self, t):
    # Pump the socket for clients
    while True:
      try:
        client = t.accept()
        self.serveClient(client)
      except Exception, x:
        logging.exception(x)

  def serve(self):
    """Start a fixed number of worker threads and put client into a queue"""
    self.serverTransport.listen()
    for i in range(self.threads):
      try:
        t = Process(target = self.doServe, args=(self.serverTransport,))
        t.start()
      except Exception, x:
        logging.exception(x)
    print "bye!"
