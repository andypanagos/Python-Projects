



class Organism:
    name = 'Unknown'
    species = 'Unknown'
    legs = None
    arms = None
    dna = 'Sequence A'
    origin = 'Unknown'
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nSpecies: {} \nLegs: {} \nArms: {} \nDNA: {} \nOrigin: {} \nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg


class Human(Organism):
    name = 'john'
    species = 'homosapian'
    legs = 2
    arms = 2
    origin = 'earth'

    def ingenuity(self):
        msg = "\nCreates a dealy weapon using only a paper clip, chewing gum, and a roll of duct tape!"
        return msg

class Dog(Organism):
    name = 'spot'
    species = 'canine'
    legs = 4
    arms = 0
    dna = 'sequence 8'
    origin = 'earth'

    def bite(self):
        msg = "nEmits a loud, menacing growl and bites dpwm ferociously on its' target"
        return msg

class Bacterium(Organism):
    name = 'x'
    species = 'bacteria'
    legs = 0
    arms = 0
    dna = 'Sequence C'
    origin = 'mars'

    def replication(self):
        msg = "\n The cells begin to divide into two seperate organisms"
        return msg


    
    




if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.replication())
    
