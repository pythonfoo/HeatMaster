#!/usr/bin/env python

#import os,sys
import Image
import ImageDraw

#import numpy
#import math
import pylab

def bresenham(x0, y0, x1, y1):
	"""https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm"""
	dx = abs(x1-x0)
	dy = abs(y1-y0)
	sx = 1 if x0 < x1 else -1
	sy = 1 if y0 < y1 else -1
	err = dx-dy

	yield x0,y0
	while x0 != x1 or y0 != y1:
		e2 = 2*err
		if e2 > -dy:
			err = err - dy
			x0 = x0 + sx
		if e2 < dx:
			err = err + dx
			y0 = y0 + sy
		yield x0, y0

class analyse(object):
	def __init__(self):
		self.tmpPath = "tmp/"

	def analyseImage(self, imageFullPath, xStart, yStart, xStop, yStop):

		im = Image.open(imageFullPath)
		print im.bits, im.size, im.format

		pixelsInt = [im.getpixel((x,y)) for x,y in bresenham(xStart, yStart, xStop, yStop)]

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
