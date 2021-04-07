import json
import datetime as dt
import os
import csv

fieldnames = ['date', 'username', 'text']
with open('scanteaksg.csv', mode='w') as csv_file:
   writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
   writer.writeheader()
   for filename in os.listdir(os.getcwd()):
      with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
         # do your stuff
         data = json.load(f)
         for dat in data:
            comment = []
            date = (dt.datetime.fromtimestamp(dat['created_at']).strftime('%Y-%m-%d %H:%M:%S'))
            user = (dat['owner']['username'])
            comment = (dat['text'])
            writer.writerow({'date': str(date), 'username': str(user), 'text': str(comment)})


   print("END____________________________________________")