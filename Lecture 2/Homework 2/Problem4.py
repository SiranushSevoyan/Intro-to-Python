import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", type=str)


args = parser.parse_args()


print ("The given string: ", args.text)

print ("The USA/usa count is: ", args.text.count("usa")+args.text.count("USA"))
print ("The new string: ", args.text.replace("usa", "Armenia").replace("USA", "Armenia"))
