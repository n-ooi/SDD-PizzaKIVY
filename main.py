from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
import csv
import pandas as pd

CartItems = [["Vegan Roasted Pineapple", 0, 18.50], ["Tandoori Chicken", 0, 18], ["Chicken 'n' Avo", 0, 19.50],
             ["Beef 'n' Shrooms", 0, 20], ["Mary's Little Lamb", 0, 18.5], ["Egg 'n' Bacon", 0, 16],
             ["Basic Margherita", 0, 11.50], ["Aloha", 0, 12.50], ["Veges 'n' Veges", 0, 17],
             ["Gourmet Pepperoni", 0, 16.50], ["Peri Peri", 0, 18], ["Mystery Meat", 0, 17.00],

             ["Sprite", 0, 4.50], ["Coca Cola", 0, 4.50], ["Solo", 0, 4.50],
             ["Fanta", 0, 4.50], ["Bottled Water", 0, 1], ["Lightly Sparkling Water", 0, 2],
             ["Ice Coffee", 0, 6.50], ["Kombucha", 0, 6.50], ["Choccy Shake", 0, 10.50],
             ["Berry Good Shake", 0, 10.50], ["Vanilla Shake", 0, 10.50], ["Caramel Shake", 0, 10.50]]
PriceInfo = [0, 0, 0]


# [Total Cost, Amount of GST, Cost excluding GST]

class PizzaOrdering(Screen):
    pizza1x = NumericProperty(CartItems[0][1])
    pizza2x = NumericProperty(CartItems[1][1])
    pizza3x = NumericProperty(CartItems[2][1])
    pizza4x = NumericProperty(CartItems[3][1])
    pizza5x = NumericProperty(CartItems[4][1])
    pizza6x = NumericProperty(CartItems[5][1])
    pizza7x = NumericProperty(CartItems[6][1])
    pizza8x = NumericProperty(CartItems[7][1])
    pizza9x = NumericProperty(CartItems[8][1])
    pizza10x = NumericProperty(CartItems[9][1])
    pizza11x = NumericProperty(CartItems[10][1])
    pizza12x = NumericProperty(CartItems[11][1])

    def add_product(self, index, root):
        CartItems[index][1] = CartItems[index][1] + 1

        root.pizza1x = (CartItems[0][1])
        root.pizza2x = (CartItems[1][1])
        root.pizza3x = (CartItems[2][1])
        root.pizza4x = (CartItems[3][1])
        root.pizza5x = (CartItems[4][1])
        root.pizza6x = (CartItems[5][1])
        root.pizza7x = (CartItems[6][1])
        root.pizza8x = (CartItems[7][1])
        root.pizza9x = (CartItems[8][1])
        root.pizza10x = (CartItems[9][1])
        root.pizza11x = (CartItems[10][1])
        root.pizza12x = (CartItems[11][1])

        print(CartItems[index])

    def remove_product(self, index, root):
        if CartItems[index][1] > 0:
            CartItems[index][1] = CartItems[index][1] - 1

        root.pizza1x = (CartItems[0][1])
        root.pizza2x = (CartItems[1][1])
        root.pizza3x = (CartItems[2][1])
        root.pizza4x = (CartItems[3][1])
        root.pizza5x = (CartItems[4][1])
        root.pizza6x = (CartItems[5][1])
        root.pizza7x = (CartItems[6][1])
        root.pizza8x = (CartItems[7][1])
        root.pizza9x = (CartItems[8][1])
        root.pizza10x = (CartItems[9][1])
        root.pizza11x = (CartItems[10][1])
        root.pizza12x = (CartItems[11][1])

        print(CartItems[index])


class DrinkOrdering(Screen):
    drink1x = NumericProperty(CartItems[12][1])
    drink2x = NumericProperty(CartItems[13][1])
    drink3x = NumericProperty(CartItems[14][1])
    drink4x = NumericProperty(CartItems[15][1])
    drink5x = NumericProperty(CartItems[16][1])
    drink6x = NumericProperty(CartItems[17][1])
    drink7x = NumericProperty(CartItems[18][1])
    drink8x = NumericProperty(CartItems[19][1])
    drink9x = NumericProperty(CartItems[20][1])
    drink10x = NumericProperty(CartItems[21][1])
    drink11x = NumericProperty(CartItems[22][1])
    drink12x = NumericProperty(CartItems[23][1])

    def add_product(self, index, root):
        CartItems[index][1] = CartItems[index][1] + 1

        root.drink1x = (CartItems[12][1])
        root.drink2x = (CartItems[13][1])
        root.drink3x = (CartItems[14][1])
        root.drink4x = (CartItems[15][1])
        root.drink5x = (CartItems[16][1])
        root.drink6x = (CartItems[17][1])
        root.drink7x = (CartItems[18][1])
        root.drink8x = (CartItems[19][1])
        root.drink9x = (CartItems[20][1])
        root.drink10x = (CartItems[21][1])
        root.drink11x = (CartItems[22][1])
        root.drink12x = (CartItems[23][1])

        print(CartItems[index])

    def remove_product(self, index, root):
        if CartItems[index][1] > 0:
            CartItems[index][1] = CartItems[index][1] - 1

        root.drink1x = (CartItems[12][1])
        root.drink2x = (CartItems[13][1])
        root.drink3x = (CartItems[14][1])
        root.drink4x = (CartItems[15][1])
        root.drink5x = (CartItems[16][1])
        root.drink6x = (CartItems[17][1])
        root.drink7x = (CartItems[18][1])
        root.drink8x = (CartItems[19][1])
        root.drink9x = (CartItems[20][1])
        root.drink10x = (CartItems[21][1])
        root.drink11x = (CartItems[22][1])
        root.drink12x = (CartItems[23][1])

        print(CartItems[index])


