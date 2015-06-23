from prettytable import PrettyTable

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
dept=[]
T1=[]
T3=[]

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

dept_temp =[]
dept_temp = filers_row
#work off filers_row to strip out first 3 characters
dept_temp = [i[3:] for i in dept_temp]

#strip out all numbers in string

for i in range(len(dept_temp)):
	dept.append(dept_temp[i][:5])
#got dept list 


for i in range(len(aggregate)):
	if("sata" in aggregate[i]):
		T1.append("0")
		T3.append(used[i])
	elif("sas" in aggregate[i]):
		T1.append(used[i])
		T3.append("0")
	else:
		T1.append(used[i])
		T3.append("0")


x = PrettyTable(["Site", "Dept", "filer", "T1", "T3", "aggr", "total", "used", "avail", "Pct"])
x.align["Site"] = "l"
x.padding_width = 1 # One space between column edges and contents (default)

for i in range(len(filers_row)):
	x.add_row([sites[i], dept[i],filers_row[i], T1[i], T3[i], aggregate[i], total[i], used[i], avail[i], capacity[i]])
print x











		