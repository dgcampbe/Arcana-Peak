# Arcana Peak: The RPG
## A simple text-based RPG set in a fantasy world made in Python.
### Licensing:
* Arcana Peak: The RPG code is licensed under the [GNU GPL v3](https://www.gnu.org/licenses/quick-guide-gplv3.html).
* Arcana Peak: The RPG Soundtrack by Dane Campbell is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0)

### Dependencies:
* Python 3 (Developed using Python 3.8, but should work on other versions)
	* [blessed](https://pypi.org/project/blessed/)
	* [pygame](https://pypi.org/project/pygame/)
	* [cmd2](https://pypi.org/project/cmd2/)

### Current Features:
* Currently, there are no functioning mechanics.

### Planned Features:
* Character voices use instruments like in Don't Starve
* Single save file in json format
* Munchkin method for character creation
* Turn-based combat
* As one plays, one may unlock multiple class trees.
* Classes:
	* Arcanist
		* Unlockable at Arcana Peak by reading "On Arcana"
	* Atrima ("One who wields a bow")
		* Unlockable by becoming an Apprentice
	* Bureaucrat
		* Unlockable in a Human Kingdom capitol
* Talents:
	* Teaching - You grant +1/2/3 Int to party members. (Knw >= 18)
	* Meat Shield - You absorb 10/20/30% of damage dealt to party members. (Vit >= 18)
	* Glass Canon - You have +10/20/30% incoming and outgoing damage. (Knw >= 18, Vit >= 12)
	* Berserk - You deal up to +10/20/30% damage at lower health. (Vit >= 18)
	* Vampirism - You heal for 5/10/15% of all damage you deal. (Vit >= 12)
	* Doctor - You heal 10 HP/turn to party members. (Knw >= 14, Prs >= 14)
* Arcanist Spells:
	* Spark
		* Consume some tinder to alight a nearby flammable object.
	* Slay
		* Deal major damage to an enemy.
* Attributes:
	* Artistry
	* Knowledge
		* Science
			* Medicine
		* History
		* Divinity
	* Dynamics
	* Brawn
	* Vitality
	* Soul
	* Presence
		* Speech
			* Diplomacy

### Potential Inspiration:
* [5e Magic Items by Rarity](https://dandwiki.com/wiki/5e_Magic_Items_by_Rarity)
* [Homebrew](https://dndbeyond.com/homebrew)
* [Magic of Dungeons and Dragons](https://en.wikipedia.org/wiki/Magic_of_Dungeons_%26a_Dragons)
* [The Hypertext d20 SRD](https://5e.d20srd.org/index.htm)
