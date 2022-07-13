

data_1 = [1]
data_2 = [2]

import json
filename = "/tmp/data_1_" + id + ".json"
file_data_1 = open(filename, "w")
file_data_1.write(json.dumps(data_1))
file_data_1.close()
filename = "/tmp/data_2_" + id + ".json"
file_data_2 = open(filename, "w")
file_data_2.write(json.dumps(data_2))
file_data_2.close()
