input_file = open("jacks.txt", "r")
output = open("output.txt", "w")
for i, line in enumerate(input_file):
    if i == 0:
        output.write(line)
    else:
        if not line.startswith('status'):
            output.write(line)

