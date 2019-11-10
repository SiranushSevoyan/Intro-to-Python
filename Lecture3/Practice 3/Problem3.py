import argparse

parser = argparse.ArgumentParser()

parser.add_argument("value", type=str)
list2=[0, 'hi', 2, 100, 300, 2, "hi"]

args = parser.parse_args()
a=list2.count(args.value)


print (a)