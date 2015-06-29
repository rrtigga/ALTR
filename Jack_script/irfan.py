user_name=[]
convert_GB=[]
temp=[]
mb=[]
new=[]
input_file = open("irfan.txt", "r")

for i, line in enumerate(input_file):
	if("MB" in line):
		temp = line.split()
		mb.append(temp[0])

for i in range(len(mb)):
	convert_GB.append(mb[i][:-2])


for i in range(len(convert_GB)):
	convert_GB[i]= float(convert_GB[i]) * 0.001
	new.append(str(convert_GB[i])+" GB")
	print new[i]



