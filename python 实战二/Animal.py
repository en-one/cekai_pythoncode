import yaml

class Animal:
    name: str = 'default'
    color: str = 'default'
    age: int = 1
    gender: str = 'default'

    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def brake(self):
        print("动物叫")

    def run(self):
        print("动物叫")


class Cat(Animal):
    hair: str = 'Shorthair'

    def catch(self):
        print("捉到了老鼠")

    def run(self):
        print("喵喵叫")


class Dog(Animal):
    hair: str = 'Longhair'

    def keep(self):
        print("能守家")

    def run(self):
        print("旺旺叫")


def main():
    with open("animal_data.yaml") as f:
        datas = yaml.safe_load(f)

    catcat = Cat(datas['catcat']['name'], datas['catcat']['color'], datas['catcat']['age'], datas['catcat']['gender'])
    catcat.catch()
    print(catcat.name, catcat.color, catcat.age, catcat.gender, catcat.hair)

    dogdog = Dog(datas['dogdog']['name'], datas['dogdog']['color'], datas['dogdog']['age'], datas['dogdog']['gender'])
    dogdog.keep()
    print(dogdog.name, dogdog.color, dogdog.age, dogdog.gender, dogdog.hair)


if __name__ == '__main__':
    main()
