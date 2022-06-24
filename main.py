from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
import csv
import random
import pandas as pd
import datetime
from pathlib import Path
import subprocess
# All my imports are listed above

# An array of arrays storing the data for:
# the name of every item, the quantity ordered as well as the price of the item
# For Example: ["Name", Quantity, Price]
CartItems = [["Vegan Roasted Pineapple", 0, 18.50], ["Tandoori Chicken", 0, 18], ["Chicken 'n' Avo", 0, 19.50],
             ["Beef 'n' Shrooms", 0, 20], ["Mary's Little Lamb", 0, 18.5], ["Egg 'n' Bacon", 0, 16],
             ["Basic Margherita", 0, 11.50], ["Aloha", 0, 12.50], ["Veges 'n' Veges", 0, 17],
             ["Gourmet Pepperoni", 0, 16.50], ["Peri Peri", 0, 18], ["Mystery Meat", 0, 17.00],

             ["Sprite", 0, 4.50], ["Coca Cola", 0, 4.50], ["Solo", 0, 4.50],
             ["Fanta", 0, 4.50], ["Bottled Water", 0, 1], ["Lightly Sparkling Water", 0, 2],
             ["Ice Coffee", 0, 6.50], ["Kombucha", 0, 6.50], ["Choccy Shake", 0, 10.50],
             ["Berry Good Shake", 0, 10.50], ["Vanilla Shake", 0, 10.50], ["Caramel Shake", 0, 10.50]]

PriceInfo = [0, 0, 0] # [Total Cost, Amount of GST, Cost excluding GST]


class PizzaOrdering(Screen):
    # These values set the number visible on the item to the quantity of that item in the cart
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
        # when this button is pressed it increments the quantity ordered

        # this updates all the values
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

    def remove_product(self, index, root):
        if CartItems[index][1] > 0: # As long as the amount is >0 this button will decrement the quantity
            CartItems[index][1] = CartItems[index][1] - 1

        # this updates all the values
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

class DrinkOrdering(Screen):
    # These values set the number visible on the item to the quantity of that item in the cart
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
        # when this button is pressed it increments the quantity ordered

        # this updates all the values
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

    def remove_product(self, index, root):
        if CartItems[index][1] > 0:  # As long as the amount is >0 this button will decrement the quantity
            CartItems[index][1] = CartItems[index][1] - 1

        # this updates all the values
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

class CartScreen(Screen):
    def on_enter(self):
        PriceInfo = [0, 0, 0]  # resets the value of PriceInfo to prepare for calculations
        items = "" # sets all values to nothing so that they start off empty
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

        PriceInfo[1] = round(PriceInfo[0] * (1 / 11), 2)  # calculates GST to 2 decimal points
        PriceInfo[2] = round(PriceInfo[0] - PriceInfo[1], 2)  # calculates total - excluding GST

        # sets all the labels on the GUI to the values calculated
        self.ids.itemnames.text = items
        self.ids.quantity.text = amount_ordered
        self.ids.item_cost.text = item_cost
        self.ids.totalitemcost.text = subtotal_cost
        self.ids.total.text = "GST: $" + str(float(PriceInfo[1])) + "\n" + "\n" + "Product Cost: $" + str(
            float(PriceInfo[2])) + '\n' + "\n" + "Total: $" + str(float(PriceInfo[0]))


receiptno = [['']]  # sets a global variable for receiptno


