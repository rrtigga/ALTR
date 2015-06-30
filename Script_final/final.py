#read input of file
input_file = open("jackfinal.txt", "r")
line_store=[]
start_store=[]

#isilon lists
isilon_site=[]
isilon_dept=[]
isilon_filer=[]
isilon_T1=[]
isilon_T3=[]
isilon_T3B=[]
isilon_T4=[]
isilon_aggr=[]
isilon_total=[]
isilon_used=[]
isilon_avail=[]
isilon_check= False 
isilon_filer_temp=""

#iterate through lines of output
for i, line in enumerate(input_file):
	line_store=line.split()

	#check if isilon
	if(len(line_store)>=1):
		if(( "ISILON" in line_store[0]) and ("START" in line_store[1])):
			isilon_check=True
	if(isilon_check):
		if("Filer:" in line):
			isilon_filer_temp=line_store[1]
		if( ("-ssd_" in line) or ("-ram" in line)):
			if("s200" in line):
				isilon_T1.append(line_store[3])
				isilon_T3.append("0")
				isilon_T3B.append("0")
				isilon_T4.append("0")
			if("n400" in line):
				isilon_T3B.append(line_store[3])
				isilon_T1.append("0")
				isilon_T3.append("0")
				isilon_T4.append("0")
			if("x400" in line):
				isilon_T3.append(line_store[3])
				isilon_T3B.append("0")
				isilon_T1.append("0")
				isilon_T4.append("0")
			if("x200" in line):
				isilon_T3.append(line_store[3])
				isilon_T3B.append("0")
				isilon_T1.append("0")
				isilon_T4.append("0")







