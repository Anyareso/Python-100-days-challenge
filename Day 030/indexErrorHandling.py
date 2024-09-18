fruits = eval(input("Name some fruits: "))

# TODO Catch the exception and make sure the code runs without crashing


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("fruit pie")
    else:
        print(fruit + "pie")


make_pie(10)
