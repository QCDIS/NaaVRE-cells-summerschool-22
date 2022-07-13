import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')

arg_parser.add_argument('--process_concatt', action='store' , type=int , required='True', dest='process_concatt')


args = arg_parser.parse_args()

id = args.id

process_concatt = args.process_concatt



process_concatt

