import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')

arg_parser.add_argument('--data', action='store' , type=str , required='True', dest='data')
arg_parser.add_argument('--data2', action='store' , type=str , required='True', dest='data2')


args = arg_parser.parse_args()

id = args.id

data = args.data
data2 = args.data2




data_concat = data + data2

import json
filename = "/tmp/data_concat_" + id + ".json"
file_data_concat = open(filename, "w")
file_data_concat.write(json.dumps(data_concat))
file_data_concat.close()
