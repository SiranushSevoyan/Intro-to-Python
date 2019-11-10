import argparse

parser=argparse.ArgumentParser()

parser.add_argument("value", type=int)

args=parser.parse_args()

set3={1, 5, 9, 55, 32, 98}
print(min(set3))
print(max(set3))

if min(set3)<args.value<max(set3):
    print("True")
else:
    print("False")