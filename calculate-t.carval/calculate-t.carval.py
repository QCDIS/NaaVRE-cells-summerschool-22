import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')

arg_parser.add_argument('--data0', action='store' , type=str , required='True', dest='data0')
arg_parser.add_argument('--data1', action='store' , type=str , required='True', dest='data1')


args = arg_parser.parse_args()

id = args.id

data0 = args.data0
data1 = args.data1



data2 = data0 + ' ' + data1 

import json
filename = "/tmp/data2_" + id + ".json"
file_data2 = open(filename, "w")
file_data2.write(json.dumps(data2))
file_data2.close()
