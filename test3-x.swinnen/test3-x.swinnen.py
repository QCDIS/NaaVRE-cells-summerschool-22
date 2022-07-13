import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')

arg_parser.add_argument('--x', action='store' , type=float , required='True', dest='x')
arg_parser.add_argument('--y', action='store' , type=float , required='True', dest='y')


args = arg_parser.parse_args()

id = args.id

x = args.x
y = args.y



print("x: " + str(x) + "; y: " + str(y))

