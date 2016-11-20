from visited import VisitedSet
import os, random, sys, time

def crawlerSim(maxvisited,urlnumber):
	visitedset = VisitedSet(maxvisited)
	name = 'urls.txt'
	count = 0
	f = open(name)
	for i in range(urlnumber):
		time.sleep(0.05)	
		currentURL = getRandomLine(f,name)
		if visitedset.alreadyVisited(currentURL):
			print ('Memory: {0} bytes. Alredy visited {1}'.format(sys.getsizeof(visitedset.visited), currentURL.strip("\n")))
		else:
			print ('Memory: {0} bytes. Visiting {1}'.format(sys.getsizeof(visitedset.visited), currentURL.strip("\n")))
	return visitedset
	# This function simulates a bot that surfs the web and uses our VisitedSet to check if some URL was recently visited.


def getRandomLine(file,name):
	size = os.stat(name).st_size
	randombyte = random.randint(0,size)
	file.seek(randombyte)
	file.readline()
	return file.readline()
	# This function gets a random line from a text file on our source folder that contains an URL. 
	# To do so, it seeks a random byte on the file and returns the corresponding line.

def main():
	if (len(sys.argv) == 3):
		try:
			arg1 = int(sys.argv[1])
			arg2 = int(sys.argv[2])
		except:
			print ('Usage: python3 webcrawler [1] [2]')
			print ('[1]: Maximum number of entries on visited set.')
			print ('[2]: Number of sites our bot will try to "visit"')	
			return False
		crawlerSim (arg1,arg2)
	else:
		print ('Incorrect number of arguments. Expected 2, {0} given.'.format(len(sys.argv)-1))


if __name__ == "__main__":
    main()

