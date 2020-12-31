import json
import csv

with open('first.json','r') as json_file:
    convert = json.load(json_file)

    field = ['url','email','password']

    with open('new_csv.csv','w') as new_csv:
        write = csv.DictWriter(new_csv,fieldnames=field)

        write.writeheader()
        write.writerows(convert)