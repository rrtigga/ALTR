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
temp =[]
filers_row =[]
sites =[]


input_file = open("output.txt", "r")
for i, line in enumerate(input_file):
	if i==0:
		output.write(line)
	if("Filer:" in line):
		temp = line.split()
		filers.append(temp[1])
		#print "\n"
		#use list comprehension to get 2nd string in filers list
	if not(("Aggregate" in line) or ("Filer:" in line)):
		if not line.strip():
			#skip blank lines
			continue
		else:
			filers_row.append(temp[1])
	if("GB" in line):
		data =[]
		data = line.split()
		aggregate.append(data[0])
		total.append(data[1])
		used.append(data[2])
		avail.append(data[3])
		capacity.append(data[4])

#iterate through filers_row and put site in separate list
for i in range(len(filers_row)):
	sites.append(filers_row[i][:2])


#print results
print filers,"\n"
print aggregate,"\n"
print total,"\n"
print used,"\n"
print avail,"\n"
print capacity,"\n"
print filers_row,"\n"
print sites, "\n"

# print len(filers),"\n"
# print len(aggregate),"\n"
# print len(total),"\n"
# print len(used),"\n"
# print len(avail),"\n"
# print len(capacity),"\n"
# print len(filers_row),"\n"







		
