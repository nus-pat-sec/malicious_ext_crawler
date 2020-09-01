import json
from datetime import datetime
import dateutil.parser as dparser
import matplotlib.pyplot as plt

last_seven_months = [0, 0, 0, 0, 0, 0, 0]

with open('/home/students/s4544688/research_2020/malicious_ext_crawler/malicious_ext_crawler/output_data/combined.json') as json_file:
    data_dict = json.load(json_file)

    

    for p in data_dict:

        date_type = dparser.parse(p["last_updated"],fuzzy=True)
        if (date_type.year == 2020):
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
                
for total in last_seven_months:
    print(total)

x_units = [1, 2, 3, 4, 5, 6, 7]

y_units = last_seven_months

months_label = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July']

plt.bar(x_units, y_units, tick_label=months_label,
        width=0.8, color=['red', 'green', 'blue', 'orange', 'purple', 'brown', 'pink'])
        # print(date_type.year)
plt.xlabel('Last 7 months')
plt.ylabel('The number of "potentially malicious" browser extensions')
plt.title('2020 the number of "potentially malicious" browser extensions, Firefox')

plt.show()
    # print(data_dict[0])
