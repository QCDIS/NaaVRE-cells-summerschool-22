


data1 = [1,2,3,4]
data2 = [5,6,7,8]

import json
filename = "/tmp/data2_" + id + ".json"
file_data2 = open(filename, "w")
file_data2.write(json.dumps(data2))
file_data2.close()
filename = "/tmp/data1_" + id + ".json"
file_data1 = open(filename, "w")
file_data1.write(json.dumps(data1))
file_data1.close()
