import logging
import csv
import argparse
import sys

# Set the log output file and the log level
logging.basicConfig(filename="output.log", level=logging.DEBUG)

def put(name,snippet,filename):
	"""Store a snippet with an associated name in the csv file"""
	logging.info("Writing {!r}:{!r} to {!r}".format(name,snippet,filename))
	logging.debug("Opening file")
	with open(filename, "a") as f:
		writer = csv.writer(f)
		logging.debug("Writing the snippet to file")
		writer.writerow([name,snippet])
	logging.debug("Write sucessful")
	return name, snippet
	
def get(name,filename):
	"""Retrieve a strored snippet with the associated name from the csv file"""
	logging.info("Retrieving {!r} from {!r}".format(name,filename))
	logging.debug("Reading file")
	with open(filename, "r") as f:
		reader = csv.reader(f)
		logging.debug("Reading the snippet from file")
		for row in reader:
			if row[0]==name:
				return name,row[1] 
	logging.debug("Read sucessful")
	#return name, "Error"

def make_parser():
	""" Construct a command line parser"""
	logging.info("Constructing parser")
	description = "Store and retrieve snippets of text"
	parser = argparse.ArgumentParser(description=description)
	
	subparsers = parser.add_subparsers(dest="command",help="Available commands")
	# Subparser for put command
	logging.debug("Constructing put subparser")
	put_parser = subparsers.add_parser("put",help="Store a snippet")
	put_parser.add_argument("name", help = "the name of the snippet")
	put_parser.add_argument("snippet", help = "snippet text")
	put_parser.add_argument("filename", default = "snippets.csv",nargs="?", help = "the snippet filename")
	
	#Subparser for the get command
	logging.debug("Constructing get subparser")
	get_parser = subparsers.add_parser("get",help ="Retrieve a snippet")
	get_parser.add_argument("name",help = "the name of the snippet")
	get_parser.add_argument("filename", default = "snippets.csv",nargs="?", help = "the snippet filename")
	
	return parser
	
def main():
	""" main function"""
	logging.info("Starting snippets")
	parser=make_parser()
	arguments = parser.parse_args(sys.argv[1:])
	#Convert parsed arguments from Namespace to dictionary
	arguments = vars(arguments)
	command = arguments.pop("command")
	
	#Put
	if command == "put":
		name,snippet = put(**arguments)
		print "Stored {!r} as {!r}".format(snippet,name)
		
	#Get
	elif command == "get":
		try:
			name,snippet = get(**arguments)
			print "Retrieved {!r} from {!r}  ".format(name,snippet)
		except:
			print ' Value does not exist '
			logging.debug("Non existent value requested")
	
if __name__ == "__main__":
	main()