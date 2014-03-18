#!/usr/bin/env python

#import os,sys
import Image
import ImageDraw

#import numpy
#import math
import pylab

class analyse(object):
	def __init__(self):
		self.tmpPath = "tmp/"

	def analyseImage(self, imageFullPath, xStart, yStart, xStop, yStop):

		im = Image.open(imageFullPath)
		print im.bits, im.size, im.format

		pixelsInt = []
		pixels = list(im.getdata())

		for x in range(xStart, xStop):
			val = pixels[yStart * 240 + x]
			pixelsInt.append(val)

		for y in range(yStart, yStop):
			val = pixels[xStart + 240 * y]
			pixelsInt.append(val)

		indices = range(1, len(pixelsInt)+1)
		pylab.plot(indices, pixelsInt)

		my_dpi = 80
		#pylab.figure(figsize=(600/my_dpi, 500/my_dpi), dpi=my_dpi)
		pylab.figure(1, figsize=(3.25, 3))

		draw = ImageDraw.Draw(im)
		draw.line([(xStart, yStart),(xStop, yStop)], fill=128)
		del draw

		im.save(self.tmpPath + "line.png", "PNG")
		#pylab.show()
		pylab.savefig(self.tmpPath + "graph.png", dpi=my_dpi)
		pylab.close()
		#600x500

if __name__ == "__main__":
	xStart = 170
	yStart = 10

	xStop = 170
	yStop = 220

	an = analyse()
	an.analyseImage("images/IR_0485.jpg", xStart, yStart, xStop, yStop)
