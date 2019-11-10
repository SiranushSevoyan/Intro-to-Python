import argparse

parser=argparse.ArgumentParser()

parser.add_argument("value")

args=parser.parse_args()
set1 = {'hello', 1, True, 'goodbye', '2', 'False'}
print(set1)
set1.add(args.value)
print(set1)