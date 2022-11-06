# This is a sample Python script.
from src.model.Grammar import Grammar


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_g = Grammar(["S", "A", "B"], ["a", "b"])
    my_g.add_production_to_variable("A", "a")
    my_g.add_production_to_variable("A", "b")
    my_g.add_production_to_variable("A", "AB")

    print(my_g.productions)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
