import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')

arg_parser.add_argument('--data', action='store' , type=str , required='True', dest='data')
arg_parser.add_argument('--data2', action='store' , type=str , required='True', dest='data2')


args = arg_parser.parse_args()

id = args.id

data = args.data
data2 = args.data2



proc=data+data2

import json
filename = "/tmp/proc_" + id + ".json"
file_proc = open(filename, "w")
file_proc.write(json.dumps(proc))
file_proc.close()
