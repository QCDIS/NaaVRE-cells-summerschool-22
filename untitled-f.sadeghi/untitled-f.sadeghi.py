import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')

arg_parser.add_argument('--process_data', action='store' , required='True', dest='process_data')


args = arg_parser.parse_args()

id = args.id

process_data = args.process_data



process_data.append(3)
process_data

