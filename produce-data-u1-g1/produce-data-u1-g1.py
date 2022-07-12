


data = ["count the character in this string"]

import json
filename = "/tmp/data_" + id + ".json"
file_data = open(filename, "w")
file_data.write(json.dumps(data))
file_data.close()
