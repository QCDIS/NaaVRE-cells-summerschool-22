
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_p1', action='store', type=int, required='True', dest='param_p1')

args = arg_parser.parse_args()

id = args.id


param_p1 = args.param_p1



a = 1 + param_p1

import json
filename = "/tmp/a_" + id + ".json"
file_a = open(filename, "w")
file_a.write(json.dumps(a))
file_a.close()