class CartScreen(Screen):
    def on_enter(self):
        PriceInfo = [0, 0, 0]
        items = ""
        amount_ordered = ""
        item_cost = ""
        subtotal_cost = ""
        for i in range(len(CartItems)):
            if CartItems[i][1] > 0:  # makes sure that it only displays items bought
                items += str(CartItems[i][0]) + '\n'  # progressively makes a list of all items bought
                amount_ordered += str(CartItems[i][1]) + '\n'  # progressively makes a list of the quantities
                item_cost += "$" + str(CartItems[i][2]) + '\n'  # progressively makes a list of the individual costs
                subtotal_cost += "$" + str(float(CartItems[i][1] * CartItems[i][
                    2])) + '\n'  # progressively makes a list of the total costs of each item
                PriceInfo[0] += float(CartItems[i][1] * CartItems[i][2])

        print(PriceInfo)
        PriceInfo[1] = round(PriceInfo[0] * .1, 2)  # calculates GST to 2 decimal points
        PriceInfo[2] = round(PriceInfo[0] - PriceInfo[1], 2)  # calculates total - excluding GST

        print(PriceInfo)

        self.ids.itemnames.text = items
        self.ids.quantity.text = amount_ordered
        self.ids.item_cost.text = item_cost
        self.ids.totalitemcost.text = subtotal_cost
        self.ids.total.text = "GST: $" + str(float(PriceInfo[1])) + "\n" + "\n" + "Product Cost: $" + str(
            float(PriceInfo[2])) + '\n' + "\n" + "Total: $" + str(float(PriceInfo[0]))


class CheckoutScreen(Screen):
    def print_receipt(self, root):
        PriceInfo = [0, 0, 0]
        items = ""
        amount_ordered = ""
        item_cost = ""
        subtotal_cost = ""
        for i in range(len(CartItems)):
            if CartItems[i][1] > 0:  # makes sure that it only displays items bought
                items += str(CartItems[i][0]) + '\n'  # progressively makes a list of all items bought
                amount_ordered += str(CartItems[i][1]) + '\n'  # progressively makes a list of the quantities
                item_cost += "$" + str(CartItems[i][2]) + '\n'  # progressively makes a list of the individual costs
                subtotal_cost += "$" + str(float(CartItems[i][1] * CartItems[i][
                    2])) + '\n'  # progressively makes a list of the total costs of each item
                PriceInfo[0] += float(CartItems[i][1] * CartItems[i][2])

        PriceInfo[1] = round(PriceInfo[0] * .1, 2)  # calculates GST to 2 decimal points
        PriceInfo[2] = round(PriceInfo[0] - PriceInfo[1], 2)  # calculates total - excluding GST

        print("_______________________________________")
        print(items.split("\n"))
        items_list = items.split("\n")
        print(amount_ordered.split("\n"))
        amount_ordered_list = amount_ordered.split("\n")
        print(item_cost.split("\n"))
        item_cost_list = item_cost.split("\n")
        print(subtotal_cost.split("\n"))
        subtotal_cost_list = subtotal_cost.split("\n")
        print("GST: $" + str(float(PriceInfo[1])) + "\n" + "\n" + "Product Cost: $" + str(
            float(PriceInfo[2])) + '\n' + "\n" + "Total: $" + str(float(PriceInfo[0])))

        df = pd.read_csv('example_output.csv')
        df = df[['ItemType', 'Quantity']]
        importedQuantities = [*df['Quantity']]
        print(importedQuantities)
        print(importedQuantities[0])
        for i in range(0, 24):
            importedQuantities[i] += CartItems[i][1]

        df['Quantity'] = importedQuantities
        df.to_csv('example_output.csv')

class WindowManager(ScreenManager):
    pass


class PapasPizzas(MDApp):
    def build(self):
        return Builder.load_file('main.kv')


print(PizzaOrdering.pizza1x)
Window.fullscreen = 'auto'
PapasPizzas().run()
print(PizzaOrdering.pizza1x)
