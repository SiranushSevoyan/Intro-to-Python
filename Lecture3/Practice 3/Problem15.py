import argparse

parser=argparse.ArgumentParser()

parser.add_argument("key", type=str)
parser.add_argument("value", type=str)

args=parser.parse_args()

dict2= {"Mariam":"David", "Lilit":"?????"}
dict2[args.key]=args.value
print(dict2)
