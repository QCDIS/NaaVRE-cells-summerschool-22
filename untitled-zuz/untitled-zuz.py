

data1 = "1"
data2 = "2"
data3 = data1 + data2
a="5"
b="6"

import json
filename = "/tmp/data2_" + id + ".json"
file_data2 = open(filename, "w")
file_data2.write(json.dumps(data2))
file_data2.close()
filename = "/tmp/data1_" + id + ".json"
file_data1 = open(filename, "w")
file_data1.write(json.dumps(data1))
file_data1.close()
