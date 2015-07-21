#here are the graph mathplotlib
#in order to install you need to run this command: sudo pip install matplotlib
import numpy
import matplotlib.pyplot as plt
import webbrowser
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
	#opening output file
	output = open("output_file.txt", "w")
	output.write("#Date,Time,Vendor,Site,Dept,filer,T1_GB,T3_GB,T3B_GB,T4_GB,aggr,total,used,avail \n")
	output.write("\n")

	print("#Date,Time,Vendor,Site,Dept,filer,T1_GB,T3_GB,T3B_GB,T4_GB,aggr,total,used,avail \n")
	for i in range(len(netapp_aggr)):
		output.write(str(netapp_date[i])+"," +netapp_time[i]+","+str(netapp_vendors[i])+"," +str(netapp_site[i])+ ","+ str(netapp_dept[i])+ ","+ str(netapp_filer[i])+ ","+str(netapp_T1[i])+ ","+str(netapp_T3[i])+","+ str(netapp_T3B[i])+ ","+str(netapp_T4[i])+","+ str(netapp_aggr[i])+ ","+str(netapp_total[i])+ ","+str(netapp_used[i])+","+ str(netapp_avail[i])+"\n")
		#print netapp table
		print (str(netapp_date[i])+"," +netapp_time[i]+","+str(netapp_vendors[i])+"," +str(netapp_site[i])+ ","+ str(netapp_dept[i])+ ","+ str(netapp_filer[i])+ ","+str(netapp_T1[i])+ ","+str(netapp_T3[i])+","+ str(netapp_T3B[i])+ ","+str(netapp_T4[i])+","+ str(netapp_aggr[i])+ ","+str(netapp_total[i])+ ","+str(netapp_used[i])+","+ str(netapp_avail[i]))

	output.write("\n")
	output.write("\n")
	output.write("#Date,Time,Vendor,Site,Dept,filer,T1_GB,T3_GB,T3B_GB,T4_GB,aggr,total,used,avail \n")
	output.write("\n")
	for i in range(len(isilon_site)):
		output.write(str(isilon_date[i])+","+isilon_time[i]+","+str(isilon_vendors[i])+","+ str(isilon_site[i])+","+ str(isilon_dept[i])+","+ str(isilon_filer[i])+","+ str(isilon_T1[i])+","+ str(isilon_T3[i])+","+ str(isilon_T3B[i])+","+ str(isilon_T4[i])+","+ str(isilon_aggr[i])+","+ str(isilon_total[i])+","+ str(isilon_used[i])+ ","+str(isilon_avail[i])+"\n")
		#printing isilon table
		print(str(isilon_date[i])+","+isilon_time[i]+","+str(isilon_vendors[i])+","+ str(isilon_site[i])+","+ str(isilon_dept[i])+","+ str(isilon_filer[i])+","+ str(isilon_T1[i])+","+ str(isilon_T3[i])+","+ str(isilon_T3B[i])+","+ str(isilon_T4[i])+","+ str(isilon_aggr[i])+","+ str(isilon_total[i])+","+ str(isilon_used[i])+ ","+str(isilon_avail[i]))

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




	print total_storage
	print used_storage

	total_storageList=[]
	used_storageList =[]
	total_storageList.append(total_storage)
	used_storageList.append(used_storage)

	#some twenty mockup numbers
	mockup=[]
	mockup.append(1)

	for i in range(20):
		if(i==7 or i==14):
			total_storage+= total_storage*1.5
			total_storageList.append(total_storage)
		else:
			total_storageList.append(total_storage)


		used_storage+=used_storage*1.05
		used_storageList.append(used_storage)
		mockup.append(i+1)	


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

	sj_length=[]
	pg_length=[]
	nl_length=[]
	uk_length=[]
	jp_length=[]
	hk_length=[]
	to_length=[]
	at_length=[]

	for i in range(len(sj_T1_used)):
		sj_length.append(i+1)
	for i in range(len(pg_T1_used)):
		pg_length.append(i+1)
	for i in range(len(nl_T1_used)):
		nl_length.append(i+1)
	for i in range(len(uk_T1_used)):
		uk_length.append(i+1)
	for i in range(len(jp_T1_used)):
		jp_length.append(i+1)
	for i in range(len(hk_T1_used)):
		hk_length.append(i+1)
	for i in range(len(to_T1_used)):
		to_length.append(i+1)
	for i in range(len(at_T1_used)):
		at_length.append(i+1)



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



		#length for the departments

		ice_length=[]
		swip_length=[]
		it_length=[]
		wwoe_length=[]


		for i in range(len(ice_T1_total)):
			ice_length.append(i+1)
		for i in range(len(swip_T1_total)):
			swip_length.append(i+1)
		for i in range(len(it_T1_total)):
			it_length.append(i+1)
		for i in range(len(wwoe_T1_total)):
			wwoe_length.append(i+1)


	mockup2=[]
	for i in range(len(netapp_T3_raw)):
		mockup2.append(i+1)



	#start plot figures
	fig = plt.figure()
	fig2= plt.figure()

	#by site by tier
	fig3= plt.figure()
	fig4=plt.figure()
	fig5=plt.figure()
	fig6=plt.figure()
	fig7=plt.figure()
	fig8=plt.figure()
	fig9=plt.figure()
	fig10=plt.figure()


	#by dept by tier
	fig11=plt.figure()
	fig12=plt.figure()
	fig13=plt.figure()
	fig14=plt.figure()

	ax1 = fig.add_subplot(111)
	ax2= fig2.add_subplot(111)

	#by site by tier
	ax3=fig3.add_subplot(111)
	ax4=fig4.add_subplot(111)
	ax5=fig5.add_subplot(111)
	ax6=fig6.add_subplot(111)
	ax7=fig7.add_subplot(111)
	ax8=fig8.add_subplot(111)
	ax9=fig9.add_subplot(111)
	ax10=fig10.add_subplot(111)


	#by dept by tier
	ax11=fig11.add_subplot(111)
	ax12=fig12.add_subplot(111)
	ax13=fig13.add_subplot(111)
	ax14=fig14.add_subplot(111)




	
	
	#full storage mockup
	ax1.scatter(mockup, used_storageList, s=30, c='b', marker="s", label='Used')
	ax1.scatter(mockup,total_storageList, s=30, c='r', marker="o", label='Total')

	ax2.scatter(mockup2,netapp_T1_raw , s=30, c='b', marker="s", label='T1 Raw')
	ax2.scatter(mockup2,netapp_T3_raw, s=30, c='r', marker="o", label='T3 Raw')
	ax2.scatter(mockup2,netapp_T3B_raw, s=30, c='y', marker="o", label='T3B Raw')
	ax2.scatter(mockup2,netapp_T4_raw, s=30, c='g', marker="o", label='T4 Raw')

	#scatter plots for tier and site
	#sj T1
	ax3.scatter(sj_length,sj_T1_used, s=30, c='b', marker="s", label='SJ T1 Used')
	ax3.scatter(sj_length,sj_T1_total, s=30, c='w', marker="s", label='SJ T1 Total')
	#sj T3
	ax3.scatter(sj_length,sj_T3_used , s=30, c='g', marker="s", label='SJ T3 Used')
	ax3.scatter(sj_length,sj_T3_total, s=30, c='r', marker="s", label='SJ T3 Total')
	#sj T3B
	ax3.scatter(sj_length,sj_T3B_used , s=30, c='m', marker="s", label='SJ T3B Used')
	ax3.scatter(sj_length,sj_T3B_total, s=30, c='c', marker="s", label='SJ T3B Total')
	#sj T4
	ax3.scatter(sj_length,sj_T4_used , s=30, c='y', marker="s", label='SJ T4 Used')
	ax3.scatter(sj_length,sj_T4_total, s=30, c='k', marker="s", label='SJ T4 Total')

	#pg T1
	ax4.scatter(pg_length,pg_T1_used, s=30, c='b', marker="s", label='pg T1 Used')
	ax4.scatter(pg_length,pg_T1_total, s=30, c='w', marker="s", label='pg T1 Total')
	#pg T3
	ax4.scatter(pg_length,pg_T3_used , s=30, c='g', marker="s", label='pg T3 Used')
	ax4.scatter(pg_length,pg_T3_total, s=30, c='r', marker="s", label='pg T3 Total')
	#pg T3B
	ax4.scatter(pg_length,pg_T3B_used , s=30, c='m', marker="s", label='pg T3B Used')
	ax4.scatter(pg_length,pg_T3B_total, s=30, c='c', marker="s", label='pg T3B Total')
	#pg T4
	ax4.scatter(pg_length,pg_T4_used , s=30, c='y', marker="s", label='pg T4 Used')
	ax4.scatter(pg_length,pg_T4_total, s=30, c='k', marker="s", label='pg T4 Total')

	#nl T1
	ax5.scatter(nl_length,nl_T1_used, s=30, c='b', marker="s", label='nl T1 Used')
	ax5.scatter(nl_length,nl_T1_total, s=30, c='w', marker="s", label='nl T1 Total')
	#nl T3
	ax5.scatter(nl_length,nl_T3_used , s=30, c='g', marker="s", label='nl T3 Used')
	ax5.scatter(nl_length,nl_T3_total, s=30, c='r', marker="s", label='nl T3 Total')
	#nl T3B
	ax5.scatter(nl_length,nl_T3B_used , s=30, c='m', marker="s", label='nl T3B Used')
	ax5.scatter(nl_length,nl_T3B_total, s=30, c='c', marker="s", label='nl T3B Total')
	#nl T4
	ax5.scatter(nl_length,nl_T4_used , s=30, c='y', marker="s", label='nl T4 Used')
	ax5.scatter(nl_length,nl_T4_total, s=30, c='k', marker="s", label='nl T4 Total')

	#uk T1
	ax6.scatter(uk_length,uk_T1_used, s=30, c='b', marker="s", label='uk T1 Used')
	ax6.scatter(uk_length,uk_T1_total, s=30, c='w', marker="s", label='uk T1 Total')
	#uk T3
	ax6.scatter(uk_length,uk_T3_used , s=30, c='g', marker="s", label='uk T3 Used')
	ax6.scatter(uk_length,uk_T3_total, s=30, c='r', marker="s", label='uk T3 Total')
	#uk T3B
	ax6.scatter(uk_length,uk_T3B_used , s=30, c='m', marker="s", label='uk T3B Used')
	ax6.scatter(uk_length,uk_T3B_total, s=30, c='c', marker="s", label='uk T3B Total')
	#uk T4
	ax6.scatter(uk_length,uk_T4_used , s=30, c='y', marker="s", label='uk T4 Used')
	ax6.scatter(uk_length,uk_T4_total, s=30, c='k', marker="s", label='uk T4 Total')

	#jp T1
	ax7.scatter(jp_length,jp_T1_used, s=30, c='b', marker="s", label='jp T1 Used')
	ax7.scatter(jp_length,jp_T1_total, s=30, c='w', marker="s", label='jp T1 Total')
	#jp T3
	ax7.scatter(jp_length,jp_T3_used , s=30, c='g', marker="s", label='jp T3 Used')
	ax7.scatter(jp_length,jp_T3_total, s=30, c='r', marker="s", label='jp T3 Total')
	#jp T3B
	ax7.scatter(jp_length,jp_T3B_used , s=30, c='m', marker="s", label='jp T3B Used')
	ax7.scatter(jp_length,jp_T3B_total, s=30, c='c', marker="s", label='jp T3B Total')
	#jp T4
	ax7.scatter(jp_length,jp_T4_used , s=30, c='y', marker="s", label='jp T4 Used')
	ax7.scatter(jp_length,jp_T4_total, s=30, c='k', marker="s", label='jp T4 Total')


	#hk T1
	ax8.scatter(hk_length,hk_T1_used, s=30, c='b', marker="s", label='hk T1 Used')
	ax8.scatter(hk_length,hk_T1_total, s=30, c='w', marker="s", label='hk T1 Total')
	#hk T3
	ax8.scatter(hk_length,hk_T3_used , s=30, c='g', marker="s", label='hk T3 Used')
	ax8.scatter(hk_length,hk_T3_total, s=30, c='r', marker="s", label='hk T3 Total')
	#hk T3B
	ax8.scatter(hk_length,hk_T3B_used , s=30, c='m', marker="s", label='hk T3B Used')
	ax8.scatter(hk_length,hk_T3B_total, s=30, c='c', marker="s", label='hk T3B Total')
	#hk T4
	ax8.scatter(hk_length,hk_T4_used , s=30, c='y', marker="s", label='hk T4 Used')
	ax8.scatter(hk_length,hk_T4_total, s=30, c='k', marker="s", label='hk T4 Total')


	#to T1
	ax9.scatter(to_length,to_T1_used, s=30, c='b', marker="s", label='to T1 Used')
	ax9.scatter(to_length,to_T1_total, s=30, c='w', marker="s", label='to T1 Total')
	#to T3
	ax9.scatter(to_length,to_T3_used , s=30, c='g', marker="s", label='to T3 Used')
	ax9.scatter(to_length,to_T3_total, s=30, c='r', marker="s", label='to T3 Total')
	#to T3B
	ax9.scatter(to_length,to_T3B_used , s=30, c='m', marker="s", label='to T3B Used')
	ax9.scatter(to_length,to_T3B_total, s=30, c='c', marker="s", label='to T3B Total')
	#to T4
	ax9.scatter(to_length,to_T4_used , s=30, c='y', marker="s", label='to T4 Used')
	ax9.scatter(to_length,to_T4_total, s=30, c='k', marker="s", label='to T4 Total')

	#at T1
	ax10.scatter(at_length,at_T1_used, s=30, c='b', marker="s", label='at T1 Used')
	ax10.scatter(at_length,at_T1_total, s=30, c='w', marker="s", label='at T1 Total')
	#to T3
	ax10.scatter(at_length,at_T3_used , s=30, c='g', marker="s", label='at T3 Used')
	ax10.scatter(at_length,at_T3_total, s=30, c='r', marker="s", label='at T3 Total')
	#to T3B
	ax10.scatter(at_length,at_T3B_used , s=30, c='m', marker="s", label='at T3B Used')
	ax10.scatter(at_length,at_T3B_total, s=30, c='c', marker="s", label='at T3B Total')
	#to T4
	ax10.scatter(at_length,at_T4_used , s=30, c='y', marker="s", label='at T4 Used')
	ax10.scatter(at_length,at_T4_total, s=30, c='k', marker="s", label='at T4 Total')




	#scatter plots for depts and tiers
	
	#ice
	ax11.scatter(ice_length,ice_T1_used , s=30, c='y', marker="s", label='Ice Used')
	ax11.scatter(ice_length,ice_T1_total , s=30, c='k', marker="s", label='Ice Total')

	#swip
	ax12.scatter(swip_length,swip_T1_used , s=30, c='b', marker="s", label='SWIP Used')
	ax12.scatter(swip_length,swip_T1_total , s=30, c='r', marker="s", label='SWIP Total')

	#it
	ax13.scatter(it_length,it_T1_used , s=30, c='m', marker="s", label='IT Used')
	ax13.scatter(it_length,it_T1_total , s=30, c='c', marker="s", label='IT Total')

	#wwoe
	ax14.scatter(wwoe_length,wwoe_T1_used , s=30, c='g', marker="s", label='WWOE Used')
	ax14.scatter(wwoe_length,wwoe_T1_total , s=30, c='w', marker="s", label='WWOE Total')




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




	
	plt.show()


def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output




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
		print "Could not read file:", filename
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
				isilon_date.append(now.strftime("%Y-%m-%d"))
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
			isilon_total[i] = float(isilon_total[i]) *1024


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
					netapp_date.append(now.strftime("%Y-%m-%d"))
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