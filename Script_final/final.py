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

edit_is_used=""
edit_is_total=""

#netapp_C lists
netapp_C_site=[]
netapp_C_dept=[]
netapp_C_filer=[]
netapp_C_T1=[]
netapp_C_T3=[]
netapp_C_T3B=[]
netapp_C_T4=[]
netapp_C_aggr=[]
netapp_C_total=[]
netapp_C_used=[]
netapp_C_avail=[]
netapp_C_capacity=[]
netapp_C_check= False 
netapp_C_filer_temp=""

edit_net_used=""
edit_net_total=""

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
			#isilon_site.append("sj")
			isilon_dept.append("ice")
			isilon_filer.append(isilon_filer_temp)
			isilon_aggr.append("NULL")
			isilon_site.append(isilon_filer_temp[:2])
			
			total_store =(float(line_store[4][:-1]) *.75)
			used_store =(float(line_store[3][:-1]) *.75)

			last_total = line_store[4][-1:]
			last_used = line_store[3][-1:]

			#strip out last character
			edit_is_total = line_store[4]
			edit_is_used = line_store[3]
			edit_is_total = edit_is_total[:-1]
			edit_is_used = edit_is_used[:-1]

			avil = float(edit_is_total )*.75- float(edit_is_used )*.75

			if("T" in last_total):
				isilon_avail.append(str(avil)+'T')
				isilon_total.append(str(total_store)+'T')
				isilon_used.append(str(used_store) +'T')
			else:
				isilon_avail.append(str(avil)+'G')
				isilon_total.append(str(total_store)+'G')
				isilon_used.append(str(used_store) +'G')

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


		#netapp here 		

	if(len(line_store)>=1):
		if(( "NETAPP" in line_store[0])):
			isilon_check=False
			netapp_C_check=True

	if(netapp_C_check):

		if("Filer:" in line):
			netapp_C_filer_temp=line_store[1]
		if not ("Filer" in line) or ("Aggregate" in line) or("entries" in line) or("status" in line) or("Permission" in line) or ("NETAPP" in line) or("GLOBAL" in line):
			if("GB" in line) and ("%" in line):
				netapp_C_filer.append(netapp_C_filer_temp)
				netapp_C_aggr.append(line_store[0])
				netapp_C_total.append(line_store[1])
				netapp_C_used.append(line_store[2])
				netapp_C_avail.append(line_store[3])
				netapp_C_capacity.append(line_store[4])
				netapp_C_site.append(netapp_C_filer_temp[:2])
				netapp_C_dept.append(netapp_C_filer_temp[3:])

				if(("4000" in line) or ("arch" in line)):
					netapp_C_T4.append(line_store[2])
					netapp_C_T1.append("0")
					netapp_C_T3B.append("0")
					netapp_C_T3.append("0")
				elif("drn" in line):
					netapp_C_T3B.append(line_store[2])
					netapp_C_T1.append("0")
					netapp_C_T4.append("0")
					netapp_C_T3.append("0")
				elif("sata" in line):
					netapp_C_T1.append("0")
					netapp_C_T3.append(line_store[2])
					netapp_C_T4.append("0")
					netapp_C_T3B.append("0")
				elif("sas" in line):
					netapp_C_T1.append(line_store[2])
					netapp_C_T3.append("0")
					netapp_C_T4.append("0")
					netapp_C_T3B.append("0")
				else:
					netapp_C_T1.append(line_store[2])
					netapp_C_T3.append("0")
					netapp_C_T4.append("0")
					netapp_C_T3B.append("0")



print netapp_C_site, "\n"
print netapp_C_dept, "\n"
print netapp_C_filer, "\n"
print netapp_C_T1, "\n"
print netapp_C_T3, "\n"
print netapp_C_T3B, "\n"
print netapp_C_T4, "\n"
print netapp_C_aggr, "\n"
print netapp_C_total, "\n"
print netapp_C_used, "\n"
print netapp_C_avail, "\n"


print isilon_site, "\n"
print isilon_dept, "\n"
print isilon_filer, "\n"
print isilon_T1, "\n"
print isilon_T3, "\n"
print isilon_T3B, "\n"
print isilon_T4, "\n"
print isilon_aggr, "\n"
print isilon_total, "\n"
print isilon_used, "\n"
print isilon_avail, "\n"


print len(netapp_C_site), "\n"
print len(netapp_C_dept), "\n"
print len(netapp_C_filer), "\n"
print len(netapp_C_T1), "\n"
print len(netapp_C_T3), "\n"
print len(netapp_C_T3B), "\n"
print len(netapp_C_T4), "\n"
print len(netapp_C_aggr), "\n"
print len(netapp_C_total), "\n"
print len(netapp_C_used), "\n"
print len(netapp_C_avail), "\n"


print len(isilon_site), "\n"
print len(isilon_dept), "\n"
print len(isilon_filer), "\n"
print len(isilon_T1), "\n"
print len(isilon_T3), "\n"
print len(isilon_T3B), "\n"
print len(isilon_T4), "\n"
print len(isilon_aggr), "\n"
print len(isilon_total), "\n"
print len(isilon_used), "\n"
print len(isilon_avail), "\n"

			


