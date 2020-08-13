import json
from datetime import datetime
import dateutil.parser as dparser
import matplotlib.pyplot as plt
import re
import csv

# find substring without case sensitives
def f_wo_case(substring, main_string):

    if re.search(substring, main_string, re.IGNORECASE):
        return True

    return False

cleaned_data = []
# with open('combined.json') as json_file:
#     data_dict = json.load(json_file)
with open('chrome_ext_data.json') as json_file:
    data_dict = json.load(json_file)

    

    for each in data_dict:

        # date_type = dparser.parse(each["last_updated"],fuzzy=True)
        ####### Using key filters
        key = each["key"]
        common_words_filters_key = (key.find("coin") != -1 or key.find("wallet") != -1 or key.find("exchange") != -1 or key.find("token") != -1 or \
                key.find("ether") != -1 or key.find("currency") != -1 or key.find("exchange") != -1 or key.find("crypto") != -1 or \
                key.find("chain") != -1 or key.find("cash") != -1 or key.find("transaction") != -1 or key.find("bank") != -1 or \
                key.find("pay") != -1 or key.find("money") != -1 or key.find("card") != -1 or key.find("card") != -1 or \
                key.find("binance") != -1 or key.find("ledger") != -1 or key.find("ledger") != -1 or key.find("trezor") != -1 or key.find("trezor") != -1 )

        filters_key = ( common_words_filters_key and (key.find("theme") == -1) )

        ######## Using name filters
        name = each["name"]     
        # Reason for excluding them because Firefox has a bac search engine that cannt effectively classify theme and extensions
        common_words_filters_name = (f_wo_case("coin", name) == True or f_wo_case("wallet", name) == True or f_wo_case("exchange", name) == True or f_wo_case("token", name) == True or \
                f_wo_case("ether", name) == True or f_wo_case("currency", name) == True or f_wo_case("exchange", name) == True or f_wo_case("crypto", name) == True or \
                f_wo_case("chain", name) == True or f_wo_case("cash", name) == True or f_wo_case("transaction", name) == True or f_wo_case("bank", name) == True or \
                f_wo_case("pay", name) == True or f_wo_case("money", name) == True or f_wo_case("card", name) == True or f_wo_case("bit", name) == True or \
                f_wo_case("nance", name) == True or f_wo_case("ledger", name) == True or f_wo_case("trezor", name) == True) 

        filters_name = ( common_words_filters_name and (f_wo_case("theme", name) == False) )
        
        ####### combining name and key filters by OR
        filters = filters_key or filters_name
        
        if (filters):
            cleaned_data.append(each)



# with open('cleaned_data.json', 'w') as cleaned_json:
# 	json.dump(cleaned_data, cleaned_json)
with open('chrome_cleaned_data.json', 'w') as cleaned_json:
	json.dump(cleaned_data, cleaned_json)

# csv_columns = ['platform','key','name', 'rating', 'user_numbers', 'creator', 'last_updated', 'reviews']
# csv_file = "cleaned_data.csv"
csv_columns = ['platform', 'id', 'key','name', 'rating', 'user_numbers', 'creator', 'last_updated']
csv_file = "chrome_cleaned_data.csv"

with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in cleaned_data:
        writer.writerow(data)