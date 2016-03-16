from include import Tag
from enum import Enum
from include import Buff

next_id = 4
entities = dict()


	
	


class Card:
	def __init__(self, belong_player, card_info = None):
		self.id = next_id
		self.name = "Unknown Card"
		self.player = belong_player
		self.buffs = {}
		
		entities[id] = self
		
		if card_info is not None:
			self.set_info(card_info)
		
		
	def set_info(self, card_info):
		self.info = card_info
		self.name = self.info["name"]
		if "cost" in self.info:
			self.cost = self.info["cost"]
		else:
			self.cost = 0
				
		
	def summon_hero(self):
		self.tag = Tag.Hero
		self.max_hp = self.info["health"] 
		self.hp = self.max_hp
		
		return self
		
	@property
	def can_attack(self):
		return self.attack > 0 and (self.buffs[Buff.Charge] or not self.just_summon) and self.attack_this_turn == 0  # FIXME: charge windfurry
		
	@property
	def is_attack_target(self):
		return self.tag == Tag.Hero or not self.buffs[Buff.Stealth]
		
	@property
	def is_spell_target(self):
		return self.tag == Tag.Hero or not self.buffs[Buff.Stealth] and not self.buffs[Buff.ImmuneToSpellpower]
		
	def attack_once(self):
		print("++++++++++attack_once")
		self.attack_this_turn += 1
		self.buffs[Buff.Stealth] = False
		
		
	def begin_turn(self):
		print("++++++++++begin_turn")
		self.attack_this_turn = 0
		self.just_summon = False
	
	def summon(self):
		self.tag = Tag.Minion
		if self.info["type"] != "MINION":
			raise AttributeError
		self.max_hp = self.info["health"] 
		self.hp = self.max_hp
		self.attack = self.info["attack"]
		self.attack_this_turn = 0
		print("++++++++summon")
		self.just_summon = True
		
		has_mech = "mechanics" in self.info
		
		#buffs
		self.buffs[Buff.Taunt] = has_mech and "TAUNT" in self.info["mechanics"]
		self.buffs[Buff.Windfurry] = has_mech and "WINDFURY" in self.info["mechanics"]
		self.buffs[Buff.Stealth] = has_mech and "STEALTH" in self.info["mechanics"]
		self.buffs[Buff.Charge] = has_mech and "CHARGE" in self.info["mechanics"]
		self.buffs[Buff.DivineShield] = has_mech and "DIVINE_SHIELD" in self.info["mechanics"]
		self.buffs[Buff.Forgetful] = has_mech and "FORGETFUL" in self.info["mechanics"]
		self.buffs[Buff.SpellPower] = has_mech and "SPELLPOWER" in self.info["mechanics"] # TODO: fix this later
		self.buffs[Buff.Poisonous] = has_mech and "POISONOUS" in self.info["mechanics"]
		self.buffs[Buff.ImmuneToSpellpower] = has_mech and "ImmuneToSpellpower" in self.info["mechanics"]
			# TODO: fix aura later
			
			
		return self
		
	def draw(self):
		#draw something event
		self.tag = Tag.Hand
		
	def take_damage(self, damage):
		self.predamage(damage)
		self.hp = self.hp - damage
		self.posdamage(damage)
		
	def predamage(self, amount):
		pass
	
	def posdamage(self, amount):
		pass
	
	@property
	def is_dead(self):
		return self.hp <= 0

if __name__ == "__main__":
	print("test Card")
	from card_parser import CardParser
	cp = CardParser()
	cp.open(path = "card-parser/card.json")
	
	cp.read_only_white_minion()
	info = cp.find("EX1_598")
	
	print(info)
	
	info_fail = cp.find("5566")
	print(info_fail)
	
	card = Card(1, info)
	
	print(card.__dict__)
	card.summon()
	
	print(card.__dict__)