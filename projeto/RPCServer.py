import xmlrpc.server
import requests


class MyRPCServer:

    def get_information(block_hash):
    
        #     # define the URL endpoint for the API
        # url = "https://blockchain.info/rawblock/"

        # # make the API request and store the response
        # response = requests.get(url + block_hash)

        # # if response status code is not OK, raise an exception
        # response.raise_for_status()

        # # parse the JSON response
        # block_data = response.json()

        # # extract the number of transactions and total value
        # num_txns = block_data['n_tx']
        # total_value = block_data.get('total', 0)

        # # calculate the total amount of BTC transferred in the block
        # total_btc = sum([out['value'] for tx in block_data['tx'] for out in tx['out']])

        # # calculate the block height from the block index
        # block_index = block_data['block_index']
        # height = requests.get("https://blockchain.info/block-height/" + str(block_index) + "?format=json").json()['blocks'][0]['height']

        # create a new file with the block hash as the filename
        filename = block_hash + ".txt"
        # with open(filename, "w") as f:
        #     # write the important information to the file
        #     f.write("Block height: " + str(height) + "\n")
        #     f.write("Number of transactions: " + str(num_txns) + "\n")
        #     f.write("Total value: " + str(total_value) + " satoshis\n")
        #     f.write("Total BTC transferred: " + str(total_btc / 100000000) + " BTC\n")

        return filename
    


server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_instance(MyRPCServer())
server.serve_forever()