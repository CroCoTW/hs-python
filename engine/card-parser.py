import json
import os
import re
from card import Card

class CardParser:
	def __init__(self):
		self.data = list()
		self.giant_regex = r"(.*)(Costs \(\d\) less for)(.*)"
		self.index = dict()
		#TODO: self.deal_damage_regex = ?
		#TODO: restore health or whatever ?
		#TODO: Summon N fucking what the fuck?
		#CONTITIONAL?

	def open(self, path):
		self.file = open(path, "r")
		
	def is_minion(self, x):
		return x["type"] == "MINION";
	
	def read(self):
		self.data = json.load(self.file)
		self.data.sort(key = lambda x : x["cost"] if "cost" in x else -1, reverse = True)
		
		for each_card in self.data:
			each_card.pop("flavor", None)
			each_card.pop("artist", None)
		
		self.make_index()
	

	def read_only_white_minion(self):
		self.data = json.load(self.file)
		l = list(filter(lambda x : x["type"] == "MINION" and "text" not in x, self.data))
		
		for each in filter(lambda x : x["type"] == "HERO", self.data):
			l.append(each)	
			
		self.data = l
		self.make_index()
#		for each_card in filter(self.is_minion, self.data):
	#	for each_card in self.data:
			
			
	#		if "text" in each_card:
	#			if re.match(self.giant_regex ,each_card["text"], re.I | re.M):
	#				print (each_card["name"])
	#				print (each_card)
	#				os.system("pause")
	def make_index(self):
		for each_card in self.data:
			self.index[each_card["id"]] = each_card
		
	def find(self, id):
		try:
			return self.index[id]
		except:
			return None
		
	def dump(self):
		print (json.dumps(self.data, indent=4, separators=(',', ': ')))



if __name__ == '__main__':
	print ("hello json")
	cp = CardParser()
	
	cp.open(path = "card-parser/card.json")
	
	cp.read()
	
	l = list()
	
	for each in cp.data:
		if "text" in each and each["type"] == "MINION":
			text = re.sub(r'<[^>]+>', '', each["text"])
			text = re.sub(r'(\n|\.)', '@', text)
			each["desc"] = text.split("@")
			
			while True:
				try:
					each["desc"].remove('')
				except BaseException:
					break
			each["pretty_desc"] = list(map(str.lstrip, each["desc"]))	
			
			if each["cost"] == 1 and each["type"] == "MINION" and "mechanics" in each and "CHARGE" in each["mechanics"]:
				print(each["id"])
				print(each)
			
			l.append(each)

	#	if each["type"] == "MINION" and "text" not in each:
	#		print(each["id"])
	#		print(each["name"])
	#		l.append(each)
		
	#	if each["type"] == "MINION" and "mechanics" in each and "TAUNT" not in each["mechanics"] and "Taunt" in each["text"]:
	#		print("=======")
	#		print(each["id"])
	#		print(each["name"])
	#		print(each["text"])
	#		l.append(each)
	
	print(len(l))