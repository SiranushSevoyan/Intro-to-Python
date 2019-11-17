import argparse

parser = argparse.ArgumentParser()

parser.add_argument("Text", type=str)


args = parser.parse_args()
b=int((len(args.Text)-3)/2)
c=int((len(args.Text)+3)/2)


print ("The old string:: ", args.Text)
print ("Middle 3 characters: ", args.Text[b:c])
print ("Middle 3 characters: ", args.Text[:b]+args.Text[b:c].upper()+args.Text[c:])