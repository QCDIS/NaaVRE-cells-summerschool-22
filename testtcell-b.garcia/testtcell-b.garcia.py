

data= [1,2,3,4,5]


import json
filename = "/tmp/data_" + id + ".json"
file_data = open(filename, "w")
file_data.write(json.dumps(data))
file_data.close()
