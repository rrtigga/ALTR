#here are the graph mathplotlib
#from scipy import interp, arange, exp


import numpy
import matplotlib.pyplot as plt
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

#main function
def main():
	#calling isilon function
	calculate_isilon();
	#calling netapp function
	calculate_netapp();
	#opening output for total usage
	output = open("/storage/data/GLOBAL/usage_collection/total_usage.txt", "a")
	output.write("#Date,Time,Vendor,Site,Dept,filer,T1_GB,T3_GB,T3B_GB,T4_GB,aggr,total,used,avail \n")
	output.write("\n")

	#print("#Date,Time,Vendor,Site,Dept,filer,T1_GB,T3_GB,T3B_GB,T4_GB,aggr,total,used,avail \n")
	for i in range(len(netapp_aggr)):
		output.write(str(netapp_date[i])+"," +netapp_time[i]+","+str(netapp_vendors[i])+"," +str(netapp_site[i])+ ","+ str(netapp_dept[i])+ ","+ str(netapp_filer[i])+ ","+str(netapp_T1[i])+ ","+str(netapp_T3[i])+","+ str(netapp_T3B[i])+ ","+str(netapp_T4[i])+","+ str(netapp_aggr[i])+ ","+str(netapp_total[i])+ ","+str(netapp_used[i])+","+ str(netapp_avail[i])+"\n")
		#print netapp table
		#print (str(netapp_date[i])+"," +netapp_time[i]+","+str(netapp_vendors[i])+"," +str(netapp_site[i])+ ","+ str(netapp_dept[i])+ ","+ str(netapp_filer[i])+ ","+str(netapp_T1[i])+ ","+str(netapp_T3[i])+","+ str(netapp_T3B[i])+ ","+str(netapp_T4[i])+","+ str(netapp_aggr[i])+ ","+str(netapp_total[i])+ ","+str(netapp_used[i])+","+ str(netapp_avail[i]))

	for i in range(len(isilon_site)):
		output.write(str(isilon_date[i])+","+isilon_time[i]+","+str(isilon_vendors[i])+","+ str(isilon_site[i])+","+ str(isilon_dept[i])+","+ str(isilon_filer[i])+","+ str(isilon_T1[i])+","+ str(isilon_T3[i])+","+ str(isilon_T3B[i])+","+ str(isilon_T4[i])+","+ str(isilon_aggr[i])+","+ str(isilon_total[i])+","+ str(isilon_used[i])+ ","+str(isilon_avail[i])+"\n")
		#printing isilon table
		#print(str(isilon_date[i])+","+isilon_time[i]+","+str(isilon_vendors[i])+","+ str(isilon_site[i])+","+ str(isilon_dept[i])+","+ str(isilon_filer[i])+","+ str(isilon_T1[i])+","+ str(isilon_T3[i])+","+ str(isilon_T3B[i])+","+ str(isilon_T4[i])+","+ str(isilon_aggr[i])+","+ str(isilon_total[i])+","+ str(isilon_used[i])+ ","+str(isilon_avail[i]))
	output.write("\n")

	#total storage T1 T3 T3B T4 
	#isilon plus netapp
	total_storage=0
	used_storage=0


	for i in range(len(netapp_dept)):
		total_storage+=float(netapp_total[i])
		used_storage+=float(netapp_used[i])
	for i in range(len(isilon_dept)):
		total_storage+=float(isilon_total[i])
		used_storage+=float(isilon_used[i])

	#raw conversion
	raw_all_used=0
	raw_all_total=0
	
	netapp_T1_raw=[]
	netapp_T3_raw=[]
	netapp_T3B_raw=[]
	netapp_T4_raw=[]

	isilon_T1_raw=[]
	isilon_T3_raw=[]
	isilon_T3B_raw=[]
	isilon_T4_raw=[]



	for i in range(len(netapp_dept)):
		netapp_T1_raw.append(float(netapp_T1[i]) /.65)
		netapp_T3_raw.append(float(netapp_T3[i])/.55)
		netapp_T3B_raw.append(float(netapp_T3B[i])/.55)
		netapp_T4_raw.append(float(netapp_T4[i])/.55)

	#print total_storage
	#print used_storage
	total_storageList=[]
	used_storageList =[]
	total_storageList.append(total_storage)
	used_storageList.append(used_storage)


	dept_site=[]
	dept_site = netapp_site+isilon_site

	#getting all the different sites and dpts 
	diff_site = uniq(dept_site)

	diff_dpt = uniq(netapp_dept+isilon_dept)


	#all lists needed for site by tier...it's a lot of lists :P
	sj_T1_used=[]
	sj_T3_used=[]
	sj_T3B_used=[]
	sj_T4_used=[]
	sj_T1_total=[]
	sj_T3_total=[]
	sj_T3B_total=[]
	sj_T4_total=[]

	pg_T1_used=[]
	pg_T3_used=[]
	pg_T3B_used=[]
	pg_T4_used=[]
	pg_T1_total=[]
	pg_T3_total=[]
	pg_T3B_total=[]
	pg_T4_total=[]

	nl_T1_used=[]
	nl_T3_used=[]
	nl_T3B_used=[]
	nl_T4_used=[]
	nl_T1_total=[]
	nl_T3_total=[]
	nl_T3B_total=[]
	nl_T4_total=[]


	uk_T1_used=[]
	uk_T3_used=[]
	uk_T3B_used=[]
	uk_T4_used=[]
	uk_T1_total=[]
	uk_T3_total=[]
	uk_T3B_total=[]
	uk_T4_total=[]

	jp_T1_used=[]
	jp_T3_used=[]
	jp_T3B_used=[]
	jp_T4_used=[]
	jp_T1_total=[]
	jp_T3_total=[]
	jp_T3B_total=[]
	jp_T4_total=[]

	hk_T1_used=[]
	hk_T3_used=[]
	hk_T3B_used=[]
	hk_T4_used=[]
	hk_T1_total=[]
	hk_T3_total=[]
	hk_T3B_total=[]
	hk_T4_total=[]

	to_T1_used=[]
	to_T3_used=[]
	to_T3B_used=[]
	to_T4_used=[]
	to_T1_total=[]
	to_T3_total=[]
	to_T3B_total=[]
	to_T4_total=[]

	at_T1_used=[]
	at_T3_used=[]
	at_T3B_used=[]
	at_T4_used=[]
	at_T1_total=[]
	at_T3_total=[]
	at_T3B_total=[]
	at_T4_total=[]

	#iterate through netapp for site and tier
	for i in range(len(netapp_site)):
		if("sj" in netapp_site[i]):
			sj_T1_used.append(netapp_T1[i])
			sj_T1_total.append(netapp_total[i])
			
			sj_T3_used.append(netapp_T3[i])
			sj_T3_total.append(netapp_total[i])
			
			sj_T3B_used.append(netapp_T3B[i])
			sj_T3B_total.append(netapp_total[i])
			
			sj_T4_used.append(netapp_T4[i])
			sj_T4_total.append(netapp_total[i])

		elif("pg" in netapp_site[i]):
			pg_T1_used.append(netapp_T1[i])
			pg_T1_total.append(netapp_total[i])
			
			pg_T3_used.append(netapp_T3[i])
			pg_T3_total.append(netapp_total[i])
			
			pg_T3B_used.append(netapp_T3B[i])
			pg_T3B_total.append(netapp_total[i])
			
			pg_T4_used.append(netapp_T4[i])
			pg_T4_total.append(netapp_total[i])

		elif("nl" in netapp_site[i]):
			nl_T1_used.append(netapp_T1[i])
			nl_T1_total.append(netapp_total[i])
			
			nl_T3_used.append(netapp_T3[i])
			nl_T3_total.append(netapp_total[i])
			
			nl_T3B_used.append(netapp_T3B[i])
			nl_T3B_total.append(netapp_total[i])
			
			nl_T4_used.append(netapp_T4[i])
			nl_T4_total.append(netapp_total[i])

		elif("uk" in netapp_site[i]):
			uk_T1_used.append(netapp_T1[i])
			uk_T1_total.append(netapp_total[i])
			
			uk_T3_used.append(netapp_T3[i])
			uk_T3_total.append(netapp_total[i])
			
			uk_T3B_used.append(netapp_T3B[i])
			uk_T3B_total.append(netapp_total[i])
			
			uk_T4_used.append(netapp_T4[i])
			uk_T4_total.append(netapp_total[i])

		elif("jp" in netapp_site[i]):
			jp_T1_used.append(netapp_T1[i])
			jp_T1_total.append(netapp_total[i])
			
			jp_T3_used.append(netapp_T3[i])
			jp_T3_total.append(netapp_total[i])
			
			jp_T3B_used.append(netapp_T3B[i])
			jp_T3B_total.append(netapp_total[i])
			
			jp_T4_used.append(netapp_T4[i])
			jp_T4_total.append(netapp_total[i])

		elif("hk" in netapp_site[i]):
			hk_T1_used.append(netapp_T1[i])
			hk_T1_total.append(netapp_total[i])
			
			hk_T3_used.append(netapp_T3[i])
			hk_T3_total.append(netapp_total[i])
			
			hk_T3B_used.append(netapp_T3B[i])
			hk_T3B_total.append(netapp_total[i])
			
			hk_T4_used.append(netapp_T4[i])
			hk_T4_total.append(netapp_total[i])

		elif("to" in netapp_site[i]):
			to_T1_used.append(netapp_T1[i])
			to_T1_total.append(netapp_total[i])
			
			to_T3_used.append(netapp_T3[i])
			to_T3_total.append(netapp_total[i])
			
			to_T3B_used.append(netapp_T3B[i])
			to_T3B_total.append(netapp_total[i])
			
			to_T4_used.append(netapp_T4[i])
			to_T4_total.append(netapp_total[i])

		elif("at" in netapp_site[i]):
			at_T1_used.append(netapp_T1[i])
			at_T1_total.append(netapp_total[i])
			
			at_T3_used.append(netapp_T3[i])
			at_T3_total.append(netapp_total[i])
			
			at_T3B_used.append(netapp_T3B[i])
			at_T3B_total.append(netapp_total[i])
			
			at_T4_used.append(netapp_T4[i])
			at_T4_total.append(netapp_total[i])

		#iterate through isilon for site and tier
	for i in range(len(isilon_site)):
		if("sj" in isilon_site[i]):
			sj_T1_used.append(isilon_T1[i])
			sj_T1_total.append(isilon_total[i])
			
			sj_T3_used.append(isilon_T3[i])
			sj_T3_total.append(isilon_total[i])
			
			sj_T3B_used.append(isilon_T3B[i])
			sj_T3B_total.append(isilon_total[i])
			
			sj_T4_used.append(isilon_T4[i])
			sj_T4_total.append(isilon_total[i])

		elif("pg" in isilon_site[i]):
			pg_T1_used.append(isilon_T1[i])
			pg_T1_total.append(isilon_total[i])
			
			pg_T3_used.append(isilon_T3[i])
			pg_T3_total.append(isilon_total[i])
			
			pg_T3B_used.append(isilon_T3B[i])
			pg_T3B_total.append(isilon_total[i])
			
			pg_T4_used.append(isilon_T4[i])
			pg_T4_total.append(isilon_total[i])

		elif("nl" in isilon_site[i]):
			nl_T1_used.append(isilon_T1[i])
			nl_T1_total.append(isilon_total[i])
			
			nl_T3_used.append(isilon_T3[i])
			nl_T3_total.append(isilon_total[i])
			
			nl_T3B_used.append(isilon_T3B[i])
			nl_T3B_total.append(isilon_total[i])
			
			nl_T4_used.append(isilon_T4[i])
			nl_T4_total.append(isilon_total[i])

		elif("uk" in isilon_site[i]):
			uk_T1_used.append(isilon_T1[i])
			uk_T1_total.append(isilon_total[i])
			
			uk_T3_used.append(isilon_T3[i])
			uk_T3_total.append(isilon_total[i])
			
			uk_T3B_used.append(isilon_T3B[i])
			uk_T3B_total.append(isilon_total[i])
			
			uk_T4_used.append(isilon_T4[i])
			uk_T4_total.append(isilon_total[i])

		elif("jp" in isilon_site[i]):
			jp_T1_used.append(isilon_T1[i])
			jp_T1_total.append(isilon_total[i])
			
			jp_T3_used.append(isilon_T3[i])
			jp_T3_total.append(isilon_total[i])
			
			jp_T3B_used.append(isilon_T3B[i])
			jp_T3B_total.append(isilon_total[i])
			
			jp_T4_used.append(isilon_T4[i])
			jp_T4_total.append(isilon_total[i])

		elif("hk" in isilon_site[i]):
			hk_T1_used.append(isilon_T1[i])
			hk_T1_total.append(isilon_total[i])
			
			hk_T3_used.append(isilon_T3[i])
			hk_T3_total.append(isilon_total[i])
			
			hk_T3B_used.append(isilon_T3B[i])
			hk_T3B_total.append(isilon_total[i])
			
			hk_T4_used.append(isilon_T4[i])
			hk_T4_total.append(isilon_total[i])

		elif("to" in isilon_site[i]):
			to_T1_used.append(isilon_T1[i])
			to_T1_total.append(isilon_total[i])
			
			to_T3_used.append(isilon_T3[i])
			to_T3_total.append(isilon_total[i])
			
			to_T3B_used.append(isilon_T3B[i])
			to_T3B_total.append(isilon_total[i])
			
			to_T4_used.append(isilon_T4[i])
			to_T4_total.append(isilon_total[i])

		elif("at" in isilon_site[i]):
			at_T1_used.append(isilon_T1[i])
			at_T1_total.append(isilon_total[i])
			
			at_T3_used.append(isilon_T3[i])
			at_T3_total.append(isilon_total[i])
			
			at_T3B_used.append(isilon_T3B[i])
			at_T3B_total.append(isilon_total[i])
			
			at_T4_used.append(isilon_T4[i])
			at_T4_total.append(isilon_total[i])

	#department and tiers lists
	ice_T1_used=[]
	ice_T3_used=[]
	ice_T3B_used=[]
	ice_T4_used=[]
	ice_T1_total=[]
	ice_T3_total=[]
	ice_T3B_total=[]
	ice_T4_total=[]

	swip_T1_used=[]
	swip_T3_used=[]
	swip_T3B_used=[]
	swip_T4_used=[]
	swip_T1_total=[]
	swip_T3_total=[]
	swip_T3B_total=[]
	swip_T4_total=[]

	it_T1_used=[]
	it_T3_used=[]
	it_T3B_used=[]
	it_T4_used=[]
	it_T1_total=[]
	it_T3_total=[]
	it_T3B_total=[]
	it_T4_total=[]

	wwoe_T1_used=[]
	wwoe_T3_used=[]
	wwoe_T3B_used=[]
	wwoe_T4_used=[]
	wwoe_T1_total=[]
	wwoe_T3_total=[]
	wwoe_T3B_total=[]
	wwoe_T4_total=[]


	#getting the appropriate tier values for department tiers 
	for i in range(len(netapp_dept)):
		if(("itnas01a" in netapp_dept[i]) or ("itnas01b" in netapp_dept[i])):
			ice_T1_used.append(netapp_T1[i])
			ice_T3_used.append(netapp_T3[i])
			ice_T3B_used.append(netapp_T3B[i])
			ice_T4_used.append(netapp_T4[i])

			ice_T1_total.append(netapp_total[i])
			ice_T3_total.append(netapp_total[i])
			ice_T3B_total.append(netapp_total[i])
			ice_T4_total.append(netapp_total[i])

		elif(("swnas01a" in netapp_dept[i]) or ("swnas01b" in netapp_dept[i])):
			swip_T1_used.append(netapp_T1[i])
			swip_T3_used.append(netapp_T3[i])
			swip_T3B_used.append(netapp_T3B[i])
			swip_T4_used.append(netapp_T4[i])

			swip_T1_total.append(netapp_total[i])
			swip_T3_total.append(netapp_total[i])
			swip_T3B_total.append(netapp_total[i])
			swip_T4_total.append(netapp_total[i])

		elif(("itcrncnas01" in netapp_dept[i])):
			it_T1_used.append(netapp_T1[i])
			it_T3_used.append(netapp_T3[i])
			it_T3B_used.append(netapp_T3B[i])
			it_T4_used.append(netapp_T4[i])

			it_T1_total.append(netapp_total[i])
			it_T3_total.append(netapp_total[i])
			it_T3B_total.append(netapp_total[i])
			it_T4_total.append(netapp_total[i])

		elif(("engnas03a" in netapp_dept[i]) or ("engnas03b" in netapp_dept[i])):
			wwoe_T1_used.append(netapp_T1[i])
			wwoe_T3_used.append(netapp_T3[i])
			wwoe_T3B_used.append(netapp_T3B[i])
			wwoe_T4_used.append(netapp_T4[i])

			wwoe_T1_total.append(netapp_total[i])
			wwoe_T3_total.append(netapp_total[i])
			wwoe_T3B_total.append(netapp_total[i])
			wwoe_T4_total.append(netapp_total[i])


	for i in range(len(isilon_dept)):
		if(("itnas01a" in isilon_dept[i]) or ("itnas01b" in isilon_dept[i])):
			ice_T1_used.append(isilon_T1[i])
			ice_T3_used.append(isilon_T3[i])
			ice_T3B_used.append(isilon_T3B[i])
			ice_T4_used.append(isilon_T4[i])

			ice_T1_total.append(isilon_total[i])
			ice_T3_total.append(isilon_total[i])
			ice_T3B_total.append(isilon_total[i])
			ice_T4_total.append(isilon_total[i])

		elif(("swnas01a" in isilon_dept[i]) or ("swnas01b" in isilon_dept[i])):
			swip_T1_used.append(isilon_T1[i])
			swip_T3_used.append(isilon_T3[i])
			swip_T3B_used.append(isilon_T3B[i])
			swip_T4_used.append(isilon_T4[i])

			swip_T1_total.append(isilon_total[i])
			swip_T3_total.append(isilon_total[i])
			swip_T3B_total.append(isilon_total[i])
			swip_T4_total.append(isilon_total[i])

		elif(("itcrncnas01" in isilon_dept[i])):
			it_T1_used.append(isilon_T1[i])
			it_T3_used.append(isilon_T3[i])
			it_T3B_used.append(isilon_T3B[i])
			it_T4_used.append(isilon_T4[i])

			it_T1_total.append(isilon_total[i])
			it_T3_total.append(isilon_total[i])
			it_T3B_total.append(isilon_total[i])
			it_T4_total.append(isilon_total[i])

		elif(("engnas03a" in isilon_dept[i]) or ("engnas03b" in isilon_dept[i])):
			wwoe_T1_used.append(isilon_T1[i])
			wwoe_T3_used.append(isilon_T3[i])
			wwoe_T3B_used.append(isilon_T3B[i])
			wwoe_T4_used.append(isilon_T4[i])

			wwoe_T1_total.append(isilon_total[i])
			wwoe_T3_total.append(isilon_total[i])
			wwoe_T3B_total.append(isilon_total[i])
			wwoe_T4_total.append(isilon_total[i])





	#create department site file to append total usage
	output = open("dept_site_usage1.txt", "a")

	output.write("#Departments\n")
	output.write("#Date, Time, T1_used, T1_total,T3_used, T3_total,T3B_used, T3B_total,T4_used, T4_total\n")

	output.write("#SJ\n")
	output.write(now.strftime("%m-%d-%Y")+","+now.strftime("%H:%M")+","+ str(sum(convertFloat(sj_T1_used)))+"," + str(sum(convertFloat(sj_T1_total))) +"," +str(sum(convertFloat(sj_T3_used)))+"," + str(sum(convertFloat(sj_T3_total)))+"," +str(sum(convertFloat(sj_T3B_used)))+"," + str(sum(convertFloat(sj_T3B_total)))+"," +str(sum(convertFloat(sj_T4_used)))+"," + str(sum(convertFloat(sj_T4_total))))
	output.write("\n")
	output.write("\n")


	output.write("#pg\n")
	output.write(now.strftime("%m-%d-%Y")+","+now.strftime("%H:%M")+","+ str(sum(convertFloat(pg_T1_used))) +"," +str(sum(convertFloat(pg_T1_total)))+"," +str(sum(convertFloat(pg_T3_used)))+"," + str(sum(convertFloat(pg_T3_total)))+"," +str(sum(convertFloat(pg_T3B_used)))+"," + str(sum(convertFloat(pg_T3B_total)))+"," +str(sum(convertFloat(pg_T4_used)))+"," + str(sum(convertFloat(pg_T4_total))))
	output.write("\n")
	output.write("\n")

	output.write("#nl\n")
	output.write(now.strftime("%m-%d-%Y")+","+now.strftime("%H:%M")+","+ str(sum(convertFloat(nl_T1_used))) +"," +str(sum(convertFloat(nl_T1_total)))+"," +str(sum(convertFloat(nl_T3_used)))+"," + str(sum(convertFloat(nl_T3_total)))+"," +str(sum(convertFloat(nl_T3B_used))) +"," +str(sum(convertFloat(nl_T3B_total)))+"," +str(sum(convertFloat(nl_T4_used))) +"," +str(sum(convertFloat(nl_T4_total))))
	output.write("\n")
	output.write("\n")

	output.write("#uk\n")
	output.write(now.strftime("%m-%d-%Y")+","+now.strftime("%H:%M")+","+ str(sum(convertFloat(uk_T1_used)))+"," + str(sum(convertFloat(uk_T1_total)))+"," +str(sum(convertFloat(uk_T3_used)))+"," + str(sum(convertFloat(uk_T3_total)))+"," +str(sum(convertFloat(uk_T3B_used))) +"," +str(sum(convertFloat(uk_T3B_total)))+"," +str(sum(convertFloat(uk_T4_used)) )+"," +str(sum(convertFloat(uk_T4_total))))
	output.write("\n")
	output.write("\n")

	output.write("#jp\n")
	output.write(now.strftime("%m-%d-%Y")+","+now.strftime("%H:%M")+","+ str(sum(convertFloat(jp_T1_used))) +"," +str(sum(convertFloat(jp_T1_total)))+"," +str(sum(convertFloat(jp_T3_used))) +"," +str(sum(convertFloat(jp_T3_total)))+"," +str(sum(convertFloat(jp_T3B_used))) +"," +str(sum(convertFloat(jp_T3B_total)))+"," +str(sum(convertFloat(jp_T4_used))) +"," +str(sum(convertFloat(jp_T4_total))))
	output.write("\n")
	output.write("\n")

	output.write("#hk\n")
	output.write(now.strftime("%m-%d-%Y")+","+now.strftime("%H:%M")+","+ str(sum(convertFloat(hk_T1_used))) +"," +str(sum(convertFloat(hk_T1_total)))+"," +str(sum(convertFloat(hk_T3_used))) +"," +str(sum(convertFloat(hk_T3_total)))+"," +str(sum(convertFloat(hk_T3B_used))) +"," +str(sum(convertFloat(hk_T3B_total)))+"," +str(sum(convertFloat(hk_T4_used)))+"," + str(sum(convertFloat(hk_T4_total))))
	output.write("\n")
	output.write("\n")

	output.write("#to\n")
	output.write(now.strftime("%m-%d-%Y")+","+now.strftime("%H:%M")+","+ str(sum(convertFloat(to_T1_used)))+"," + str(sum(convertFloat(to_T1_total)))+"," +str(sum(convertFloat(to_T3_used)))+"," + str(sum(convertFloat(to_T3_total)))+"," + str(sum(convertFloat(to_T3B_used)))+"," + str(sum(convertFloat(to_T3B_total)))+"," +str(sum(convertFloat(to_T4_used)))+"," + str(sum(convertFloat(to_T4_total))))
	output.write("\n")
	output.write("\n")

	output.write("#at\n")
	output.write(now.strftime("%m-%d-%Y")+","+now.strftime("%H:%M")+","+ str(sum(convertFloat(at_T1_used)))+"," + str(sum(convertFloat(at_T1_total)))+"," + str(sum(convertFloat(at_T3_used)))+"," + str(sum(convertFloat(at_T3_total)))+"," + str(sum(convertFloat(at_T3B_used)))+"," + str(sum(convertFloat(at_T3B_total)))+"," + str(sum(convertFloat(at_T4_used)))+"," + str(sum(convertFloat(at_T4_total))))
	output.write("\n")
	output.write("\n")

	output.write("\n")
	output.write("\n")
	output.write("\n")
	output.write("#Sites\n")
	output.write("#Date, Time, T1_used, T1_total,T3_used, T3_total,T3B_used, T3B_total,T4_used, T4_total\n")

	output.write("\n")
	output.write("#ICE\n")
	output.write(now.strftime("%m-%d-%Y")+","+now.strftime("%H:%M")+","+ str(sum(convertFloat(ice_T1_used)))+"," +  str(sum(convertFloat(ice_T1_total)))+"," + str(sum(convertFloat(ice_T3_used)))+"," + str(sum(convertFloat(ice_T3_total)))+"," + str(sum(convertFloat(ice_T3B_used)))+"," + str(sum(convertFloat(ice_T3B_total)))+"," + str(sum(convertFloat(ice_T4_used)))+"," + str(sum(convertFloat(ice_T4_total))))
	output.write("\n")
	output.write("\n")

	output.write("#SWIP\n")
	output.write(now.strftime("%m-%d-%Y")+","+now.strftime("%H:%M")+","+  str(sum(convertFloat(swip_T1_used)))+"," +  str(sum(convertFloat(swip_T1_total)))+"," + str(sum(convertFloat(swip_T3_used)))+"," + str(sum(convertFloat(swip_T3_total)))+"," + str(sum(convertFloat(swip_T3B_used)))+"," +  str(sum(convertFloat(swip_T3B_total)))+"," + str(sum(convertFloat(swip_T4_used)))+"," +  str(sum(convertFloat(swip_T4_total))))
	output.write("\n")
	output.write("\n")

	output.write("#IT\n")
	output.write(now.strftime("%m-%d-%Y")+","+now.strftime("%H:%M")+","+  str(sum(convertFloat(it_T1_used)))+"," +  str(sum(convertFloat(it_T1_total))) +"," +str(sum(convertFloat(it_T3_used)))+"," +  str(sum(convertFloat(it_T3_total)))+"," + str(sum(convertFloat(it_T3B_used)))+"," + str(sum(convertFloat(it_T3B_total)))+"," + str(sum(convertFloat(it_T4_used)))+"," + str(sum(convertFloat(it_T4_total))))
	output.write("\n")
	output.write("\n")

	output.write("#WWOE\n")
	output.write(now.strftime("%m-%d-%Y")+","+now.strftime("%H:%M")+","+ str(sum(convertFloat(wwoe_T1_used)))+"," + str(sum(convertFloat(wwoe_T1_total)))+"," + str(sum(convertFloat(wwoe_T3_used)))+"," +  str(sum(convertFloat(wwoe_T3_total)))+"," + str(sum(convertFloat(wwoe_T3B_used)))+"," + str(sum(convertFloat(wwoe_T3B_total)))+"," + str(sum(convertFloat(wwoe_T4_used)))+"," + str(sum(convertFloat(wwoe_T4_total))))
	output.write("\n")
	output.write("\n")



	#opening the total usage file to get the total usages dates 
	try:
		#open input file
	output = open("/storage/data/GLOBAL/usage_collection/dept_site_usage.txt", "a")
	except:
		#if file can't be read, exit
		print "Could not read file:", input_file
   		sys.exit()

   	total_usage_date_store=[]

	#iterate through lines of output
	#get the number of dates and different dates in order to generate the graphs

	for i, line in enumerate(input_file):
		if(line =='\n'):
			continue
		else:
			if not('#' in line):
				line_store=line.split(",")
				total_usage_date_store.append(line_store[0])

	unique_dates= uniq(total_usage_date_store)


	dept_site_usage_date_store=[]
	
	try:
		#open input file
		input_file = open("/storage/data/GLOBAL/storage_data.txt", "r")
	except:
		#if file can't be read, exit
		print "Could not read file:", input_file
   		sys.exit()

   	#iterate through lines of output of dept_site_usage text files
	#get the number of dates and different dates in order to generate the graphs
	for i, line in enumerate(input_file):
		if(line =='\n'):
			continue
		else:
			if not('#' in line):
				line_store=line.split(",")
				dept_site_usage_date_store.append(line_store[0])

	

	
	#get the number of dates and different dates in order to generate the graphs

	total_storage_graphs=[0]*len(unique_dates)
	used_storage_graphs=[0]*len(unique_dates)

	#raw lists
	netapp_T1_raw_graphs=[0]*len(unique_dates)
	netapp_T3_raw_graphs=[0]*len(unique_dates)
	netapp_T3B_raw_graphs=[0]*len(unique_dates)
	netapp_T4_raw_graphs=[0]*len(unique_dates)


	#all lists needed for site by tier...it's a lot of lists :P
	sj_T1_used_graphs=[0]*len(unique_dates)
	sj_T3_used_graphs=[0]*len(unique_dates)
	sj_T3B_used_graphs=[0]*len(unique_dates)
	sj_T4_used_graphs=[0]*len(unique_dates)
	sj_T1_total_graphs=[0]*len(unique_dates)
	sj_T3_total_graphs=[0]*len(unique_dates)
	sj_T3B_total_graphs=[0]*len(unique_dates)
	sj_T4_total_graphs=[0]*len(unique_dates)

	pg_T1_used_graphs=[0]*len(unique_dates)
	pg_T3_used_graphs=[0]*len(unique_dates)
	pg_T3B_used_graphs=[0]*len(unique_dates)
	pg_T4_used_graphs=[0]*len(unique_dates)
	pg_T1_total_graphs=[0]*len(unique_dates)
	pg_T3_total_graphs=[0]*len(unique_dates)
	pg_T3B_total_graphs=[0]*len(unique_dates)
	pg_T4_total_graphs=[0]*len(unique_dates)

	nl_T1_used_graphs=[0]*len(unique_dates)
	nl_T3_used_graphs=[0]*len(unique_dates)
	nl_T3B_used_graphs=[0]*len(unique_dates)
	nl_T4_used_graphs=[0]*len(unique_dates)
	nl_T1_total_graphs=[0]*len(unique_dates)
	nl_T3_total_graphs=[0]*len(unique_dates)
	nl_T3B_total_graphs=[0]*len(unique_dates)
	nl_T4_total_graphs=[0]*len(unique_dates)


	uk_T1_used_graphs=[0]*len(unique_dates)
	uk_T3_used_graphs=[0]*len(unique_dates)
	uk_T3B_used_graphs=[0]*len(unique_dates)
	uk_T4_used_graphs=[0]*len(unique_dates)
	uk_T1_total_graphs=[0]*len(unique_dates)
	uk_T3_total_graphs=[0]*len(unique_dates)
	uk_T3B_total_graphs=[0]*len(unique_dates)
	uk_T4_total_graphs=[0]*len(unique_dates)

	jp_T1_used_graphs=[0]*len(unique_dates)
	jp_T3_used_graphs=[0]*len(unique_dates)
	jp_T3B_used_graphs=[0]*len(unique_dates)
	jp_T4_used_graphs=[0]*len(unique_dates)
	jp_T1_total_graphs=[0]*len(unique_dates)
	jp_T3_total_graphs=[0]*len(unique_dates)
	jp_T3B_total_graphs=[0]*len(unique_dates)
	jp_T4_total_graphs=[0]*len(unique_dates)

	hk_T1_used_graphs=[0]*len(unique_dates)
	hk_T3_used_graphs=[0]*len(unique_dates)
	hk_T3B_used_graphs=[0]*len(unique_dates)
	hk_T4_used_graphs=[0]*len(unique_dates)
	hk_T1_total_graphs=[0]*len(unique_dates)
	hk_T3_total_graphs=[0]*len(unique_dates)
	hk_T3B_total_graphs=[0]*len(unique_dates)
	hk_T4_total_graphs=[0]*len(unique_dates)

	to_T1_used_graphs=[0]*len(unique_dates)
	to_T3_used_graphs=[0]*len(unique_dates)
	to_T3B_used_graphs=[0]*len(unique_dates)
	to_T4_used_graphs=[0]*len(unique_dates)
	to_T1_total_graphs=[0]*len(unique_dates)
	to_T3_total_graphs=[0]*len(unique_dates)
	to_T3B_total_graphs=[0]*len(unique_dates)
	to_T4_total_graphs=[0]*len(unique_dates)

	at_T1_used_graphs=[0]*len(unique_dates)
	at_T3_used_graphs=[0]*len(unique_dates)
	at_T3B_used_graphs=[0]*len(unique_dates)
	at_T4_used_graphs=[0]*len(unique_dates)
	at_T1_total_graphs=[0]*len(unique_dates)
	at_T3_total_graphs=[0]*len(unique_dates)
	at_T3B_total_graphs=[0]*len(unique_dates)
	at_T4_total_graphs=[0]*len(unique_dates)




	#all lists of dpts 
	#department and tiers lists
	ice_T1_used_graphs=[0]*len(unique_dates)
	ice_T3_used_graphs=[0]*len(unique_dates)
	ice_T3B_used_graphs=[0]*len(unique_dates)
	ice_T4_used_graphs=[0]*len(unique_dates)
	ice_T1_total_graphs=[0]*len(unique_dates)
	ice_T3_total_graphs=[0]*len(unique_dates)
	ice_T3B_total_graphs=[0]*len(unique_dates)
	ice_T4_total_graphs=[0]*len(unique_dates)

	swip_T1_used_graphs=[0]*len(unique_dates)
	swip_T3_used_graphs=[0]*len(unique_dates)
	swip_T3B_used_graphs=[0]*len(unique_dates)
	swip_T4_used_graphs=[0]*len(unique_dates)
	swip_T1_total_graphs=[0]*len(unique_dates)
	swip_T3_total_graphs=[0]*len(unique_dates)
	swip_T3B_total_graphs=[0]*len(unique_dates)
	swip_T4_total_graphs=[0]*len(unique_dates)

	it_T1_used_graphs=[0]*len(unique_dates)
	it_T3_used_graphs=[0]*len(unique_dates)
	it_T3B_used_graphs=[0]*len(unique_dates)
	it_T4_used_graphs=[0]*len(unique_dates)
	it_T1_total_graphs=[0]*len(unique_dates)
	it_T3_total_graphs=[0]*len(unique_dates)
	it_T3B_total_graphs=[0]*len(unique_dates)
	it_T4_total_graphs=[0]*len(unique_dates)

	wwoe_T1_used_graphs=[0]*len(unique_dates)
	wwoe_T3_used_graphs=[0]*len(unique_dates)
	wwoe_T3B_used_graphs=[0]*len(unique_dates)
	wwoe_T4_used_graphs=[0]*len(unique_dates)
	wwoe_T1_total_graphs=[0]*len(unique_dates)
	wwoe_T3_total_graphs=[0]*len(unique_dates)
	wwoe_T3B_total_graphs=[0]*len(unique_dates)
	wwoe_T4_total_graphs=[0]*len(unique_dates)



	for j in range(len(unique_dates)):
		
		try:
		#open input file
		input_file = open("/storage/data/GLOBAL/storage_data.txt", "r")
		except:
			#if file can't be read, exit
			print "Could not read file:", input_file
   			sys.exit()
		
		for i, line in enumerate(input_file):
			if(line =='\n'):
				continue
			if("#" in line):
				continue
			else:
				#adding the proper total storage and used storage in correspondence with the dates
				line_store = line.split(",")
				if(unique_dates[j] in line):


					#plot 1 
					total_storage_graphs[j]+=float(line_store[11])
					used_storage_graphs[j]+=float(line_store[12])

					#plot 2
					netapp_T1_raw_graphs[j]+=float(line_store[6])
					netapp_T3_raw_graphs[j]+=float(line_store[7])
					netapp_T3B_raw_graphs[j]+=float(line_store[8])
					netapp_T4_raw_graphs[j]+=float(line_store[9])


					#plot 3-10
					if("sj" in line_store[3]):
						sj_T1_used_graphs[j]+=float(line_store[6])
						sj_T1_total_graphs[j]+=float(line_store[11])
						sj_T3_total_graphs[j]+=float(line_store[7])
						
						sj_T3_total_graphs[j]+=float(line_store[11])
						
						sj_T3B_used_graphs[j]+=float(line_store[8])
						sj_T3B_total_graphs[j]+=float(line_store[11])
						
						sj_T4_used_graphs[j]+=float(line_store[9])
						sj_T4_total_graphs[j]+=float(line_store[11])

					elif("pg" in line_store[3]):
						pg_T1_used_graphs[j]+=float(line_store[6])
						pg_T1_total_graphs[j]+=float(line_store[11])
						
						pg_T3_used_graphs[j]+=float(line_store[7])
						pg_T3_total_graphs[j]+=float(line_store[11])
						
						pg_T3B_used_graphs[j]+=float(line_store[8])
						pg_T3B_total_graphs[j]+=float(line_store[11])
						
						pg_T4_used_graphs[j]+=float(line_store[9])
						pg_T4_total_graphs[j]+=float(line_store[11])

					elif("nl" in line_store[3]):
						nl_T1_used_graphs[j]+=float(line_store[6])
						nl_T1_total_graphs[j]+=float(line_store[11])
						
						nl_T3_used_graphs[j]+=float(line_store[7])
						nl_T3_total_graphs[j]+=float(line_store[11])
						
						nl_T3B_used_graphs[j]+=float(line_store[8])
						nl_T3B_total_graphs[j]+=float(line_store[11])
						
						nl_T4_used_graphs[j]+=float(line_store[9])
						nl_T4_total_graphs[j]+=float(line_store[11])

					elif("uk" in line_store[3]):
						uk_T1_used_graphs[j]+=float(line_store[6])
						uk_T1_total_graphs[j]+=float(line_store[11])
						
						uk_T3_used_graphs[j]+=float(line_store[7])
						uk_T3_total_graphs[j]+=float(line_store[11])
						
						uk_T3B_used_graphs[j]+=float(line_store[8])
						uk_T3B_total_graphs[j]+=float(line_store[11])
						
						uk_T4_used_graphs[j]+=float(line_store[9])
						uk_T4_total_graphs[j]+=float(line_store[11])

					elif("jp" in line_store[3]):
						jp_T1_used_graphs[j]+=float(line_store[6])
						jp_T1_total_graphs[j]+=float(line_store[11])
						
						jp_T3_used_graphs[j]+=float(line_store[7])
						jp_T3_total_graphs[j]+=float(line_store[11])
						
						jp_T3B_used_graphs[j]+=float(line_store[8])
						jp_T3B_total_graphs[j]+=float(line_store[11])
						
						jp_T4_used_graphs[j]+=float(line_store[9])
						jp_T4_total_graphs[j]+=float(line_store[11])

					elif("hk" in line_store[3]):
						hk_T1_used_graphs[j]+=float(line_store[6])
						hk_T1_total_graphs[j]+=float(line_store[11])
						
						hk_T3_used_graphs[j]+=float(line_store[7])
						hk_T3_total_graphs[j]+=float(line_store[11])
						
						hk_T3B_used_graphs[j]+=float(line_store[8])
						hk_T3B_total_graphs[j]+=float(line_store[11])
						
						hk_T4_used_graphs[j]+=float(line_store[9])
						hk_T4_total_graphs[j]+=float(line_store[11])

					elif("to" in line_store[3]):
						to_T1_used_graphs[j]+=float(line_store[6])
						to_T1_total_graphs[j]+=float(line_store[11])
						
						to_T3_used_graphs[j]+=float(line_store[7])
						to_T3_total_graphs[j]+=float(line_store[11])
						
						to_T3B_used_graphs[j]+=float(line_store[8])
						to_T3B_total_graphs[j]+=float(line_store[11])
						
						to_T4_used_graphs[j]+=float(line_store[9])
						to_T4_total_graphs[j]+=float(line_store[11])

					elif("at" in line_store[3]):
						at_T1_used_graphs[j]+=float(line_store[6])
						at_T1_total_graphs[j]+=float(line_store[11])
						
						at_T3_used_graphs[j]+=float(line_store[7])
						at_T3_total_graphs[j]+=float(line_store[11])
						
						at_T3B_used_graphs[j]+=float(line_store[8])
						at_T3B_total_graphs[j]+=float(line_store[11])
						
						at_T4_used_graphs[j]+=float(line_store[9])
						at_T4_total_graphs[j]+=float(line_store[11])

					#iterate through isilon for site and tier
					if("sj" in line_store[3]):
						sj_T1_used_graphs[j]+=float(line_store[6])
						sj_T1_total_graphs[j]+=float(line_store[11])
						
						sj_T3_used_graphs[j]+=float(line_store[7])
						sj_T3_total_graphs[j]+=float(line_store[11])
						
						sj_T3B_used_graphs[j]+=float(line_store[8])
						sj_T3B_total_graphs[j]+=float(line_store[11])
						
						sj_T4_used_graphs[j]+=float(line_store[9])
						sj_T4_total_graphs[j]+=float(line_store[11])

					elif("pg" in line_store[3]):
						pg_T1_used_graphs[j]+=float(line_store[6])
						pg_T1_total_graphs[j]+=float(line_store[11])
						
						pg_T3_used_graphs[j]+=float(line_store[7])
						pg_T3_total_graphs[j]+=float(line_store[11])
						
						pg_T3B_used_graphs[j]+=float(line_store[8])
						pg_T3B_total_graphs[j]+=float(line_store[11])
						
						pg_T4_used_graphs[j]+=float(line_store[9])
						pg_T4_total_graphs[j]+=float(line_store[11])

					elif("nl" in line_store[3]):
						nl_T1_used_graphs[j]+=float(line_store[6])
						nl_T1_total_graphs[j]+=float(line_store[11])
						
						nl_T3_used_graphs[j]+=float(line_store[7])
						nl_T3_total_graphs[j]+=float(line_store[11])
						
						nl_T3B_used_graphs[j]+=float(line_store[8])
						nl_T3B_total_graphs[j]+=float(line_store[11])
						
						nl_T4_used_graphs[j]+=float(line_store[9])
						nl_T4_total_graphs[j]+=float(line_store[11])

					elif("uk" in line_store[3]):
						uk_T1_used_graphs[j]+=float(line_store[6])
						uk_T1_total_graphs[j]+=float(line_store[11])
						
						uk_T3_used_graphs[j]+=float(line_store[7])
						uk_T3_total_graphs[j]+=float(line_store[11])
						
						uk_T3B_used_graphs[j]+=float(line_store[8])
						uk_T3B_total_graphs[j]+=float(line_store[11])
						
						uk_T4_used_graphs[j]+=float(line_store[9])
						uk_T4_total_graphs[j]+=float(line_store[11])

					elif("jp" in line_store[3]):
						jp_T1_used_graphs[j]+=float(line_store[6])
						jp_T1_total_graphs[j]+=float(line_store[11])
						
						jp_T3_used_graphs[j]+=float(line_store[7])
						jp_T3_total_graphs[j]+=float(line_store[11])
						
						jp_T3B_used_graphs[j]+=float(line_store[8])
						jp_T3B_total_graphs[j]+=float(line_store[11])
						
						jp_T4_used_graphs[j]+=float(line_store[9])
						jp_T4_total_graphs[j]+=float(line_store[11])

					elif("hk" in line_store[3]):
						hk_T1_used_graphs[j]+=float(line_store[6])
						hk_T1_total_graphs[j]+=float(line_store[11])
						
						hk_T3_used_graphs[j]+=float(line_store[7])
						hk_T3_total_graphs[j]+=float(line_store[11])
						
						hk_T3B_used_graphs[j]+=float(line_store[8])
						hk_T3B_total_graphs[j]+=float(line_store[11])
						
						hk_T4_used_graphs[j]+=float(line_store[9])
						hk_T4_total_graphs[j]+=float(line_store[11])

					elif("to" in line_store[3]):

						to_T1_used_graphs[j]+=float(line_store[6])
						to_T1_total_graphs[j]+=float(line_store[11])
						
						to_T3_used_graphs[j]+=float(line_store[7])
						to_T3_total_graphs[j]+=float(line_store[11])
						
						to_T3B_used_graphs[j]+=float(line_store[8])
						to_T3B_total_graphs[j]+=float(line_store[11])
						
						to_T4_used_graphs[j]+=float(line_store[9])
						to_T4_total_graphs[j]+=float(line_store[11])

					elif("at" in line_store[3]):
						at_T1_used_graphs[j]+=float(line_store[6])
						at_T1_total_graphs[j]+=float(line_store[11])
						
						at_T3_used_graphs[j]+=float(line_store[7])
						at_T3_total_graphs[j]+=float(line_store[11])
						
						at_T3B_used_graphs[j]+=float(line_store[8])
						at_T3B_total_graphs[j]+=float(line_store[11])
						
						at_T4_used_graphs[j]+=float(line_store[9])
						at_T4_total_graphs[j]+=float(line_store[11])




					#here are the checks for dpts
					#plots 11-14


					if(("itnas01a" in line_store[4]) or ("itnas01b" in line_store[4])):
						ice_T1_used_graphs[j]+=float(line_store[6])
						ice_T3_used_graphs[j]+=float(line_store[7])
						ice_T3B_used_graphs[j]+=float(line_store[8])
						ice_T4_used_graphs[j]+=float(line_store[9])

						ice_T1_total_graphs[j]+=float(line_store[11])
						ice_T3_total_graphs[j]+=float(line_store[11])
						ice_T3B_total_graphs[j]+=float(line_store[11])
						ice_T4_total_graphs[j]+=float(line_store[11])

					elif(("swnas01a" in line_store[4]) or ("swnas01b" in line_store[4])):
						swip_T1_used_graphs[j]+=float(line_store[6])
						swip_T3_used_graphs[j]+=float(line_store[7])
						swip_T3B_used_graphs[j]+=float(line_store[8])
						swip_T4_used_graphs[j]+=float(line_store[9])

						swip_T1_total_graphs[j]+=float(line_store[11])
						swip_T3_total_graphs[j]+=float(line_store[11])
						swip_T3B_total_graphs[j]+=float(line_store[11])
						swip_T4_total_graphs[j]+=float(line_store[11])
					
					elif("itcrncnas01" in line_store[4]):
						it_T1_used_graphs[j]+=float(line_store[6])
						it_T3_used_graphs[j]+=float(line_store[7])
						it_T3B_used_graphs[j]+=float(line_store[8])
						it_T4_used_graphs[j]+=float(line_store[9])

						it_T1_total_graphs[j]+=float(line_store[11])
						it_T3_total_graphs[j]+=float(line_store[11])
						it_T3B_total_graphs[j]+=float(line_store[11])
						it_T4_total_graphs[j]+=float(line_store[11])

					elif(("engnas03a" in line_store[4]) or ("engnas03b" in line_store[4])):
						wwoe_T1_used_graphs[j]+=float(line_store[6])
						wwoe_T3_used_graphs[j]+=float(line_store[7])
						wwoe_T3B_used_graphs[j]+=float(line_store[8])
						wwoe_T4_used_graphs[j]+=float(line_store[9])

						wwoe_T1_total_graphs[j]+=float(line_store[11])
						wwoe_T3_total_graphs[j]+=float(line_store[11])
						wwoe_T3B_total_graphs[j]+=float(line_store[11])
						wwoe_T4_total_graphs[j]+=float(line_store[11])


					if(("itnas01a" in line_store[4]) or ("itnas01b" in line_store[4])):
						ice_T1_used_graphs[j]+=float(line_store[6])
						ice_T3_used_graphs[j]+=float(line_store[7])
						ice_T3B_used_graphs[j]+=float(line_store[8])
						ice_T4_used_graphs[j]+=float(line_store[9])

						ice_T1_total_graphs[j]+=float(line_store[11])
						ice_T3_total_graphs[j]+=float(line_store[11])
						ice_T3B_total_graphs[j]+=float(line_store[11])
						ice_T4_total_graphs[j]+=float(line_store[11])

					elif(("swnas01a" in line_store[4]) or ("swnas01b" in line_store[4])):
						swip_T1_used_graphs[j]+=float(line_store[6])
						swip_T3_used_graphs[j]+=float(line_store[7])
						swip_T3B_used_graphs[j]+=float(line_store[8])
						swip_T4_used_graphs[j]+=float(line_store[9])

						swip_T1_total_graphs[j]+=float(line_store[11])
						swip_T3_total_graphs[j]+=float(line_store[11])
						swip_T3B_total_graphs[j]+=float(line_store[11])
						swip_T4_total_graphs[j]+=float(line_store[11])
					

					elif(("itcrncnas01" in line_store[4])):
						it_T1_used_graphs[j]+=float(line_store[6])
						it_T3_used_graphs[j]+=float(line_store[7])
						it_T3B_used_graphs[j]+=float(line_store[8])
						it_T4_used_graphs[j]+=float(line_store[9])

						it_T1_total_graphs[j]+=float(line_store[11])
						it_T3_total_graphs[j]+=float(line_store[11])
						it_T3B_total_graphs[j]+=float(line_store[11])
						it_T4_total_graphs[j]+=float(line_store[11])

					elif(("engnas03a" in line_store[4]) or ("engnas03b" in line_store[4])):
						wwoe_T1_used_graphs[j]+=float(line_store[6])
						wwoe_T3_used_graphs[j]+=float(line_store[7])
						wwoe_T3B_used_graphs[j]+=float(line_store[8])
						wwoe_T4_used_graphs[j]+=float(line_store[9])

						wwoe_T1_total_graphs[j]+=float(line_store[11])
						wwoe_T3_total_graphs[j]+=float(line_store[11])
						wwoe_T3B_total_graphs[j]+=float(line_store[11])
						wwoe_T4_total_graphs[j]+=float(line_store[11])

	# #start plot figures
	fig = plt.figure()
	fig2= plt.figure()

	# #by site by tier
	fig3= plt.figure()
	fig4=plt.figure()
	fig5=plt.figure()
	fig6=plt.figure()
	fig7=plt.figure()
	fig8=plt.figure()
	fig9=plt.figure()
	fig10=plt.figure()


	# #by dept by tier
	fig11=plt.figure()
	fig12=plt.figure()
	fig13=plt.figure()
	fig14=plt.figure()

	ax1 = fig.add_subplot(111)
	ax2= fig2.add_subplot(111)

	# #by site by tier
	ax3=fig3.add_subplot(111)
	ax4=fig4.add_subplot(111)
	ax5=fig5.add_subplot(111)
	ax6=fig6.add_subplot(111)
	ax7=fig7.add_subplot(111)
	ax8=fig8.add_subplot(111)
	ax9=fig9.add_subplot(111)
	ax10=fig10.add_subplot(111)


	# #by dept by tier
	ax11=fig11.add_subplot(111)
	ax12=fig12.add_subplot(111)
	ax13=fig13.add_subplot(111)
	ax14=fig14.add_subplot(111)

	count_date=[]
	for i in range(len(unique_dates)):
		count_date.append(i)


	# #full storage mockup
	ax1.plot(count_date, used_storage_graphs, c='b', label='Full Storage Used')
	ax1.plot(count_date,total_storage_graphs, c='r', label='Full Storage Total')

	ax2.plot(count_date,netapp_T1_raw_graphs , c='b', label='T1 Raw')
	ax2.plot(count_date,netapp_T3_raw_graphs, c='r', label='T3 Raw')
	ax2.plot(count_date,netapp_T3B_raw_graphs, c='y', label='T3B Raw')
	ax2.plot(count_date,netapp_T4_raw_graphs, c='g', label='T4 Raw')

	# #plot plots for tier and site
	# #sj T1 
	ax3.plot(count_date,sj_T1_used_graphs, c='b', label='SJ T1 Used')
	ax3.plot(count_date,sj_T1_total_graphs, c='w', label='SJ T1 Total')
	#sj T3
	ax3.plot(count_date,sj_T3_used_graphs , c='g', label='SJ T3 Used')
	ax3.plot(count_date,sj_T3_total_graphs, c='r', label='SJ T3 Total')
	#sj T3B
	ax3.plot(count_date,sj_T3B_used_graphs , c='m', label='SJ T3B Used')
	ax3.plot(count_date,sj_T3B_total_graphs, c='c', label='SJ T3B Total')
	#sj T4
	ax3.plot(count_date,sj_T4_used_graphs , c='y', label='SJ T4 Used')
	ax3.plot(count_date,sj_T4_total_graphs, c='k', label='SJ T4 Total')

	# #pg T1
	ax4.plot(count_date,pg_T1_used_graphs, c='b', label='pg T1 Used')
	ax4.plot(count_date,pg_T1_total_graphs, c='w', label='pg T1 Total')
	#pg T3
	ax4.plot(count_date,pg_T3_used_graphs , c='g', label='pg T3 Used')
	ax4.plot(count_date,pg_T3_total_graphs, c='r', label='pg T3 Total')
	#pg T3B
	ax4.plot(count_date,pg_T3B_used_graphs , c='m', label='pg T3B Used')
	ax4.plot(count_date,pg_T3B_total_graphs, c='c', label='pg T3B Total')
	#pg T4
	ax4.plot(count_date,pg_T4_used_graphs , c='y', label='pg T4 Used')
	ax4.plot(count_date,pg_T4_total_graphs, c='k', label='pg T4 Total')

	# #nl T1
	ax5.plot(count_date,nl_T1_used_graphs, c='b', label='nl T1 Used')
	ax5.plot(count_date,nl_T1_total_graphs, c='w', label='nl T1 Total')
	#nl T3
	ax5.plot(count_date,nl_T3_used_graphs , c='g', label='nl T3 Used')
	ax5.plot(count_date,nl_T3_total_graphs, c='r', label='nl T3 Total')
	#nl T3B
	ax5.plot(count_date,nl_T3B_used_graphs , c='m', label='nl T3B Used')
	ax5.plot(count_date,nl_T3B_total_graphs, c='c', label='nl T3B Total')
	#nl T4
	ax5.plot(count_date,nl_T4_used_graphs , c='y', label='nl T4 Used')
	ax5.plot(count_date,nl_T4_total_graphs, c='k', label='nl T4 Total')

	#uk T1
	ax6.plot(count_date,uk_T1_used_graphs, c='b', label='uk T1 Used')
	ax6.plot(count_date,uk_T1_total_graphs, c='w', label='uk T1 Total')
	#uk T3
	ax6.plot(count_date,uk_T3_used_graphs , c='g', label='uk T3 Used')
	ax6.plot(count_date,uk_T3_total_graphs, c='r', label='uk T3 Total')
	#uk T3B
	ax6.plot(count_date,uk_T3B_used_graphs , c='m', label='uk T3B Used')
	ax6.plot(count_date,uk_T3B_total_graphs, c='c', label='uk T3B Total')
	#uk T4
	ax6.plot(count_date,uk_T4_used_graphs , c='y', label='uk T4 Used')
	ax6.plot(count_date,uk_T4_total_graphs, c='k', label='uk T4 Total')

	#jp T1
	ax7.plot(count_date,jp_T1_used_graphs, c='b', label='jp T1 Used')
	ax7.plot(count_date,jp_T1_total_graphs, c='w', label='jp T1 Total')
	#jp T3
	ax7.plot(count_date,jp_T3_used_graphs , c='g', label='jp T3 Used')
	ax7.plot(count_date,jp_T3_total_graphs, c='r', label='jp T3 Total')
	#jp T3B
	ax7.plot(count_date,jp_T3B_used_graphs , c='m', label='jp T3B Used')
	ax7.plot(count_date,jp_T3B_total_graphs, c='c', label='jp T3B Total')
	#jp T4
	ax7.plot(count_date,jp_T4_used_graphs , c='y', label='jp T4 Used')
	ax7.plot(count_date,jp_T4_total_graphs, c='k', label='jp T4 Total')

	#hk T1
	ax8.plot(count_date,hk_T1_used_graphs, c='b', label='hk T1 Used')
	ax8.plot(count_date,hk_T1_total_graphs, c='w', label='hk T1 Total')
	#hk T3
	ax8.plot(count_date,hk_T3_used_graphs , c='g', label='hk T3 Used')
	ax8.plot(count_date,hk_T3_total_graphs, c='r', label='hk T3 Total')
	#hk T3B
	ax8.plot(count_date,hk_T3B_used_graphs , c='m', label='hk T3B Used')
	ax8.plot(count_date,hk_T3B_total_graphs, c='c', label='hk T3B Total')
	#hk T4
	ax8.plot(count_date,hk_T4_used_graphs , c='y', label='hk T4 Used')
	ax8.plot(count_date,hk_T4_total_graphs, c='k', label='hk T4 Total')


	#to T1
	ax9.plot(count_date,to_T1_used_graphs, c='b', label='to T1 Used')
	ax9.plot(count_date,to_T1_total_graphs, c='w', label='to T1 Total')
	#to T3
	ax9.plot(count_date,to_T3_used_graphs , c='g', label='to T3 Used')
	ax9.plot(count_date,to_T3_total_graphs, c='r', label='to T3 Total')
	#to T3B
	ax9.plot(count_date,to_T3B_used_graphs , c='m', label='to T3B Used')
	ax9.plot(count_date,to_T3B_total_graphs, c='c', label='to T3B Total')
	#to T4
	ax9.plot(count_date,to_T4_used_graphs , c='y', label='to T4 Used')
	ax9.plot(count_date,to_T4_total_graphs, c='k', label='to T4 Total')

	#at T1
	ax10.plot(count_date,at_T1_used_graphs, c='b', label='at T1 Used')
	ax10.plot(count_date,at_T1_total_graphs, c='w', label='at T1 Total')
	#to T3
	ax10.plot(count_date,at_T3_used_graphs , c='g', label='at T3 Used')
	ax10.plot(count_date,at_T3_total_graphs, c='r', label='at T3 Total')
	#to T3B
	ax10.plot(count_date,at_T3B_used_graphs , c='m', label='at T3B Used')
	ax10.plot(count_date,at_T3B_total_graphs, c='c', label='at T3B Total')
	#to T4
	ax10.plot(count_date,at_T4_used_graphs , c='y', label='at T4 Used')
	ax10.plot(count_date,at_T4_total_graphs, c='k', label='at T4 Total')

	# #plot plots for depts and tiers

	# #ice
	ax11.plot(count_date,ice_T1_used_graphs , c='y', marker="s", label='Ice Used')
	ax11.plot(count_date,ice_T1_total_graphs , c='k', marker="s", label='Ice Total')

	#swip
	ax12.plot(count_date,swip_T1_used_graphs , c='b', marker="s", label='SWIP Used')
	ax12.plot(count_date,swip_T1_total_graphs , c='r', marker="s", label='SWIP Total')

	#it
	ax13.plot(count_date,it_T1_used_graphs , c='m', marker="s", label='IT Used')
	ax13.plot(count_date,it_T1_total_graphs , c='c', marker="s", label='IT Total')

	#wwoe
	ax14.plot(count_date,wwoe_T1_used_graphs , c='g', marker="s", label='WWOE Used')
	ax14.plot(count_date,wwoe_T1_total_graphs , c='r', marker="s", label='WWOE Total')
	
	ax1.legend(loc='upper left')
	ax2.legend(loc='upper left')
	ax3.legend(loc='upper left')
	ax4.legend(loc='upper left')
	ax5.legend(loc='upper left')
	ax6.legend(loc='upper left')
	ax7.legend(loc='upper left')
	ax8.legend(loc='upper left')
	ax9.legend(loc='upper left')
	ax10.legend(loc='upper left')
	ax11.legend(loc='upper left')
	ax12.legend(loc='upper left')
	ax13.legend(loc='upper left')
	ax14.legend(loc='upper left')



	ax1.set_xlabel('Date(MM/DD/YYYY)', fontsize=10)
	ax2.set_xlabel('Date(MM/DD/YYYY)', fontsize=10)
	ax3.set_xlabel('Date(MM/DD/YYYY)', fontsize=10)
	ax4.set_xlabel('Date(MM/DD/YYYY)', fontsize=10)
	ax5.set_xlabel('Date(MM/DD/YYYY)', fontsize=10)
	ax6.set_xlabel('Date(MM/DD/YYYY)', fontsize=10)
	ax7.set_xlabel('Date(MM/DD/YYYY)', fontsize=10)
	ax8.set_xlabel('Date(MM/DD/YYYY)', fontsize=10)
	ax9.set_xlabel('Date(MM/DD/YYYY)', fontsize=10)
	ax10.set_xlabel('Date(MM/DD/YYYY)', fontsize=10)
	ax11.set_xlabel('Date(MM/DD/YYYY)', fontsize=10)
	ax12.set_xlabel('Date(MM/DD/YYYY)', fontsize=10)
	ax13.set_xlabel('Date(MM/DD/YYYY)', fontsize=10)
	ax14.set_xlabel('Date(MM/DD/YYYY)', fontsize=10)



	ax1.set_ylabel('GB', fontsize=10)
	ax2.set_ylabel('GB', fontsize=10)
	ax3.set_ylabel('GB', fontsize=10)
	ax4.set_ylabel('GB', fontsize=10)
	ax5.set_ylabel('GB', fontsize=10)
	ax6.set_ylabel('GB', fontsize=10)
	ax7.set_ylabel('GB', fontsize=10)
	ax8.set_ylabel('GB', fontsize=10)
	ax9.set_ylabel('GB', fontsize=10)
	ax10.set_ylabel('GB', fontsize=10)
	ax11.set_ylabel('GB', fontsize=10)
	ax12.set_ylabel('GB', fontsize=10)
	ax13.set_ylabel('GB', fontsize=10)
	ax14.set_ylabel('GB', fontsize=10)
	

	
	plt.setp(ax1,xticks=count_date,xticklabels=unique_dates)
	fig.savefig('/storage/data/GLOBAL/usage_images/ax1.png')
	plt.setp(ax2,xticks=count_date,xticklabels=unique_dates)
	fig2.savefig('/storage/data/GLOBAL/usage_images/ax2.png')
	plt.setp(ax3,xticks=count_date,xticklabels=unique_dates)
	fig3.savefig('/storage/data/GLOBAL/usage_images/ax3.png')
	plt.setp(ax4,xticks=count_date,xticklabels=unique_dates)
	fig4.savefig('/storage/data/GLOBAL/usage_images/ax4.png')
	plt.setp(ax5,xticks=count_date,xticklabels=unique_dates)
	fig5.savefig('/storage/data/GLOBAL/usage_images/ax5.png')
	plt.setp(ax6,xticks=count_date,xticklabels=unique_dates)
	fig6.savefig('/storage/data/GLOBAL/usage_images/ax6.png')
	plt.setp(ax7,xticks=count_date,xticklabels=unique_dates)
	fig7.savefig('/storage/data/GLOBAL/usage_images/ax7.png')
	plt.setp(ax8,xticks=count_date,xticklabels=unique_dates)
	fig8.savefig('/storage/data/GLOBAL/usage_images/ax8.png')
	plt.setp(ax9,xticks=count_date,xticklabels=unique_dates)
	fig9.savefig('/storage/data/GLOBAL/usage_images/ax9.png')
	plt.setp(ax10,xticks=count_date,xticklabels=unique_dates)
	fig10.savefig('/storage/data/GLOBAL/usage_images/ax10.png')
	plt.setp(ax11,xticks=count_date,xticklabels=unique_dates)
	fig11.savefig('/storage/data/GLOBAL/usage_images/ax11.png')
	plt.setp(ax12,xticks=count_date,xticklabels=unique_dates)
	fig12.savefig('/storage/data/GLOBAL/usage_images/ax12.png')
	plt.setp(ax13,xticks=count_date,xticklabels=unique_dates)
	fig13.savefig('/storage/data/GLOBAL/usage_images/ax13.png')
	plt.setp(ax14,xticks=count_date,xticklabels=unique_dates)
	fig14.savefig('/storage/data/GLOBAL/usage_images/ax14.png')


