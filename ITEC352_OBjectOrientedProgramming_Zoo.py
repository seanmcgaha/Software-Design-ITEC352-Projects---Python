#Zoo.py is connected to the Object.py. This will include the main function to the objects.py
from ITEC352_ObjectOrientedProgramming_Objects import Animal, Monkey, Lion, Snake, Otter, Dog, Giraffe, Panda, Bear

def main():
    #Create animals
    simba = Lion("Bongo", 7)
    simba.make_sound()
    simba.feed()

    bongo = Monkey("Bongo", 8)
    bongo.make_sound
    bongo.feed()

    ace = Snake("Ace", 1)
    ace.make_sound()
    ace.feed()
   
    max = Otter("Max", 2)
    max.make_sound()
    max.feed()
   
    scar = Dog("Scar", 3)
    scar.make_sound()
    scar.feed()

    bhutan = Giraffe("Bhutan", 3)
    bhutan.make_sound()
    bhutan.feed()

    spot = Panda("Scar", 3)
    spot.make_sound()
    spot.feed()

    smoky = Bear("Smoky", 5)
    smoky.make_sound()
    smoky.feed()


if __name__ == "__main__":
    main()