import sys
from block import Block
from random import random, shuffle, seed

sys.setrecursionlimit(10**8)


class MazeGenerator:
	def generate(self, map, size):
		self.height, self.width = size
		seed(self.getRandomInt(0, 1000000))
		y = self.getRandomInt(0, self.height - 1)
		x = self.getRandomInt(0, self.width - 1)

		self.dfs(map, (y, x), (0, 0))
		self.generateExit(map)

	def dfs(self, map, currentPosition, direction):
		y, x = currentPosition
		lookupQueue = self.createQueueOfBlocksToLookNext(y, x)

		map[y][x] = Block()
		map[y][x].openWall(direction)

		for pos in lookupQueue:
			if self.isPlaceEmpty(map, pos):
				ny, nx = pos
				map[y][x].openWall((ny - y, nx - x))
				self.dfs(map, pos, (y - ny, x - nx))

	def isPlaceEmpty(self, map, pos):
		y, x = pos
		if y >= 0 and x >= 0 and y < self.height and x < self.width:
			return map[y][x] == None
		return False

	def generateExit(self, map):
		y = self.getRandomInt(self.height // 2, self.height - 1)
		x = self.width - 1
		map[y][x].setExit(True)

	def createQueueOfBlocksToLookNext(self, y, x):
		queue = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
		shuffle(queue)
		return queue

	def getRandomInt(self, min, max):
		return int(random() * (max - min)) + min