

x = 1
y = 2

a = 2
b = 3
c = 5

import json
filename = "/tmp/x_" + id + ".json"
file_x = open(filename, "w")
file_x.write(json.dumps(x))
file_x.close()
filename = "/tmp/y_" + id + ".json"
file_y = open(filename, "w")
file_y.write(json.dumps(y))
file_y.close()
filename = "/tmp/a_" + id + ".json"
file_a = open(filename, "w")
file_a.write(json.dumps(a))
file_a.close()
filename = "/tmp/c_" + id + ".json"
file_c = open(filename, "w")
file_c.write(json.dumps(c))
file_c.close()
filename = "/tmp/b_" + id + ".json"
file_b = open(filename, "w")
file_b.write(json.dumps(b))
file_b.close()
