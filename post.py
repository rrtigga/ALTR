def main():
	#need to use raw_input for non-python-3
	for i, line in enumerate("jacks.txt"):
	    if i == 0:
	        output.write(line)
	    else:
	        if not line.startswith('#'):
	            output.write(line)

main()
