# Arcana Peak: The RPG
## A simple text-based RPG set in a fantasy world made in Python.
### Licensing:
* Arcana Peak: The RPG code is licensed under the [GNU GPL v3](https://www.gnu.org/licenses/quick-guide-gplv3.html).
* Arcana Peak: The RPG Soundtrack by Dane Campbell is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0)

### Dependencies:
* Python 3 (Developed using Python 3.12)
  * [blessed](https://pypi.org/project/blessed/)
  * [pygame](https://pypi.org/project/pygame/)
  * [urwid](https://github.com/urwid/urwid)
  * [asciimatics](https://github.com/peterbrittain/asciimatics)
  * [mido](https://mido.readthedocs.io/en/stable/binaries.html?highlight=play#mido-play)

### Planned Features:
* Character voices use instruments like in Don't Starve
* Single save file in json format
* Munchkin method for character creation
* Turn-based combat
* Coyote time for fall damage
* Roll high, under
* Classes trees:
  * Arcanist
    * Unlockable at Arcana Peak by reading the book "On Arcana"
  * Atrima ("One who wields a bow")
    * Unlockable by becoming an Apprentice
  * Bureaucrat
    * Unlockable in a Human Kingdom capitol city
* Talents:
  * Teaching Aura - You grant +1/2/3 Knw to a party member. (Knw >= 16)
  * Meat Shield - You absorb 10/20/30% of damage dealt to party members. (Vit >= 16)
  * Glass Canon - You have +10/20/30% incoming and outgoing damage. (Knw >= 16, Vit >= 12)
  * Berserk - You deal up to +10/20/30% damage at low health. (Vit >= 16)
  * Vampirism - You heal for 5/10/15% of all damage you deal. (Vit >= 12)
* Abilities:
  * Battle Medic - A party member within a meter of you heals for 1d10 HP. (Knw >= 14, Prs >= 14) Costs 1 Knw and 1 Prs
* Arcanist Spells:
  * Spark
    * Consume some tinder to alight a nearby flammable object.
  * Slay
    * Deal major damage to an enemy.

### Attributes
Each attribute has a value from 3-18
* Will
* Knowledge
* Presence
* Dynamics
* Brawn
* Vitality

### Potential Inspiration:
* [5e Magic Items by Rarity](https://dandwiki.com/wiki/5e_Magic_Items_by_Rarity)
* [Homebrew](https://dndbeyond.com/homebrew)
* [Magic of Dungeons and Dragons](https://en.wikipedia.org/wiki/Magic_of_Dungeons_%26a_Dragons)
* [The Hypertext d20 SRD](https://5e.d20srd.org/index.htm)
