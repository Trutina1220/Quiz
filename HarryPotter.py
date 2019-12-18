class Spell: #Parent Class
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation
    def __str__(self):
        return self.name + " " + self.incantation + "\n" + self.get_description()
    def get_description(self):
        return "No Description"
    def execute(self):
        print(self.incantation)
class Accio(Spell): #Child Class
    def __init__(self):
        Spell.__init__(self, "Accio", "Summoning Charm")
    def get_description(self):  #add another method to get the description for Accio
        return "This charm summonsan object to the caster, potentially over a significant distance"
class Confundo(Spell):  #Child Class
    def __init__(self):
        Spell.__init__(self, "Confundo", "Confundus Charm")
    def get_description(self): #this description method is running when the get description is excecuted
        return "Causes the victim to become confused and befuddled."
    def study_spell(spell):
        print(spell)

print(Accio.get_description(Accio))#getting the desctiption for accio




