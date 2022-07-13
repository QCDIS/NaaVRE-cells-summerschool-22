

data0  = 'coucou'
data1  = 'hello'

import json
filename = "/tmp/data1_" + id + ".json"
file_data1 = open(filename, "w")
file_data1.write(json.dumps(data1))
file_data1.close()
filename = "/tmp/data0_" + id + ".json"
file_data0 = open(filename, "w")
file_data0.write(json.dumps(data0))
file_data0.close()
