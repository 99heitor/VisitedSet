from collections import deque
import hashlib
import sys

class VisitedSet:
	def __init__(self, max):
		self.visited = deque([],maxlen=max)
		# Visited is a python queue. It supports constant time (O(1)) insert and remove operations from both ends.
		# The maxlen argument sets the queue's max lengh, and automatically removes the last (oldest) entry when inserting a new one.
		# Limiting the size of the visited set was my solution to the memory problem. Another possible solution could have been writing
		# to the disk to save RAM, but it's a lot more complex and I might not have been able to do it in 1~2 days.


	def alreadyVisited(self,url):	
		url = self.trim(url)
		if url:
			newid = self.generateID(url)
			for id in self.visited:
				if id == newid:
					return True
			self.visited.append(newid)
		return False
		# alredyVisited is our main function. It prepares the URL to be added to the visited queue, then checks if it's already there.
		# It returns True if the URL it receives is alredy on our Visited queue. If it is not, it is added and then returns False. 
		# This is the worst performing section, since it performs a linear search on an unsorted array. (O(n), where "n" is the current size of the queue). 
		# There is a reason for this design:
		# Python's [set] collection (https://docs.python.org/2/library/sets.html) supports constant time member checking, but uses much more space
		# since its underlying implementation makes use of hashing. That was my first idea, but since our main constraint is space and not time,
		# I opted for slower member checking and less memory usage.

		
	def trim(self,url):
		if url.startswith("http://"):
			url = url[7:]
		elif url.startswith("https://"):
			url = url[8:]
		if url.startswith("www."):
			url = url[4:]
		return url
		# We cut out the first part of our URL. That's not very necessary, but I wanted to give our generateID function
		# strings that were as different as possible, to avoid md5 collision. Of course, the chances of collision happening
		# is very either way.

	def generateID (self,url):
		id = hashlib.md5(url.encode('utf-8')).hexdigest()
		id = id[:16]
		return id
		# Here we generate the md5 hash of our URL, then convert it to a string that contains its hexadecimal representation
		# We use only the first 16 characters, since our queue size is (usually) small and so are the odds of collisions happening.