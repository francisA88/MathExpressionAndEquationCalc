import re
from mappings import maps, sups, pairs

class Engine:
	'''Class for processing math equations and expressions'''
	sample= "y=x³+x"
	def __init__(self, rawString):
		#This string would later contain the final processed equation
		self.processed="" #fully parsed
		self.preprocessed="" #Mid stage of parsing
		self.raw=rawString #unparsed
		self.nodes="•,+,-,/".split(",")
		parGroups=[]
		
	def _handleBrackets(self, string):
		if string.count("(") != string.count(")"):
			return -1
		if string.count("(")==string.count(")")==0:
			return -1
		else:
			span=re.search("\(+.+\)", string).span()
			subString=string[span[0]:span[1]+1]
			self.parGroups.append(subString)
			subString=subString[1:-1]
			if string.count("(")==string.count(")")==1:
				return 1
			self._handleBrackets(string=subString)
	
	def _handleSuperBrackets(self, string):
		openBrac="\u207D"
		closBrac="\u207E"
		
			