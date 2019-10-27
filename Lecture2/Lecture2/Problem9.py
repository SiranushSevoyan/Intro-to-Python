import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", type=str)
parser.add_argument("start_index", type=int)
parser.add_argument("end_index", type=int)


args = parser.parse_args()
print("The given text: ", args.text)
print("Start index: ", args.start_index)
print("end index: ", args.end_index)
print("Output string: ", args.text[args.start_index:args.end_index])