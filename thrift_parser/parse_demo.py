from ptsd.parser import Parser
with open('../thrift-idl/tutorial.thrift') as fp:
    tree = Parser().parse(fp.read())
