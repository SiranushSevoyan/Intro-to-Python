import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text")

args = parser.parse_args()

print("The given string: %s" % str(args.text))
print("All lowercase: %s" % str(args.text).lower())
print("All uppercase: %s" % str(args.text).upper())