# A simple text-based rpg in Python. 
The game will be renamed later.
## Licensing
rpg code is licensed under the [GNU GPL v3](https://www.gnu.org/licenses/quick-guide-gplv3.html).
rpg Soundtrack by Dane Campbell is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0).

## Dependencies
Requires:
* WildMIDI
* Python 3
* Python Packages:
	* fabulous
	* keyboard

## Here is a description of all current and planned game mechanics.
Currently, there are no functioning mechanics.

Combat will be turn based.

During character creation you can choose a class
Classes:
* Arcanist

Talents:

* Teacher - You create an aura granting +1 Int to nearby allies. (Int > 17)
* Diplomat - You reduce hostility of others. (Speech > 85)
* Student - You earn extra XP. (Int > 13)
* Meat Shield - You redirect 15% of damage dealt to allies. (Con > 17)
* Glass Canon - You have +50% incoming and outgoing damage. (Int > 17)
* Berserker - You deal more damage at lower health. (Con > 17)
* Vampire - You heal for 5% of all damage you deal. (Con > 17)
* Linguist - Your understanding of languages increases. (Int > 13, Speech > 75)
* Doctor - You create an aura that heals HP to nearby allies. (Thinking > 45, Wil > 13)

Attributes:
* Body Attributes:
	* Strength (Str) - ability to possess
	* Dexterity (Dex) - ability to move
	* Constitution (Con) - ability to live
* Mind Attributes:
	* Intelligence (Int) - ability to know
	* Wisdom (Wis) - ability to reason
	* Will (Wil) - ability to change
 * Divine Attribute:
	* Favor (Fav) - standing with the powers that be

Skills:
* Crafting = (3 * Dex) + Int + Wil
* Speech = (3 * Wil) + Wis + Int
* Spirit = Con + Wil  + Wis
* Endurance = (2 * Con) + Str
* Armor = Con + Str + Dex
* Perception = Wis + Wil
* Thinking = (2 * Wis) + Int + Wil
* Divinity = (3 * Fav) + Wis + Wil
* Technology = (3 * Int) + Wis + Wil

Potential Inspiration:
https://www.dandwiki.com/wiki/5e_Magic_Items_by_Rarity
https://www.dndbeyond.com/homebrew
https://en.wikipedia.org/wiki/Magic_of_Dungeons_%26a_Dragons
