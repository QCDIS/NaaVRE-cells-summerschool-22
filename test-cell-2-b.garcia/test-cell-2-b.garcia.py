import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')

arg_parser.add_argument('--data1', action='store' , type=int , required='True', dest='data1')
arg_parser.add_argument('--data2', action='store' , type=int , required='True', dest='data2')


args = arg_parser.parse_args()

id = args.id

data1 = args.data1
data2 = args.data2




processed_data = data1 + data2

import json
filename = "/tmp/processed_data_" + id + ".json"
file_processed_data = open(filename, "w")
file_processed_data.write(json.dumps(processed_data))
file_processed_data.close()
