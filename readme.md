# Arcana Peak: The RPG
## A simple text-based RPG set in a fantasy world made in Python.
### Licensing:
* Arcana Peak: The RPG code is licensed under the [GNU GPL v3](https://www.gnu.org/licenses/quick-guide-gplv3.html).
* Arcana Peak: The RPG Soundtrack by Dane Campbell is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0).

### Dependencies:
*  [fluidsynth](https://github.com/FluidSynth/fluidsynth)
* Python 3
	* [blessed](https://pypi.org/project/blessed/)

### Current Features:
* Currently, there are no functioning mechanics.

### Planned Features:
* Turn-based combat.
* As one plays, one may unlock multiple class trees.
* Classes:
	* Human
		* Available on character creation
	* Arcanist
		* Unlockable at Arcana Peak by reading "On Arcana"
	* Atrima
		* "One who wields a bow"
	* Civil Servant
		* Unlockable in a Human Kingdom
* Talents:
	* Teaching - You grant +2 Int to party members. (Knw >= 18)
	* Diplomacy - You reduce hostility of others. (Speech >= 16)
	* Apprenticeship - You earn +10% XP. (Knw >= 12)
	* Meat Shield - You absorb 15% of damage dealt to party members. (Vit >= 18)
	* Glass Canon - You have +50% incoming and outgoing damage. (Knw >= 18, Vit >= 12)
	* Berserk - You deal up to +50% damage at lower health. (Vit >= 18)
	* Vampirism - You heal for 5% of all damage you deal. (Vit >= 12)
	* Linguistics - Your understanding of languages increases. (Knw >= 16, Speech >= 16)
	* Medicine - You heal 10 HP/turn to party members. (Knw >= 14, Prs >= 14)
* Spells:
	* Spark
		* Consume some tinder to alight a nearby flammable object.
	* Slay
		* Deal major damage to an enemy.
* Attributes:
	* Body Attributes:
		* Brawn (Brn) - ability to possess
		* Dynamics (Dyn) - ability to move
		* Vitality (Vit) - ability to live
	* Mind Attributes:
		* Knowledge (Knw) - ability to know
		* Reason (Rsn) - ability to think
		* Presence (Prs) - ability to influence
	* Divine Attribute:
		* Favor (Fav) - standing with the powers that be
* Skills:
	* Artistry = ((3 * Dyn) + Knw + Prs)/5
	* Speech = ((3 * Prs) + Rsn + Kwn)/5
	* Divinity = ((3 * Fav) + Rsn + Prs)/5
	* Science = ((3 * Knw) + Rsn + Prs)/5
	* Acrobatics = ((3 * Dyn) + Brn)/4
	* Athletics = ((3 * Brn) + Dyn)/4
	* Health = ((3 * Vit) + Brn + Dyn)/5
	* Soul = ((3 * Prs) + Knw + Rsn)/5

### Potential Inspiration:
* [5e Magic Items by Rarity](https://dandwiki.com/wiki/5e_Magic_Items_by_Rarity)
* [Homebrew](https://dndbeyond.com/homebrew)
* [Magic of Dungeons and Dragons](https://en.wikipedia.org/wiki/Magic_of_Dungeons_%26a_Dragons)
* [The Hypertext d20 SRD](https://5e.d20srd.org/index.htm)