def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output

def convertFloat(input):
	for i in range(len(input)):
		input[i]=float(input[i])
	return input

#end main
#isilon function
def calculate_isilon():
   	#using boolean to check isilon part of input file
	isilon_check= False 
	#get user input
	#read input of file
	try:
		#open input file
		input_file = open("jackfinal.txt", "r")
	except:
		#if file can't be read, exit
		print "Could not read file:", input_file
   		sys.exit()

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
				#adding appropriate values in lists
				#isilon_site.append("sj")
				isilon_dept.append("ice")
				isilon_filer.append(isilon_filer_temp)
				isilon_aggr.append("NULL")
				isilon_site.append(isilon_filer_temp[:2])
				#getting date
				isilon_date.append(now.strftime("%m-%d-%Y"))
				isilon_time.append(now.strftime("%H:%M"))
				#adding vendor name
				isilon_vendors.append("isilon")

				#convert using .75 ratio
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


				#put back T because it was stripped out while converting
				if("T" in last_total):
					isilon_avail.append(str(avil)+'T')
					isilon_total.append(str(total_store)+'T')
					isilon_used.append(str(used_store) +'T')
				#put back G because it was was stripped out while converting
				else:
					isilon_avail.append(str(avil)+'G')
					isilon_total.append(str(total_store)+'G')
					isilon_used.append(str(used_store) +'G')


				#conditionals then adds depending on keywords on line, based on that the value will be added 
				#to the respective T_...

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


	#convert to GB
	for i in range(len(isilon_T1)):

		#for T1
		if("GB" in isilon_T1[i]):
			#strip out 2 last character which are GB
			isilon_T1[i] = isilon_T1[i][:-2]

		if("T" in isilon_T1[i]):
			isilon_T1[i]= isilon_T1[i][:-1]
			isilon_T1[i] = float(isilon_T1[i]) *1024

		#for T3
		if("GB" in isilon_T3[i]):
			#strip out 2 last character which are GB
			isilon_T3[i] = isilon_T3[i][:-2]

		if("T" in isilon_T3[i]):
			isilon_T3[i]= isilon_T3[i][:-1]
			isilon_T3[i] = float(isilon_T3[i]) *1024

		#for T3B
		if("GB" in isilon_T3B[i]):
			#strip out 2 last character which are GB
			isilon_T3B[i] = isilon_T3B[i][:-2]

		if("T" in isilon_T3B[i]):
			isilon_T3B[i]= isilon_T3B[i][:-1]
			isilon_T3B[i] = float(isilon_T3B[i]) *1024

		#for T4
		if("GB" in isilon_T4[i]):
			#strip out 2 last character which are GB
			isilon_T4[i] = isilon_T4[i][:-2]

		if("T" in isilon_T4[i]):
			isilon_T4[i]= isilon_T4[i][:-1]
			isilon_T4[i] = float(isilon_T4[i]) *1024



		#for total
		if("GB" in isilon_total[i]):
			#strip out 2 last character which are GB
			isilon_total[i] = isilon_total[i][:-2]

		if("T" in isilon_total[i]):
			isilon_total[i]= isilon_total[i][:-1]
			isilon_total[i] = float(isilon_total[i])*1024


		#for used
		if("GB" in isilon_used[i]):
			#strip out 2 last character which are GB
			isilon_used[i] = isilon_used[i][:-2]

		if("T" in isilon_used[i]):
			isilon_used[i]= isilon_used[i][:-1]
			isilon_used[i] = float(isilon_used[i]) *1024


		#for avail
		if("GB" in isilon_avail[i]):
			#strip out 2 last character which are GB
			isilon_avail[i] = isilon_avail[i][:-2]

		if("T" in isilon_avail[i]):
			isilon_avail[i]= isilon_avail[i][:-1]
			isilon_avail[i] = float(isilon_avail[i]) *1024




