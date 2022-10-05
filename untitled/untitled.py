import os

import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')



args = arg_parser.parse_args()

id = args.id




local_path_AHN4 = "/project/lidarac/Data/Regions/Oostvaarderplassen/AHN4"

laz_files = [f for f in os.listdir(local_path_AHN4) if f.endswith('.LAZ')]

import json
filename = "/tmp/laz_files_" + id + ".json"
file_laz_files = open(filename, "w")
file_laz_files.write(json.dumps(laz_files))
file_laz_files.close()
