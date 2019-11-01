import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--age")

args = parser.parse_args()
if args.age:
    print("Happy Birthday, you are already %s years old" % str(args.age))
