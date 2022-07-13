

arr = [5,7,23,4,2,98,56,8]

import json
filename = "/tmp/arr_" + id + ".json"
file_arr = open(filename, "w")
file_arr.write(json.dumps(arr))
file_arr.close()
