#!/usr/bin/env python
from xml.sax.handler import ContentHandler
from xml.sax import parse

class HeadlineHandler(ContentHandler):
	in_headline = False
	def __init__(self, headlines):
		ContentHandler.__init__(self)
		self.headlines = headlines
		self.data = []

	def startElement(self, name, attrs):
		if name == 'h1':
			self.in_headline = True

	def endElement(self, name):
		if name == 'h1':
			text = ''.join(self.data)
			self.data = []
			self.headlines.append(text)
			self.in_headline = False


	def characters(self, chars):
		if self.in_headline:
			self.data.append(chars)

headlines = []
parse('website.xml', HeadlineHandler(headlines))

for h in headlines:
	print h