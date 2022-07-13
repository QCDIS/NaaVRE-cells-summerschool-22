import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')

arg_parser.add_argument('--data_1', action='store' , required='True', dest='data_1')
arg_parser.add_argument('--data_2', action='store' , required='True', dest='data_2')


args = arg_parser.parse_args()

id = args.id

data_1 = args.data_1
data_2 = args.data_2



process_data = data_1 + data_2

