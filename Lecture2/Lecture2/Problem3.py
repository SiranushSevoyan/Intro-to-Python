import argparse

parser = argparse.ArgumentParser()

parser.add_argument("X")

args = parser.parse_args()
print("Welcome, %s!" % str(args.X))