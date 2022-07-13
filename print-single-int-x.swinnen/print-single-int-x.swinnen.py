import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')

arg_parser.add_argument('--i', action='store' , type=int , required='True', dest='i')


args = arg_parser.parse_args()

id = args.id

i = args.i



print(str(i))

