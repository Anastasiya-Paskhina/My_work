class animals:
    name = 'Unname'
    weight = 0
    voice = 'none'
    feed = True
    product_animal = 0

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def collect_product(self, volume_product):
        self.volume_product -= produc_animal

    def food(self, feed):
        sele.hungry = Folse
        sele.weight += feed


class gooses(animals):
    voice = 'Ga-ga-ga'
    product_animal = 3 #яйца


class cow(animals):
    voice = 'Muuuu'
    product_animal = 15 #литров

class sheeps(animals):
    voice = 'Me-e-e'
    product_animal = 2 #кг шерсти

class chickens(animals):
    voice = 'Cocococo'
    product_animal = 5 #яиц

class goats(animals):
    voice = 'Be-e-e-e'
    product_animal = 2 #литра

class duck(animals):
    voice = 'Crya-Crya'
    product_animal = 2 #яицa

goose_1 = gooses('Серый', 2)
goose_2 = gooses('Белый', 3)
cow = cow('Манька', 600)
sheep_1 = sheeps('Барашек', 20)
sheep_2 = sheeps('Кудрявый', 15)
chicken_1 = chickens('Ко-ко', 3)
chicken_2 = chickens('Кукареку', 4)
goat_1 = goats('Рога', 30)
goat_2 = goats('Копыта', 25)
duck = duck('Кряква', 5)

zoo = [goose_1, goose_2, cow, sheep_1, sheep_2, chicken_1, chicken_2, goat_1, goat_2, duck]

total_weight = 0
max_weight = 0
heaviest_animal = str()
for animal in zoo:
  total_weight += animal.weight
  if animal.weight > max_weight:
    max_weight = animal.weight
    heaviest_animal = animal.name

print('Вес всех животных {} кг'.format(total_weight))
print('Самое тяжелое животное {}'.format(heaviest_animal))
