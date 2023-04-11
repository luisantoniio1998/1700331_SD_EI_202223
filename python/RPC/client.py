import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
x= float(input("entre o 1-valor: "))
y=float(input("entre o 2-valor: "))
n= int(input("entre o valor n para fazer somatorio:"))
a1 = float(input("parte real complexo 1: "))
b1 = float(input("parte imaginaria complexo 1: "))
a2 = float(input("parte real complexo 2: "))
b2 = float(input("parte imaginaria complexo 2: "))
       
print(type(x))
print(s.pow(x%150,y%10))  # Returns x ^ y
print(s.add(x,y))  # Returns x + y
print(s.mul(x,y))  # Returns x * y
print(s.subtract(x,y)) #Returns x - y 
print(s.divide(x,y)) #Returns x / y 
print(s.sum(n))
print(s.soma_complexo(a1,a2,b1,b2))
print(s.multi_complexo(a1,a2,b1,b2))
#print(s.ia()) #Returns inteligencia artificial

# Print list of available methods
print(s.system.listMethods())