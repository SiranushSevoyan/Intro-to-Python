import argparse
import datetime
import time
import calendar

parser = argparse.ArgumentParser()

parser.add_argument("--num_y", type=int)
parser.add_argument("--num_d", type=int)


args = parser.parse_args()

tday=datetime.datetime.today()
print ("Current date: ",tday)
print ("Given years: ", args.num_y)
print ("Given days: ", args.num_d)
Final_dateV1=tday.replace(year=tday.year+args.num_y)
print("Final Date: ",Final_dateV1)
days=Final_dateV1-tday
two_year = datetime.timedelta(days = days.days)
Final_dateV2 = tday + two_year
print("Final Date: ", Final_dateV2)
