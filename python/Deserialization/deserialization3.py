# A test object
import pickle
def identity(n):
    return n
# Deserialization
reconstructed = pickle.load(open('Deserialization/files/outputser3','rb'))
print(reconstructed(10))
#print(reconstructed)
