import pandas as pd
import csv

s=input("enter password:")
lock = open('lock.csv','w', newline='')
obj = csv.writer(lock)
obj.writerows(s)
lock.close()
print(lock)
a=input("enter pass:")

if a==lock:
    print("successful")
else:
    print("failure")