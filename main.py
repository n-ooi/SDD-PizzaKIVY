from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp


ProductsInCart = [["Vegan Roasted Pineapple", 0, 18.50], ["Tandoori Chicken", 0, 18], ["Chicken 'n' Avo", 0, 19.50],
                  ["Beef 'n' Shrooms", 0, 20], ["Mary's Little Lamb", 0, 18.5], ["Egg 'n' Bacon", 0, 16],
                  ["Basic Margherita", 0, 11.50], ["Aloha", 0, 12.50], ["Veges 'n' Veges", 0, 17],
                  ["Gourmet Pepperoni", 0, 16.50], ["Peri Peri", 0, 18], ["Mystery Meat", 0, 17.00],

                  ["Sprite", 0, 4.50], ["Coca Cola", 0, 4.50], ["Solo", 0, 4.50],
                  ["Fanta", 0, 4.50], ["Bottled Water", 0, 1], ["Lightly Sparkling Water", 0, 2],
                  ["Drink 7", 0, 6.50], ["Drink 8", 0, 6.50], ["Choccy Shake", 0, 10.50],
                  ["Berry Good Shake", 0, 10.50], ["Vanilla Shake", 0, 10.50], ["Caramel Shake", 0, 10.50]]
PriceInfo = [0, 0, 0, "0%", 0]

class PizzaOrdering(Screen):
    pizza1x = NumericProperty(ProductsInCart[0][1])
    pizza2x = NumericProperty(ProductsInCart[1][1])
    pizza3x = NumericProperty(ProductsInCart[2][1])
    pizza4x = NumericProperty(ProductsInCart[3][1])
    pizza5x = NumericProperty(ProductsInCart[4][1])
    pizza6x = NumericProperty(ProductsInCart[5][1])
    pizza7x = NumericProperty(ProductsInCart[6][1])
    pizza8x = NumericProperty(ProductsInCart[7][1])
    pizza9x = NumericProperty(ProductsInCart[8][1])
    pizza10x = NumericProperty(ProductsInCart[9][1])
    pizza11x = NumericProperty(ProductsInCart[10][1])
    pizza12x = NumericProperty(ProductsInCart[11][1])

    def add_product(self, index, root):
        ProductsInCart[index][1] = ProductsInCart[index][1] + 1

        root.pizza1x = (ProductsInCart[0][1])
        root.pizza2x = (ProductsInCart[1][1])
        root.pizza3x = (ProductsInCart[2][1])
        root.pizza4x = (ProductsInCart[3][1])
        root.pizza5x = (ProductsInCart[4][1])
        root.pizza6x = (ProductsInCart[5][1])
        root.pizza7x = (ProductsInCart[6][1])
        root.pizza8x = (ProductsInCart[7][1])
        root.pizza9x = (ProductsInCart[8][1])
        root.pizza10x = (ProductsInCart[9][1])
        root.pizza11x = (ProductsInCart[10][1])
        root.pizza12x = (ProductsInCart[11][1])

        print(ProductsInCart[index])

    def remove_product(self, index, root):
        if ProductsInCart[index][1] > 0:
            ProductsInCart[index][1] = ProductsInCart[index][1] - 1

        root.pizza1x = (ProductsInCart[0][1])
        root.pizza2x = (ProductsInCart[1][1])
        root.pizza3x = (ProductsInCart[2][1])
        root.pizza4x = (ProductsInCart[3][1])
        root.pizza5x = (ProductsInCart[4][1])
        root.pizza6x = (ProductsInCart[5][1])
        root.pizza7x = (ProductsInCart[6][1])
        root.pizza8x = (ProductsInCart[7][1])
        root.pizza9x = (ProductsInCart[8][1])
        root.pizza10x = (ProductsInCart[9][1])
        root.pizza11x = (ProductsInCart[10][1])
        root.pizza12x = (ProductsInCart[11][1])

        print(ProductsInCart[index])



