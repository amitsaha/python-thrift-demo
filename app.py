import io
from flask import Flask
from flask import make_response, send_file, request
from tutorial import Calculator
import tutorial.ttypes
from shared.ttypes import SharedStruct
from thrift.protocol import TBinaryProtocol
from thrift.server import THttpServer
from thrift.server import TServer
from thrift.transport import TTransport
app=Flask(__name__)
class CalculatorHandler(object):
    def __init__(self):
        self.log = {}
    def ping(self):
        print("ping()")
    def add(self, n1, n2):
        print("add({}, {})".format(n1, n2))
        return n1 + n2
@app.route('/thr', methods=['POST'])
def thr():
    # get the thrift package from HTTP POST body
    body = request.get_data()
    content_length = int(request.headers["Content-Length"])
    # thrift setup
    itrans = TTransport.TMemoryBuffer(body)
    itrans = TTransport.TBufferedTransport(itrans, content_length)
    otrans = TTransport.TMemoryBuffer()
    handler = CalculatorHandler()
    processor = Calculator.Processor(handler)
    inputProtocolFactory = TBinaryProtocol.TBinaryProtocolFactory()
    outputProtocolFactory = inputProtocolFactory
    iprot = inputProtocolFactory.getProtocol(itrans)
    oprot = outputProtocolFactory.getProtocol(otrans)
    processor.process(iprot,oprot)
    response = make_response(otrans.getvalue())
    response.headers['Content-Type'] = 'application/x-thrift'
    return response, 200
if __name__ == '__main__':
    app.run()
