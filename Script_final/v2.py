#date time library
import datetime
from time import strftime
#get time now
now = datetime.datetime.now()

#store the lines of the input file for checking
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
isilon_date=[]
isilon_time=[]
isilon_vendors=[]
isilon_filer_temp=""

edit_is_used=""
edit_is_total=""

#netapp lists
netapp_site=[]
netapp_dept=[]
netapp_filer=[]
netapp_T1=[]
netapp_T3=[]
netapp_T3B=[]
netapp_T4=[]
netapp_aggr=[]
netapp_total=[]
netapp_used=[]
netapp_avail=[]
netapp_date=[]
netapp_time=[]
netapp_vendors=[]
netapp_capacity=[]
netapp_filer_temp=""

edit_net_used=""
edit_net_total=""



def main():
	
	calculate_isilon();
	calculate_netapp();
	output = open("output_file.txt", "w")
	output.write("#Date,Time,Vendor,Site,Dept,filer,T1,T3,T3B,T4,aggr,total,used,avail \n")
	output.write("\n")

	print("#Date,Time,Vendor,Site,Dept,filer,T1,T3,T3B,T4,aggr,total,used,avail \n")
	for i in range(len(netapp_aggr)):
		output.write(str(netapp_date[i])+"," +netapp_time[i]+","+str(netapp_vendors[i])+"," +str(netapp_site[i])+ ","+ str(netapp_dept[i])+ ","+ str(netapp_filer[i])+ ","+str(netapp_T1[i])+ ","+str(netapp_T3[i])+","+ str(netapp_T3B[i])+ ","+str(netapp_T4[i])+","+ str(netapp_aggr[i])+ ","+str(netapp_total[i])+ ","+str(netapp_used[i])+","+ str(netapp_avail[i])+"\n")
		print (str(netapp_date[i])+"," +netapp_time[i]+","+str(netapp_vendors[i])+"," +str(netapp_site[i])+ ","+ str(netapp_dept[i])+ ","+ str(netapp_filer[i])+ ","+str(netapp_T1[i])+ ","+str(netapp_T3[i])+","+ str(netapp_T3B[i])+ ","+str(netapp_T4[i])+","+ str(netapp_aggr[i])+ ","+str(netapp_total[i])+ ","+str(netapp_used[i])+","+ str(netapp_avail[i]))

	output.write("\n")
	output.write("\n")
	output.write("#Date,Time,Vendor,Site,Dept,filer,T1,T3,T3B,T4,aggr,total,used,avail \n")
	output.write("\n")




	for i in range(len(isilon_site)):
		output.write(str(isilon_date[i])+","+isilon_time[i]+","+str(isilon_vendors[i])+","+ str(isilon_site[i])+","+ str(isilon_dept[i])+","+ str(isilon_filer[i])+","+ str(isilon_T1[i])+","+ str(isilon_T3[i])+","+ str(isilon_T3B[i])+","+ str(isilon_T4[i])+","+ str(isilon_aggr[i])+","+ str(isilon_total[i])+","+ str(isilon_used[i])+ ","+str(isilon_avail[i])+"\n")
		print(str(isilon_date[i])+","+isilon_time[i]+","+str(isilon_vendors[i])+","+ str(isilon_site[i])+","+ str(isilon_dept[i])+","+ str(isilon_filer[i])+","+ str(isilon_T1[i])+","+ str(isilon_T3[i])+","+ str(isilon_T3B[i])+","+ str(isilon_T4[i])+","+ str(isilon_aggr[i])+","+ str(isilon_total[i])+","+ str(isilon_used[i])+ ","+str(isilon_avail[i]))


#isilon function

def calculate_isilon():


	isilon_check= False 
	#read input of file
	input_file = open("jackfinal.txt", "r")

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
				isilon_date.append(now.strftime("%Y-%m-%d"))
				isilon_time.append(now.strftime("%H:%M"))
				isilon_vendors.append("isilon")
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
#end isilon function======================================================

#netapp function
def calculate_netapp():
	#netapp here
	input_file = open("jackfinal.txt", "r")

	netapp_check= False 


	for i, line in enumerate(input_file):
		line_store=line.split()

		if(len(line_store)>=1):
			if(( "NETAPP" in line_store[0])):
				netapp_check=True

		if(netapp_check):
			if("Filer:" in line):
				netapp_filer_temp=line_store[1]
			if not ("Filer" in line) or ("Aggregate" in line) or("entries" in line) or("status" in line) or("Permission" in line) or ("NETAPP" in line) or("GLOBAL" in line):
				if("GB" in line) and ("%" in line):
					netapp_filer.append(netapp_filer_temp)
					netapp_aggr.append(line_store[0])
					netapp_total.append(line_store[1])
					netapp_used.append(line_store[2])
					netapp_avail.append(line_store[3])
					netapp_capacity.append(line_store[4])
					netapp_vendors.append("netapp")
					netapp_site.append(netapp_filer_temp[:2])
					netapp_dept.append(netapp_filer_temp[3:])
					netapp_date.append(now.strftime("%Y-%m-%d"))
					netapp_time.append(now.strftime("%H:%M"))

					if(("4000" in line) or ("arch" in line)):
						netapp_T4.append(line_store[2])
						netapp_T1.append("0")
						netapp_T3B.append("0")
						netapp_T3.append("0")
					elif("drn" in line):
						netapp_T3B.append(line_store[2])
						netapp_T1.append("0")
						netapp_T4.append("0")
						netapp_T3.append("0")
					elif("sata" in line):
						netapp_T1.append("0")
						netapp_T3.append(line_store[2])
						netapp_T4.append("0")
						netapp_T3B.append("0")
					elif("sas" in line):
						netapp_T1.append(line_store[2])
						netapp_T3.append("0")
						netapp_T4.append("0")
						netapp_T3B.append("0")
					else:
						netapp_T1.append(line_store[2])
						netapp_T3.append("0")
						netapp_T4.append("0")
						netapp_T3B.append("0")




#end netapp function=======================================================



#call main at the end 
main()