from include import MoveType
from include import Tag
from include import Stage
from include import Buff
from move import Move
from game import Player
from game import Game
from card import Card
from card_parser import CardParser

## TODO:
# 3. player lost win ? (need test)
#  3.0    game start game end.
# 3.1 draw card
# 4. simple spell like hero powers
# 5. the big one: generalize card parsing
#    (1) key words of minions
#     (2) deal damage & restore & add attack/health effect
# 6. player mulligan thinking / or simulated
# 7. 

def print_moves(moves):
	print ("==============")
	print (str(len(moves)) + " options")
	for move in moves:
		print(move.__dict__)

if __name__ == "__main__":
	P = Player(1)
	cp = CardParser()
	cp.open("card-parser/card.json")
	cp.read()
	
	g = Game()
	
	g.init_games(Card(1, cp.find("HERO_03")).summon_hero(), Card(2, cp.find("HERO_03")).summon_hero(), None)
	g.dump()
	
	g.do_move(Move(MoveType.EndThisTurn))
	
	g.do_move(Move(MoveType.EndThisTurn))
	
	g.player[1].cards[Tag.Hand] = [Card(1, cp.find("EX1_598")), Card(1, cp.find("EX1_598")), Card(1, cp.find("CS2_171"))]
	
	
	g.stage = Stage.Play
	moves = g.next_moves()
	print_moves(moves)
	g.do_move(moves[2])
	
	g.dump()
	
	moves = g.next_moves()
	print_moves(moves)
	
	g.do_move(moves[1])
	g.player[2].cards[Tag.Hand] = [Card(2, cp.find("BRMA01_4t")), Card(2, cp.find("CS2_119")), Card(2, cp.find("EX1_tk28"))]
	
	
	moves = g.next_moves()
	print_moves(moves)
	g.do_move(moves[0])
	
	moves = g.next_moves()
	
	print_moves(moves)
	g.dump()
	g.do_move(moves[0])
	g.dump()
	
	g.do_move(moves[1])
	g.dump()
	moves = g.next_moves()
	print_moves(moves)
	
	#g.do_move(moves[2])
	#g.dump()
	#moves = g.next_moves()
	#print_moves(moves)
