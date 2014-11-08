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

def make_parser():
	""" Construct a command line parser"""
	logging.info("Constructing parser")
	description = "Store and retrieve snippets of text"
	parser = argparse.ArgumentParser(description=description)
	return parser
	
def main():
	""" main function"""
	logging.info("Starting snippets")
	parser=make_parser()
	arguments = parser.parse_args(sys.argv[1:])

if __name__ == "__main__":
	main()