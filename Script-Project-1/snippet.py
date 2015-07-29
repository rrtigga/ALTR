#opening the total usage file to get the total usages dates 
	try:
		#open input file
		input_file = open("total_usage1.txt", "r")
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
		input_file = open("dept_site_usage1.txt", "r")
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
			input_file = open("total_usage1.txt", "r")
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
	fig.savefig('images/ax1.png')
	plt.setp(ax2,xticks=count_date,xticklabels=unique_dates)
	fig2.savefig('images/ax2.png')
	plt.setp(ax3,xticks=count_date,xticklabels=unique_dates)
	fig3.savefig('images/ax3.png')
	plt.setp(ax4,xticks=count_date,xticklabels=unique_dates)
	fig4.savefig('images/ax4.png')
	plt.setp(ax5,xticks=count_date,xticklabels=unique_dates)
	fig5.savefig('images/ax5.png')
	plt.setp(ax6,xticks=count_date,xticklabels=unique_dates)
	fig6.savefig('images/ax6.png')
	plt.setp(ax7,xticks=count_date,xticklabels=unique_dates)
	fig7.savefig('images/ax7.png')
	plt.setp(ax8,xticks=count_date,xticklabels=unique_dates)
	fig8.savefig('images/ax8.png')
	plt.setp(ax9,xticks=count_date,xticklabels=unique_dates)
	fig9.savefig('images/ax9.png')
	plt.setp(ax10,xticks=count_date,xticklabels=unique_dates)
	fig10.savefig('images/ax10.png')
	plt.setp(ax11,xticks=count_date,xticklabels=unique_dates)
	fig11.savefig('images/ax11.png')
	plt.setp(ax12,xticks=count_date,xticklabels=unique_dates)
	fig12.savefig('images/ax12.png')
	plt.setp(ax13,xticks=count_date,xticklabels=unique_dates)
	fig13.savefig('images/ax13.png')
	plt.setp(ax14,xticks=count_date,xticklabels=unique_dates)
	fig14.savefig('images/ax14.png')