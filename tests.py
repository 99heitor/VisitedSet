import webcrawler
from visited import VisitedSet


def testAlredyVisited():
	visitedset = VisitedSet(3)
	if visitedset.alreadyVisited("www.google.com"):
		print ("alredyVisited test failed.")
		return False
		# the first time we check, www.google.com hasn't been visited yet, so it should return False.

	elif not visitedset.alreadyVisited("www.google.com"):
		print ("alredyVisited test failed.")
		return False
		# the second time we check, www.google.com was alredy visited, so it should return True.
	else:
		print ("alredyVisited test succeeded.")
		return True

def testVisitedQueueMaxSize():
	visitedset = VisitedSet(3)
	
	visitedset.alreadyVisited("www.google.com")
	visitedset.alreadyVisited("www.yahoo.com")
	visitedset.alreadyVisited("www.bing.com")

	if len(visitedset.visited) == 3:
		partialTest = True
	else:
		partialTest = False

	#If we add another URL, the queue size should still be 3.

	visitedset.alreadyVisited("www.facebook.com")

	if (len(visitedset.visited) == 3 and partialTest):
		print ("Visited queue max size test succeeded.")
		return True
	else:
		print ("Visited queue max size test failed.")
		return False

def testVisitedRemoveOldestEntry():
	visitedset = VisitedSet(3)
	
	visitedset.alreadyVisited("www.google.com")
	visitedset.alreadyVisited("www.yahoo.com")
	visitedset.alreadyVisited("www.bing.com")

	#If we add another URL, www.google.com should be removed, since the max queue size is 3.

	visitedset.alreadyVisited("www.facebook.com")

	if not visitedset.alreadyVisited("www.google.com"):
		print ("Oldest entry removal test succeeded.")
		return True
	else:
		print ("Oldest entry removal test failed.")
		return False


def main():
	if testAlredyVisited() and testVisitedQueueMaxSize() and testVisitedRemoveOldestEntry():
		print ("All tests succeeded.")
		return True
	else:
		print ("Some test failed.")
		return False
	

if __name__ == "__main__":
    main()
