# remember to pip install PrettyTable
from prettytable import PrettyTable

#remember to  pip install plotly and follow these instructions https://plot.ly/python/getting-started/
import plotly.plotly as py
from plotly.graph_objs import *

from random import randint


#stripping out system lines

input_file = open("jack2.txt", "r")
output = open("output.txt", "w")
for i, line in enumerate(input_file):
    if i == 0:
        output.write(line)
    else:
    	tempish=[]
    	tempish = line.split()
        if not (line.startswith('status') or ("entries" in line) or("password" in line) or ("Health" in line) or ("Throughput" in line) or ("-----" in line)or ("========" in line) ):
            output.write(line)

#column lists
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
T3B=[]
T4=[]

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
	if(("4000" in aggregate[i]) or ("arch" in aggregate[i])):
		T4.append(used[i])
		T1.append("0")
		T3B.append("0")
		T3.append("0")
	elif("drn" in filers_row[i]):
		T3B.append(used[i])
		T1.append("0")
		T4.append("0")
		T3.append("0")
	elif("sata" in aggregate[i]):
		T1.append("0")
		T3.append(used[i])
		T4.append("0")
		T3B.append("0")
	elif("sas" in aggregate[i]):
		T1.append(used[i])
		T3.append("0")
		T4.append("0")
		T3B.append("0")
	else:
		T1.append(used[i])
		T3.append("0")
		T4.append("0")
		T3B.append("0")

#using python library to generate formatted table 
print "\n"
print "NetApp table"

x = PrettyTable(["Site", "Dept", "filer", "T1", "T3","T3B","T4", "aggr", "total", "used", "avail"])
x.align["Site"] = "l"
x.padding_width = 1 # One space between column edges and contents (default)

for i in range(len(filers_row)):
	x.add_row([sites[i], dept[i],filers_row[i], T1[i], T3[i],T3B[i], T4[i],aggregate[i], total[i], used[i], avail[i]])
print x


#2nd part isilon
s_data=[]
s_used =[]
s_size=[]
s_name=[]

s_T3B=[]
s_T1=[]
s_T3=[]



#reading in isilon file
input_file = open("output.txt", "r")

for i, line in enumerate(input_file):
	if not (line.startswith('=') or ("Throughput" in line) or("Health" in line) or ("--" in line)):
            s_data = line.split()
            if (len(s_data)> 8):
            	s_used.append(s_data[6])
            	s_size.append(s_data[7])
            	s_name.append(s_data[0])
            	print s_name


#strip out final character of string
for i in range(len(s_used)):
	s_used[i] = s_used[i][:-1]
	s_size[i] = s_size[i][:-1]

s_used_type=[]
s_size_type=[]

#store last character type in separate type lists
for i in range(len(s_used)):
	#store last character in list
	s_used_type.append(s_used[i][-1:])
	s_size_type.append(s_size[i][-1:])
	#strip out last character
	s_used[i] = s_used[i][:-1]
	s_size[i] = s_size[i][:-1]
	#multiply by .75
	s_used[i] = int(s_used[i]) * .75
	s_size[i] = int(s_size[i]) * .75
	#concatenate 
	s_used[i] = str(s_used[i]) + s_used_type[i]
	s_size[i] = str(s_size[i]) + s_size_type[i]

for i in range(len(s_name)):
	if("s200" in s_name[i]):
		s_T1.append(s_used[i])
		s_T3.append("0")
		s_T3B.append("0")
	elif("n400" in s_name[i]):
		s_T3B.append(s_used[i])
		s_T1.append("0")
		s_T3.append("0")
	elif("x400" in s_name[i]):
		s_T3.append(s_used[i])
		s_T3B.append("0")
		s_T1.append("0")

#print out isilon data
print "\n"

print "Isilon Table \n"
y = PrettyTable(["Name", "T1", "T3", "T3B", "Used", "Size"])
y.align["Site"] = "l"
y.padding_width = 1 # One space between column edges and contents (default)

#for i in range(5):
	#y.add_row([s_name[i], s_T1[i], s_T3[i], s_T3B[i], s_used[i], s_size[i]])
#print y


date=[]
for i in range(len(T1)):
	date.append("6/22")
print date

T_1_NOGB=[]
T_3_NOGB=[]
T_3B_NOGB=[]
T_4NO_NOGB=[]

time_random=[]


for i in range(len(T1)):
	if(T1[i][-2:]=="GB"):
		T_1_NOGB.append(T1[i][:-2])
	else: 
		T_1_NOGB.append(T1[i])
	
	if(T3[i][-2:]=="GB"):
		T_3_NOGB.append(T3[i][:-2])
	else: 
		T_3_NOGB.append(T3[i])

	if(T3B[i][-2:]=="GB"):
		T_3B_NOGB.append(T3B[i][:-2])
	else: 
		T_3B_NOGB.append(T3B[i])

	if(T4[i][-2:]=="GB"):
		T_4NO_NOGB.append(T4[i][:-2])
	else: 
		T_4NO_NOGB.append(T4[i])

	time_random.append(i)

	#print T1[i][-2:]


#plotly stuff below

T_1 = Scatter(
    x=time_random,
    y=T_1_NOGB
)
T_3 = Scatter(
    x=time_random,
    y=T_3_NOGB
)
T_3B = Scatter(
    x=time_random,
    y=T_3B_NOGB
)
T_4 = Scatter(
    x=time_random,
    y=T_4NO_NOGB
)

#data = Data([T_1, T_3,T_3B,T_4])

#unique_url = py.plot(data, filename = 'Graph: T1, T3, T3B, T4')








		
