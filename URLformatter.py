# !/usr/bin/python

from sys import argv

script, from_file, to_file = argv

def readfile():
	# read file into function from 'from_file' argument
	in_file = open(from_file, 'r')

	urllist = []

	for line in in_file:

		# strip any characters that will mess up list formatting
		line_strp = line.strip()
		fields = line_strp.split(',')

		# skip lines without port checks. assumes Sublist3r check
		# for ip address queries
		if len(fields) <= 2:
			pass

		if len(fields) == 3:
			field1 = fields[0]
			field2 = fields[1]
			field3 = fields[2]

			if field3 == '80':
				headhttp = ('http://' + field1)
			elif field3 == '443':
				headhttp = ('https://' + field1)
			else:
				headhttp = ('http://' + field1 + ':' + field3)

			# add each subdomain to 'urllist'
			urllist.append(headhttp)

		if len(fields) == 4:
			field1 = fields[0]
			field2 = fields[1]
			field3 = fields[2]
			field4 = fields[3]

			if field3 == '80':
				headhttp3 = ('http://' + field1)
			elif field3 == '443':
				headhttp3 = ('https://' + field1)
			else:
				headhttp3 = ('http://' + field1 + ':' + field3)

			urllist.append(headhttp3)

			if field4 == '80':
                                headhttp4 = ('http://' + field1)
                        elif field4 == '443':
                                headhttp4 = ('https://' + field1)
                        else:
                                headhttp4 = ('http://' + field1 + ':' + field4)

			urllist.append(headhttp4)

	# convert 'urllist' to string for buffer object issue.
	# separate each element onto a new line
	str_urllist = str('\n'.join(urllist))

	# open new file to write to using 'to_file' argument
	out_file = open(to_file, 'w')
	out_file.write(str_urllist)
	out_file.close()

	in_file.close()

def main():

	# currently redundant, as you could simply remove the
	# 'main' function and just call 'readfile()'. Created
	# for future changes.
	readfile()

main()
