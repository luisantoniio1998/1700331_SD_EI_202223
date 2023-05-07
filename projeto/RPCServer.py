import xmlrpc.server

class MyRPCServer:

    def get_information(x):

        

    server.register_function(get_information, 'get')


server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
#server.register_instance(MyRPCServer())
server.serve_forever()