class CheckoutScreen(Screen):

    def print_receipt(self, root):
        dbpath = 'Databases/' + str(datetime.datetime.now())[0:10] + '.csv'
        if Path(dbpath).is_file():
            print('File Exists')
        else:
            print('Creating New Database')
            dbpath = "/Users/nooi23/Desktop/Minor Project/SDDPizzaAssessmentMDv2-master-master/Databases/" + str(datetime.datetime.now())[0:10] + ".csv"
            ff = open(dbpath, "w+")
            ff.write(""",ItemType,Quantity
0,Vegan Roasted Pineapple,0
1,Tandoori Chicken,0
2,Chicken 'n' Avo,0
3,Beef 'n' Shrooms,0
4,Mary's Little Lamb,0
5,Egg 'n' Bacon,0
6,Basic Margherita,0
7,Aloha,0
8,Veges 'n' Veges,0
9,Gourmet Pepperoni,0
10,Peri Peri,0
11,Mystery Meat,0
12,Sprite,0
13,Coca Cola,0
14,Solo,0
15,Fanta,0
16,Bottled Water,0
17,Lightly Sparkling Water,0
18,Ice Coffee,0
19,Kombucha,0
20,Choccy Shake,0
21,Berry Good Shake,0
22,Vanilla Shake,0
23,Caramel Shake,0""")

            ff.close()

        PriceInfo = [0, 0, 0] # resets PriceInfo for calculations
        df = pd.read_csv(dbpath) # using the 'Pandas' library begins reading the csv file
        df = df[['ItemType', 'Quantity']]  # finds the two columns named 'ItemType' and 'Quantity'
        importedQuantities = [*df['Quantity']]  # creates an array of all the quantities listed in the csv file
        for i in range(0, 24):  # for every value in the array increments it by the amount ordered in the cart
            importedQuantities[i] += CartItems[i][1]

        df['Quantity'] = importedQuantities  # updates the column in the database to new values
        df.to_csv(dbpath)  # updates the csv file

        # Sets the receipt name to the current time (to the second)
        receiptno[0] = datetime.datetime.now().strftime("%c")

        # Creates a new file in the folder
        filename = "/Users/nooi23/Desktop/Minor Project/SDDPizzaAssessmentMDv2-master-master/Receipts/" + str(
            receiptno[0]) + ".txt"
        f = open(filename, "w+")
        RContent = "RECEIPT" + ' ' + str(receiptno[0]) + '\n\n'

        # Displays the first row of the table
        RContent += "+-------------------------+---------------+----------+----------+\n" \
                    "|      Product Name       |    Quantity   |   Cost   | Subtotal | \n" \
                    "+-------------------------+---------------+----------+----------+"
        for i in range(len(CartItems)):
            if CartItems[i][1] > 0:
                # This adds each of the pricing info for each item with formatting to line up with the table
                RContent += "\n| " + str(CartItems[i][0]) \
                            + str(" " * (24 - len(CartItems[i][0]))) \
                            + "|       " + str(CartItems[i][1]) \
                            + " " * (8 - len(str(CartItems[i][1]))) \
                            + "|   $" + str(CartItems[i][2]) \
                            + " " * (6 - len(str( CartItems[i][2]))) \
                            + "|  $" + str(CartItems[i][2]*CartItems[i][1]) \
                            + " " * (7 - len(str(CartItems[i][2]*CartItems[i][1]))) \
                            + "|"

                PriceInfo[0] += float(CartItems[i][1] * CartItems[i][2])
        # This adds the bottom of the table
        RContent += "\n+-------------------------+---------------+----------+----------+"

        PriceInfo[1] = round(PriceInfo[0] * (1 / 11), 2)  # calculates GST
        PriceInfo[2] = round(PriceInfo[0] - PriceInfo[1], 2)  # calculates Product Cost

        # adds pricing info at the bottom of the receipt
        RContent += "\nGST: $" + str(PriceInfo[1]) + "\n" + "Product Cost: $" + str(
            PriceInfo[2]) + '\n' + "Total: $" + str(int(PriceInfo[0]))

        f.write(RContent)
        f.close()  # closes the file

    def validcc(self, number, expiry, cvv, name, root):
        # checks if the credit card number is a integer and between 8 and 19 characters
        if number.replace(' ', '').isdecimal() and 8 <= len(number.replace(' ', '')) <= 19:
            # checks if the date is a valid date in correct format
            if expiry.replace('/', '').isdecimal() and len(expiry) == 5:
                # checks if the cvv is an integer and either 3 or 4 characters
                if cvv.isdecimal() and (len(cvv) == 4 or len(cvv) == 3):
                    # checks if a name has been entered
                    if name:
                        # if all conditions are met returns True enabling the button
                        return True
        # return True ## for testing purposes


class Thx(Screen):
    def open_receipt(self, root):
        rpath = "Receipts/" + str(receiptno[0]) + ".txt"  # creates a variable for the location of the receipt
        subprocess.call(('open', rpath))  # opens the receipt

    def open_db(self, root):
        dbpath = 'Databases/' + str(datetime.datetime.now())[0:10]+ '.csv'
        subprocess.call(('open', dbpath))  # opens the database


class WindowManager(ScreenManager): # this class defines the ScreenManager
    pass


class PapasPizzas(MDApp):
    def build(self):  # Opening the App
        return Builder.load_file('main.kv')

    def restart(self):  # Restarting the App
        self.root.clear_widgets()
        self.stop()
        return PapasPizzas().run()

    def stop(self):  # Closing the App
        self.stop()


Window.fullscreen = 'auto'  # Sets the app's default state to fullscreen
PapasPizzas().run()  # Opens the app
