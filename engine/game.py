from include import MoveType
from include import Tag
from include import Stage
from include import Buff
from move import Move


class Player:
	def __init__(self, belong_id):
		self.id = belong_id
		self.cards = {}
		self.cards[Tag.Hand] = []
		self.cards[Tag.Minion] = []
		self.taunts = []
		self.resource = 0
		self.max_resource = 0
		self.lost = False
		
	def minions(self):
		str = ""
		
		for m in self.cards[Tag.Minion]:
			k = "{0} ({3}-{1}/{2}){4} ".format(m.name, m.hp, m.max_hp, m.attack, m.attack_this_turn)
			str += k
			
		return str
	
	def dump(self):
		str = 'Hero {0}\n' \
			'Crystal {1}/{2}\n' \
			'Minions {3} {4}\n'.format(self.cards[Tag.Hero].__dict__, self.resource, self.max_resource, len(self.cards[Tag.Minion]), self.minions())
			
		print (str)

class Game:
	def __init__(self):
		self.id = 1
		self.player = [0, Player(1), Player(2)]
		self.stage = Stage.Mulligan
		
	def init_games(self, hero1, hero2, deck1):	
		self.player[1].cards[Tag.Hero] = hero1
		self.player[2].cards[Tag.Hero] = hero2
		self.current_player = self.player[1]
		self.opp_player = self.player[2]

#	def mulligan(self):
#		self.
	def play_moves(self):
		# plays
		l = list()
		for card in self.current_player.cards[Tag.Hand]:
			if (card.cost > self.current_player.resource):
				continue
			m = Move(type = MoveType.Play)
			m.set_entity(card)
			l.append(m)
		# attacks
		if len(self.opp_player.taunts):
			target_list = self.opp_player.taunts.copy()
		else:
			target_list = self.opp_player.cards[Tag.Minion].copy()
			target_list.append(self.opp_player.cards[Tag.Hero])
			target_list = list(filter(lambda x : x.is_attack_target, target_list))

		
		for card in self.current_player.cards[Tag.Minion]:
			if not card.can_attack:
				continue
			
			for target in target_list:
				m = Move(type = MoveType.Attack)
				m.set_entity(card)
				m.set_target(target)			
				l.append(m)
		#end_this_turn
		l.append(Move(MoveType.EndThisTurn))
		return l
		
	def next_moves(self):
		if self.stage == Stage.Mulligan:
			return range(0, 8) if self.current_player is self.player[1] else range(0, 16)
		elif self.stage == Stage.Play:
			return self.play_moves()
		elif self.stage == Stage.Decide:
			pass
		elif self.stage == Stage.Random:
			pass

	def end_this_turn(self, move):
		self.current_player, self.opp_player = self.opp_player, self.current_player
		if self.current_player.max_resource < 10:
			self.current_player.max_resource += 1
		self.current_player.resource = self.current_player.max_resource
		
		for each in self.current_player.cards[Tag.Minion]:
			each.begin_turn()
		# increase resouce.
	
	def play_card(self, move):
		card = move.entity
		self.current_player.cards[Tag.Hand].remove(card)
		if card.info["type"] == "MINION":
			self.current_player.resource = self.current_player.resource - card.cost;
			card.summon()
			print(move.index)
			self.current_player.cards[Tag.Minion].insert(move.index, card)
			if card.buffs[Buff.Taunt]:
				self.current_player.taunts.append(card)
		elif card.info["type"] == "WEAPON":
			pass
		else: # should be spell
			pass
			
	def is_ended(self):
		return self.current_player.is_lost or self.opp_player.is_lost
		
	def check_death(self):
		for each_player in self.player[1:]:
			for minion in each_player.cards[Tag.Minion]:
				if minion.is_dead:
					# FIXME: deathrattle here
					each_player.cards[Tag.Minion].remove(minion)
					if minion.buffs[Buff.Taunt]:
						each_player.taunts.remove(minion)
					
		for each_player in self.player[1:]:
			if each_player.cards[Tag.Hero].is_dead:
				each_play.is_lost = True
	
	def attack(self, move):
	# 	if move.target is None:
	#		raise Exception
		move.target.take_damage(move.entity.attack)
		move.entity.attack_once()
		if move.target.tag == Tag.Minion:
			move.entity.take_damage(move.target.attack)
			
		self.check_death()
		pass
		
	def decide(self, move):
		pass
		
	def random(self, move):
		pass
		
	def do_move(self, move):
		switch = {
			MoveType.EndThisTurn : self.end_this_turn,
			MoveType.Play : self.play_card,
			MoveType.Attack : self.attack,
			MoveType.Decide : self.decide,
			MoveType.Random : self.random
		}
		
		return switch[move.type](move)

	def dump(self):
		print ("********************")
		for player in self.player[1:]:
			player.dump()
	

		

	
	
	
	