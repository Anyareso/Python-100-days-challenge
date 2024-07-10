class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    # how to enable class fish to inherit attributed from Animal
    def __init__(self):
        super().__init__()

    # to edit a method in the super class
    def breathe(self):
        # allows it to do everything that the breathe method does in the super class
        super().breathe()
        print("doing this under water")

    def swim(self):
        print("moving in water")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)