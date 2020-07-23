import json
from datetime import datetime
import dateutil.parser as dparser
import matplotlib.pyplot as plt
import re
import csv


cleaned_data = []
with open('combined.json') as json_file:
    data_dict = json.load(json_file)

    

    for each in data_dict:

        # date_type = dparser.parse(each["last_updated"],fuzzy=True)
        key = each["key"]
        # a_string.find(substring1)
        # if ((key.find("coin") != -1 or key.find("wallet") != -1 or key.find("exchange") or key.find("token") or key.find("ether") or key.find("currency")) != -1) and key.find("theme") == -1):
        # if (re.search('coin', name, re.IGNORECASE) == True or re.search('wallet', name, re.IGNORECASE) == True):
        # print(re.search('coin', name, re.IGNORECASE))
        
        # filter_words = ['wallet', 'coin']
        # for word in filter_words:
        #     if (word.lower() in name.lower()):
        common_words_filters = (key.find("coin") != -1 or key.find("wallet") != -1 or key.find("exchange") != -1 or key.find("token") != -1 or \
                key.find("ether") != -1 or key.find("currency") != -1 or key.find("exchange") != -1 or key.find("crypto") != -1 or \
                key.find("chain") != -1)

        filters = ( common_words_filters and (key.find("theme") == -1) )
        
        
        
        if (filters):
            cleaned_data.append(each)



with open('cleaned_data.json', 'w') as cleaned_json:
	json.dump(cleaned_data, cleaned_json)

csv_columns = ['platform','key','name', 'rating', 'user_numbers', 'creator', 'last_updated', 'reviews']
csv_file = "cleaned_data.csv"

with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in cleaned_data:
        writer.writerow(data)