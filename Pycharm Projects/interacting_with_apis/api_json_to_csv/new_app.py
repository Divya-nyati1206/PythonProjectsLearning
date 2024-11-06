import requests
import json
import csv

response = requests.get("https://dummyjson.com/users").json()


with open("json_file.json",'w') as fp:
     fp.write(json.dumps(response["users"], indent = 4))
    # json.dump(response["users"], fp)


with open("json_file.json",'r') as fp:
     json_obj = json.load(fp)


print(type(json_obj))


fields = list(json_obj[0].keys())
# fields = "id,firstName,lastName,maidenName,age,gender,email,phone,username,password".split(',')

with open("csv_file.csv", 'w') as csvfile:
    writer = csv.DictWriter(csvfile,delimiter="|", fieldnames=fields)

    writer.writeheader()
 
    writer.writerows(json_obj)









'''with open("csv_file.csv",'r') as fp:
     csv_r = csv.reader(fp)
     flag = 0
     for row in csv_r:
          if flag == 0:
               fields = row
               flag = 1
'''



'''
with open("csv_file.csv",'w') as fp:
     csv_w = csv.writer(fp)

     csv_w.writerows(json_obj)
'''