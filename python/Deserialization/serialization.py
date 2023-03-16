# A test object
import pickle

f = open("/home/kali/Desktop/github_202223/1700331_SD_EI_202223/python/Deserialization/files/demo2.txt", "r",encoding='utf8')
x=f.read()

# Serialization
with open("/home/kali/Desktop/github_202223/1700331_SD_EI_202223/python/Deserialization/files/outputser1.pickle", "wb") as outfile:
    pickle.dump(x, outfile)
print("Written object outputser1")