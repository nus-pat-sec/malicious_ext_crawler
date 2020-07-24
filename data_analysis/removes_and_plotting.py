import json
from datetime import datetime
import dateutil.parser as dparser
import matplotlib.pyplot as plt

import csv

# Remove duplicates
def remove_dup_list_dic(test_list):
     # remove duplicates
    # seen = set()
    # new_filter_cleaned_data = []
    # for each in filter_cleaned_data:
    #     tup = tuple(each.items())
    #     if tup not in seen:
    #         seen.add(tup)
    #         new_filter_cleaned_data.append(each)
    res_list = [] 
    for i in range(len(test_list)): 
        if test_list[i] not in test_list[i + 1:]: 
            res_list.append(test_list[i])

    return res_list

def export_csv(filter_cleaned_data,csv_file):
   
    final_data = remove_dup_list_dic(filter_cleaned_data)
    
    csv_columns = ['platform','key','name', 'rating', 'user_numbers', 'creator', 'last_updated', 'reviews']

    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in final_data:
            writer.writerow(data)

def processing(input_file):
    data = []
    last_seven_months = [0, 0, 0, 0, 0, 0, 0]

    with open(input_file) as json_file:
        data_dict = json.load(json_file)

        # Removing duplicates
        clean_data = remove_dup_list_dic(data_dict)


        for p in clean_data:

            date_type = dparser.parse(p["last_updated"],fuzzy=True)
            # 2020
            if (date_type.year == 2020):
                data.append(p)
                # Jan
                if (date_type.month == 1):
                    last_seven_months[0] = last_seven_months[0] + 1
                # Feb
                elif (date_type.month == 2):
                    last_seven_months[1] = last_seven_months[1] + 1
                # Mar
                elif (date_type.month == 3):
                    last_seven_months[2] = last_seven_months[2] + 1
                # April
                elif (date_type.month == 4):
                    last_seven_months[3] = last_seven_months[3] + 1
                # May
                elif (date_type.month == 5):
                    last_seven_months[4] = last_seven_months[4] + 1
                # June
                elif (date_type.month == 6):
                    last_seven_months[5] = last_seven_months[5] + 1
                # July
                elif (date_type.month == 7):
                    last_seven_months[6] = last_seven_months[6] + 1
                    
    # for total in last_seven_months:
    #     print(total)

    y_units = last_seven_months

    result = [y_units, data]
    return result




x_units = [1, 2, 3, 4, 5, 6, 7]
y_1 = processing("cleaned_data.json")
# export csv
export_csv(y_1[1],"cleaned_data.csv")
y_2 = processing("combined.json")

f = plt.figure(1)
# two figure
# fig, (ax1, ax2) = plt.subplots(1, 2)

plt.subplot(211)

months_label = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July']

plt.bar(x_units, y_1[0], tick_label=months_label,
        width=0.8, color=['red', 'green', 'blue', 'orange', 'purple', 'brown', 'pink'])
        # print(date_type.year)
# plt.xlabel('Last 7 months')
# plt.ylabel('The number of "potentially malicious" browser extensions')
plt.title('Cleaning up')
# plt.suptitle('Comparision between before (left) and after (right) cleaning up ')
plt.subplot(212)
plt.bar(x_units, y_2[0], tick_label=months_label,
        width=0.8, color=['red', 'green', 'blue', 'orange', 'purple', 'brown', 'pink'])
plt.title('without cleaning up')
# plt.suptitle('Comparision between before (left) and after (right) cleaning up ')

# plt.suptitle('Comparision between before (left) and after (right) cleaning up ')

# ax1.plot(x_units, y_units)
plt.show()
    # print(data_dict[0])