#end isilon function======================================================

#netapp function
def calculate_netapp():
	#netapp here
	#file name of input file entered by user

	#open file name from user
	try:
		input_file = open("jackfinal.txt", "r")

	#throw exception if file cannot be read then exit
	except:
		print "Could not read file:", filename
   		sys.exit()

   	#using boolean to check netapp part of input file
	netapp_check= False 

	#iterate thru lines of input file
	for i, line in enumerate(input_file):
		line_store=line.split()

		#check thru if netapp part of file
		if(len(line_store)>=1):
			if(( "NETAPP" in line_store[0])):
				netapp_check=True


		#check boolean to check for netapp part of file
		if(netapp_check):
			if("Filer:" in line):
				netapp_filer_temp=line_store[1]
			if not ("Filer" in line) or ("Aggregate" in line) or("entries" in line) or("status" in line) or("Permission" in line) or ("NETAPP" in line) or("GLOBAL" in line):
				if("GB" in line) and ("%" in line):

					#adding appropriate values in lists
					netapp_filer.append(netapp_filer_temp)
					netapp_aggr.append(line_store[0])
					netapp_total.append(line_store[1])
					netapp_used.append(line_store[2])
					netapp_avail.append(line_store[3])
					netapp_capacity.append(line_store[4])

					#adding netapp vendor to list
					netapp_vendors.append("netapp")
					netapp_site.append(netapp_filer_temp[:2])
					netapp_dept.append(netapp_filer_temp[3:])

					#adding date to list
					netapp_date.append(now.strftime("%m-%d-%Y"))
					netapp_time.append(now.strftime("%H:%M"))

					#conditionals then adds depending on keywords on line, based on that the value will be added 
					#to the respective T_...

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


	#convert to GB
	for i in range(len(netapp_T1)):

		#for T1
		if("GB" in netapp_T1[i]):
			#strip out 2 last character which are GB
			netapp_T1[i] = netapp_T1[i][:-2]

		if("T" in netapp_T1[i]):
			netapp_T1[i]= netapp_T1[i][:-1]
			netapp_T1[i] = float(netapp_T1[i]) *1024

		#for T3
		if("GB" in netapp_T3[i]):
			#strip out 2 last character which are GB
			netapp_T3[i] = netapp_T3[i][:-2]

		if("T" in netapp_T3[i]):
			netapp_T3[i]= netapp_T3[i][:-1]
			netapp_T3[i] = float(netapp_T3[i]) *1024

		#for T3B
		if("GB" in netapp_T3B[i]):
			#strip out 2 last character which are GB
			netapp_T3B[i] = netapp_T3B[i][:-2]

		if("T" in netapp_T3B[i]):
			netapp_T3B[i]= netapp_T3B[i][:-1]
			netapp_T3B[i] = float(netapp_T3B[i]) *1024

		#for T4
		if("GB" in netapp_T4[i]):
			#strip out 2 last character which are GB
			netapp_T4[i] = netapp_T4[i][:-2]

		if("T" in netapp_T4[i]):
			netapp_T4[i]= netapp_T4[i][:-1]
			netapp_T4[i] = float(netapp_T4[i]) *1024

		#for total
		if("GB" in netapp_total[i]):
			#strip out 2 last character which are GB
			netapp_total[i] = netapp_total[i][:-2]

		if("T" in netapp_total[i]):
			netapp_total[i]= netapp_total[i][:-1]
			netapp_total[i] = float(netapp_total[i]) *1024


		#for used
		if("GB" in netapp_used[i]):
			#strip out 2 last character which are GB
			netapp_used[i] = netapp_used[i][:-2]

		if("T" in netapp_used[i]):
			netapp_used[i]= netapp_used[i][:-1]
			netapp_used[i] = float(netapp_used[i]) *1024


		#for avail
		if("GB" in netapp_avail[i]):
			#strip out 2 last character which are GB
			netapp_avail[i] = netapp_avail[i][:-2]

		if("T" in netapp_avail[i]):
			netapp_avail[i]= netapp_avail[i][:-1]
			netapp_avail[i] = float(netapp_avail[i]) *1024




#end netapp function=======================================================






#call main at the end 
main()