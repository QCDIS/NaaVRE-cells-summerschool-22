import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')

arg_parser.add_argument('--arr', action='store' , required='True', dest='arr')


args = arg_parser.parse_args()

id = args.id

arr = args.arr



for i in arr:
    print(str(i))

