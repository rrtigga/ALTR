#stripping out system lines
input_file = open("jacks.txt", "r")
output = open("output.txt", "w")
for i, line in enumerate(input_file):
    if i == 0:
        output.write(line)
    else:
        if not (line.startswith('status') or ("entries" in line) or("password" in line)):
            output.write(line)

filers = []
aggregate=[]
total=[]
used=[]
avail=[]
capacity=[]


input_file = open("output.txt", "r")
#output = open("output.txt", "w")
for i, line in enumerate(input_file):
	if i==0:
		output.write(line)
	if("Filer:" in line):
		temp =[]
		temp = line.split()
		filers.append(temp[1])
		#print "\n"
		#use list comprehension to get 2nd string in filers list
	if ("Aggregate" in line):
		continue
	elif("GB" in line):
		data =[]
		data = line.split()
		aggregate.append(data[0])
		total.append(data[1])
		used.append(data[2])
		avail.append(data[3])
		capacity.append(data[4])
#print results
print filers,"\n"
print aggregate,"\n"
print total,"\n"
print used,"\n"
print avail,"\n"
print capacity,"\n"





		
