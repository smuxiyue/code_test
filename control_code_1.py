
file = "/../../data.txt"
f = open(file,'r')
data = f.read()
if data == '2':
    actuators.accel = -0.5
f.close()

