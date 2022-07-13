import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')

arg_parser.add_argument('--a', action='store' , type=float , required='True', dest='a')
arg_parser.add_argument('--b', action='store' , type=float , required='True', dest='b')
arg_parser.add_argument('--c', action='store' , type=float , required='True', dest='c')


args = arg_parser.parse_args()

id = args.id

a = args.a
b = args.b
c = args.c



def foo(a, b):
    return a + b

def bar(a, b):
    return a * b

res = bar(foo(a, b), c)
res

import json
filename = "/tmp/foo_" + id + ".json"
file_foo = open(filename, "w")
file_foo.write(json.dumps(foo))
file_foo.close()
