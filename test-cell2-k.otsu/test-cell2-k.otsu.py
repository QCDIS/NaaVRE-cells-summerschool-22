import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')

arg_parser.add_argument('--data', action='store' , type=int , required='True', dest='data')
arg_parser.add_argument('--data2', action='store' , type=int , required='True', dest='data2')


args = arg_parser.parse_args()

id = args.id

data = args.data
data2 = args.data2



processed_data = data[1] + data2[3]

import json
filename = "/tmp/processed_data_" + id + ".json"
file_processed_data = open(filename, "w")
file_processed_data.write(json.dumps(processed_data))
file_processed_data.close()
