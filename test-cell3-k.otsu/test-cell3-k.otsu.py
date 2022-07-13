

data = [1, 2, 3, 4, 5]
data2 = [6, 7, 8, 9, 10]

import json
filename = "/tmp/data2_" + id + ".json"
file_data2 = open(filename, "w")
file_data2.write(json.dumps(data2))
file_data2.close()
filename = "/tmp/data_" + id + ".json"
file_data = open(filename, "w")
file_data.write(json.dumps(data))
file_data.close()
