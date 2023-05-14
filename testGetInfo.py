import requests

# define the URL endpoint for the API
url = "https://blockchain.info/rawblock/"

# prompt user to enter the block hash they want information on
block_hash = input("Enter the block hash: ")

# make the API request and store the response
response = requests.get(url + block_hash)

# if response status code is not OK, raise an exception
response.raise_for_status()

# create a new file with the block hash as the filename
filename = block_hash + ".txt"
with open(filename, "w") as f:
    # write the response content to the file
    f.write(response.text)
    
print("Block information saved to " + filename)