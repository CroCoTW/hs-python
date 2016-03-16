

	
class Move:
	def __init__(self, type):
		self.type = type
		self.index = 0
		
	def set_target(self, target):
		self.target = target
		
	def set_entity(self, ent):
		self.entity = ent
	
	def set_index(self, index):
		self.index = index