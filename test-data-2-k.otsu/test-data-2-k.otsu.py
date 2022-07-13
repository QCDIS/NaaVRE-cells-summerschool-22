import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')

arg_parser.add_argument('--data', action='store' , type=int , required='True', dest='data')


args = arg_parser.parse_args()

id = args.id

data = args.data



data2 = data

