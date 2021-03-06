#here are the graph mathplotlib
#in order to install you need to run this command: sudo pip install matplotlib
import numpy as np
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

	print total_storage
	print used_storage

	total_storageList=[]
	used_storageList =[]
	total_storageList.append(total_storage)
	used_storageList.append(used_storage)

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

	#convert to raw storage

	f = open('output.html','w')

	message = """
<!DOCTYPE html>
<meta charset="utf-8">
<style>

body {
  font: 10px sans-serif;
}

.axis path,
.axis line {
  fill: none;
  stroke: #000;
  shape-rendering: crispEdges;
}

.dot {
  stroke: #000;
}

</style>
<body>
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min.js"></script>
<script>

var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var x = d3.scale.linear()
    .range([0, width]);

var y = d3.scale.linear()
    .range([height, 0]);

var color = d3.scale.category10();

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

d3.tsv("data.tsv", function(error, data) {
  if (error) throw error;

  data.forEach(function(d) {
    d.sepalLength = +d.sepalLength;
    d.sepalWidth = +d.sepalWidth;
  });

  x.domain(d3.extent(data, function(d) { return d.sepalWidth; })).nice();
  y.domain(d3.extent(data, function(d) { return d.sepalLength; })).nice();

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis)
    .append("text")
      .attr("class", "label")
      .attr("x", width)
      .attr("y", -6)
      .style("text-anchor", "end")
      .text("Sepal Width (cm)");

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("class", "label")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Sepal Length (cm)")

  svg.selectAll(".dot")
      .data(data)
    .enter().append("circle")
      .attr("class", "dot")
      .attr("r", 3.5)
      .attr("cx", function(d) { return x(d.sepalWidth); })
      .attr("cy", function(d) { return y(d.sepalLength); })
      .style("fill", function(d) { return color(d.species); });

  var legend = svg.selectAll(".legend")
      .data(color.domain())
    .enter().append("g")
      .attr("class", "legend")
      .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

  legend.append("rect")
      .attr("x", width - 18)
      .attr("width", 18)
      .attr("height", 18)
      .style("fill", color);

  legend.append("text")
      .attr("x", width - 24)
      .attr("y", 9)
      .attr("dy", ".35em")
      .style("text-anchor", "end")
      .text(function(d) { return d; });

});

</script>

"""

	f.write(message)
	f.close()







	# fig = plt.figure()
	# fig2= plt.figure()
	
	# ax1 = fig.add_subplot(111)
	# ax2= fig2.add_subplot(111)
	
	# #full storage mockup
	# ax1.scatter(mockup, used_storageList, s=10, c='b', marker="s", label='Used')
	# ax1.scatter(mockup,total_storageList, s=10, c='r', marker="o", label='Total')

	# ax2.scatter(mockup, used_storageList, s=10, c='b', marker="s", label='free')
	# ax2.scatter(mockup,total_storageList, s=10, c='r', marker="o", label='free')
	
	# ax1.legend(loc='upper left');
	# ax2.legend(loc='upper left');

	# plt.show()






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