class DrinkOrdering(Screen):
    drink1x = NumericProperty(ProductsInCart[12][1])
    drink2x = NumericProperty(ProductsInCart[13][1])
    drink3x = NumericProperty(ProductsInCart[14][1])
    drink4x = NumericProperty(ProductsInCart[15][1])
    drink5x = NumericProperty(ProductsInCart[16][1])
    drink6x = NumericProperty(ProductsInCart[17][1])
    drink7x = NumericProperty(ProductsInCart[18][1])
    drink8x = NumericProperty(ProductsInCart[19][1])
    drink9x = NumericProperty(ProductsInCart[20][1])
    drink10x = NumericProperty(ProductsInCart[21][1])
    drink11x = NumericProperty(ProductsInCart[22][1])
    drink12x = NumericProperty(ProductsInCart[23][1])

    def add_product(self, index, root):
        ProductsInCart[index][1] = ProductsInCart[index][1] + 1

        root.drink1x = (ProductsInCart[12][1])
        root.drink2x = (ProductsInCart[13][1])
        root.drink3x = (ProductsInCart[14][1])
        root.drink4x = (ProductsInCart[15][1])
        root.drink5x = (ProductsInCart[16][1])
        root.drink6x = (ProductsInCart[17][1])
        root.drink7x = (ProductsInCart[18][1])
        root.drink8x = (ProductsInCart[19][1])
        root.drink9x = (ProductsInCart[20][1])
        root.drink10x = (ProductsInCart[21][1])
        root.drink11x = (ProductsInCart[22][1])
        root.drink12x = (ProductsInCart[23][1])

        print(ProductsInCart[index])

    def remove_product(self, index, root):
        if ProductsInCart[index][1] > 0:
            ProductsInCart[index][1] = ProductsInCart[index][1] - 1

        root.drink1x = (ProductsInCart[12][1])
        root.drink2x = (ProductsInCart[13][1])
        root.drink3x = (ProductsInCart[14][1])
        root.drink4x = (ProductsInCart[15][1])
        root.drink5x = (ProductsInCart[16][1])
        root.drink6x = (ProductsInCart[17][1])
        root.drink7x = (ProductsInCart[18][1])
        root.drink8x = (ProductsInCart[19][1])
        root.drink9x = (ProductsInCart[20][1])
        root.drink10x = (ProductsInCart[21][1])
        root.drink11x = (ProductsInCart[22][1])
        root.drink12x = (ProductsInCart[23][1])

        print(ProductsInCart[index])


class CartScreen(Screen):
    def on_enter(self):
        items = ""
        amount_ordered = ""
        item_cost = ""
        subtotal_cost = ""
        for i in range(len(ProductsInCart)):
            if ProductsInCart[i][1] > 0:
                items += str(ProductsInCart[i][0]) + '\n'
                amount_ordered += str(ProductsInCart[i][1]) + '\n'
                item_cost += "$" + str(ProductsInCart[i][2]) + '\n'
                subtotal_cost += "$" + str(float(ProductsInCart[i][1] * ProductsInCart[i][2])) + '\n'
                PriceInfo[0] += float(ProductsInCart[i][1] * ProductsInCart[i][2])

        print(PriceInfo)
        PriceInfo[1] = round(PriceInfo[0] * .1, 2)
        PriceInfo[2] = round(PriceInfo[0] - PriceInfo[1], 2)

        print(PriceInfo)

        self.ids.itemnames.text = items
        self.ids.quantity.text = amount_ordered
        self.ids.item_cost.text = item_cost
        self.ids.totalitemcost.text = subtotal_cost
        self.ids.total.text = "GST: $" + str(float(PriceInfo[1])) + "\n" + "\n" + "Product Cost: $" + str(float(PriceInfo[2])) + '\n' + "\n" + "Total: $" + str(float(PriceInfo[0]))


class CheckoutScreen(Screen):
    def print_receipt(self, root):
        print('1:', PizzaOrdering.pizza1x)
        print('1:', PizzaOrdering.pizza2x)
        print('1:', PizzaOrdering.pizza3x)
        print('1:', PizzaOrdering.pizza4x)
        print('1:', PizzaOrdering.pizza5x)
        print('1:', PizzaOrdering.pizza6x)



class WindowManager(ScreenManager):
    pass


class PapasPizzas(MDApp):
    def build(self):
        return Builder.load_file('main.kv')


print(PizzaOrdering.pizza1x)
Window.fullscreen = 'auto'
PapasPizzas().run()
print(PizzaOrdering.pizza1x)
