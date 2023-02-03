#from turtle import Turtle, Screen
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)


# dicky = Turtle()
# dicky.shape("turtle")
# dicky.color("brown2")
# dicky.forward(100)
#
#
# my_screen = Screen()
# my_screen.exitonclick()



