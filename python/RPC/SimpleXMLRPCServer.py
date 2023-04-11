from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Register pow() function; this will use the value of
    # pow.__name__ as the name, which is just 'pow'.
    server.register_function(pow)

    # Register a function under a different name
    def adder_function(x, y):
        return x + y
    server.register_function(adder_function, 'add')

    def somatorio(n):
        total = 0
        for i in range(1,n+1):
            total += i**3
        return total
    server.register_function(somatorio, 'sum')

    def minus_function(x,y):
        return x - y
    server.register_function(minus_function, 'subtract')

    def div_function(x,y):
        return x // y
    server.register_function(div_function, 'divide')
    
    def complex_num(x, y):
        return str(complex(x, y)).replace('j', 'i')
    
    def sum_comple(a1,a2,b1,b2):
        x = a1 + a2
        y = b1 + b2 
        return (complex_num(x,y))
    server.register_function(sum_comple, 'soma_complexo')

    def mul_comple(a1,a2,b1,b2):
        x = (a1*a2)-(b1*b2)
        y = (a2*b1)+(a1*b2)
        return (complex_num(x,y))
    server.register_function(mul_comple, 'multi_complexo')

    #def chatGPT4(): 
     #   return ("Inteligencia Artificial")
    #server.register_function(chatGPT4, 'ia')

    # Register an instance; all the methods of the instance are
    # published as XML-RPC methods (in this case, just 'mul').
    class MyFuncs:
        def mul(self, x, y):
            return x * y

    server.register_instance(MyFuncs())

    # Run the server's main loop
    server.serve_forever()

