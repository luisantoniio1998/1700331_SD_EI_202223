import pickle
class NewClass:
    def __init__(self, data):
        print(data)
        self.data = data
        self.x=0
    def setX(self,x):
        self.x=x;

reconstructed = pickle.load(open('/home/kali/Desktop/github_202223/1700331_SD_EI_202223/python/Deserialization/files/outputser2.pickle','rb'))
print("Data from reconstructed object:", reconstructed.data,reconstructed.x)
reconstructed.setX(2)
print("Data from reconstructed object:", reconstructed.data,reconstructed.x)