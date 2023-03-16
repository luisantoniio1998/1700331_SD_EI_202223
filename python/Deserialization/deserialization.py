# A test object
import pickle

# Deserialization
x_reconstructed=""
with open("/home/kali/Desktop/github_202223/1700331_SD_EI_202223/python/Deserialization/files/outputser1.pickle", "rb") as infile:
    x_reconstructed = x_reconstructed+pickle.load(infile)
print("Reconstructed object outputser1.pickle\n", x_reconstructed)
