import pickle
class NewClass:
    def __init__(self, data):
        print(data)
        self.data = data
        self.x=0

    def setX(self,x):
        self.x=x;
# Create an object of NewClass
new_class = NewClass(1)
new_class.x=10
# Serialize o objecto new_class
outfile=open("/home/kali/Desktop/github_202223/1700331_SD_EI_202223/python/Deserialization/files/outputser2.pickle", "wb")
pickle.dump(new_class, outfile)