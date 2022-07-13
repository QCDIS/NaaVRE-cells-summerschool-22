import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')

arg_parser.add_argument('--processed_data', action='store' , type=str , required='True', dest='processed_data')


args = arg_parser.parse_args()

id = args.id

processed_data = args.processed_data



result = processed_data

