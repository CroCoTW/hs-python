from enum import Enum

class Tag(Enum):
	Hero = 1
	Minion = 2
	Hand = 3
	Deck = 4
	HeroPower = 5
	Secrete = 6
	
class Stage(Enum):
	Mulligan = 1
	Play = 2
	Decide = 3
	Random = 4
	

class MoveType(Enum):
	EndThisTurn = 1
	Play = 2
	Attack = 3
	Decide = 4
	Random = 5
	

'''
{
    "mechanics": {
		"TAUNT": 72, Done!!
		"WINDFURY": 12, Done!!
		"CHARGE": 27, Done !!
		"STEALTH": 13,
		"DIVINE_SHIELD": 14,
		"FREEZE": 14,
		"FORGETFUL": 2,
		"OVERLOAD": 19,
		"SPELLPOWER": 13,
		"ENRAGED": 7,
		"INSPIRE": 21,
		"COMBO": 12,
		"DEATHRATTLE": 71,
		"BATTLECRY": 183,
		"MORPH": 3,
		"POISONOUS": 4,
		"SECRET": 22,
		"SILENCE": 4,
		"TAG_ONE_TURN_EFFECT": 33,
		"ADJACENT_BUFF": 2,
		"AURA": 41
		"ImmuneToSpellpower": 16,
		"InvisibleDeathrattle": 9,
    },
    "type": {
        "ENCHANTMENT": 326,
        "HERO": 125,
        "HERO_POWER": 169,
        "MINION": 800,
        "SPELL": 470,
        "WEAPON": 46
    }
}

'''

class Buff(Enum):
	Taunt = 0
	Windfury = 1
	Charge = 2
	Stealth = 3
	DivineShield = 4
	Freeze = 5
	Forgetful = 6
	SpellPower = 7
	Poisonous = 8
	Aura = 9
	ImmuneToSpellpower = 10
	
class Trigger(Enum):
	Enraged = 0
	Inspire = 1
	Combo = 2
	Battlecry = 3
	Dealthrattle = 4
	