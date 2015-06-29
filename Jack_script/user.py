#stripping out bash lines
input_file = open("user.txt", "r")
output = open("user_out.txt", "w")

for i, line in enumerate(input_file):
    if not (("default" in line) or ("bash" in line)):
        output.write(line)

user_temp=[]
user=[]
file_system=[]
dataUsed_notconverted=[]
dataUsed_converted=[]
data =[]


input_file = open("user_out.txt", "r")
for i, line in enumerate(input_file):
	if("user" in line):
		data = line.split()
		if(len(data)>2):
			user_temp.append(data[1])
			file_system.append(data[2])
			dataUsed_notconverted.append(data[9])

print user_temp, "\n"
print file_system, "\n"
print dataUsed_notconverted, "\n"

print len(user_temp), "\n"
print len(file_system), "\n"
print len(dataUsed_notconverted), "\n"




