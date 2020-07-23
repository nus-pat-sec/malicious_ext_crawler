import json
from datetime import datetime
import dateutil.parser as dparser
import matplotlib.pyplot as plt
import re

cleaned_data = []
with open('cleaned_data.json') as json_file:
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
        

        filters = ( common_words_filters and (key.find("theme") == -1) )
        
        
        
        if (filters):
            filter_data.append(each)



with open('manual_filters_results.json', 'w') as filter_json:
	json.dump(filter_data, filter_json)