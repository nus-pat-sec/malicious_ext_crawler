import json
import numpy as np

with open ('sub_data_1.json') as json_file:
	data_dict = json.load(json_file)

for num in range(2, 10):
	url = 'sub_data_%s.json' % num
	with open (url) as json_file_next:
		data_dict_next = json.load(json_file_next)

		data_dict = data_dict + data_dict_next

with open ('combined.json', 'w') as json_combined:
	json.dump(data_dict, json_combined)