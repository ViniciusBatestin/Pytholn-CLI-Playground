class Animal():
    def has_fur(self):
        return True

    def eats(self):
        return True

class Dog(Animal):
    def barks(self):
        return "Woof"

class Cat(Animal):
    def meows(self):
        return "meow"

class Parrot(Animal):
    def has_fur(self):
        return False

p = Parrot()
print("A parrot has fur??? ", p.has_fur())


d = Cat()
print(d.meows())
print(d.has_fur())

# value = 7
# class A:
#     value = 5

# v = A()
# v.value = 3
# print(v.value)
