from tabulate import tabulate
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import pandas as pd
import datetime
from pathlib import Path
import subprocess
import sys

# All my imports are listed above

# An array of arrays storing the data for:
# the name of every item, the quantity ordered as well as the price of the item
# Structure: ["Name", Quantity, Price]
items_ordered = [["Vegan Roasted Pineapple", 0, 18.50], ["Tandoori Chicken", 0, 18], ["Chicken 'n' Avo", 0, 19.50],
                 ["Beef 'n' Shrooms", 0, 20], ["Mary's Little Lamb", 0, 18.5], ["Egg 'n' Bacon", 0, 16],
                 ["Basic Margherita", 0, 11.50], ["Aloha", 0, 12.50], ["Veges 'n' Veges", 0, 17],
                 ["Gourmet Pepperoni", 0, 16.50], ["Peri Peri", 0, 18], ["Mystery Meat", 0, 17.00],

                 ["Sprite", 0, 4.50], ["Coca Cola", 0, 4.50], ["Solo", 0, 4.50],
                 ["Fanta", 0, 4.50], ["Bottled Water", 0, 1], ["Lightly Sparkling Water", 0, 2],
                 ["Ice Coffee", 0, 6.50], ["Kombucha", 0, 6.50], ["Choccy Shake", 0, 10.50],
                 ["Berry Good Shake", 0, 10.50], ["Vanilla Shake", 0, 10.50], ["Caramel Shake", 0, 10.50]]
print(sys.getsizeof(items_ordered))


class PizzaOrdering(Screen):
    # These values set the number visible on the item to the quantity of that item in the cart
    pizza1x = NumericProperty(items_ordered[0][1])
    pizza2x = NumericProperty(items_ordered[1][1])
    pizza3x = NumericProperty(items_ordered[2][1])
    pizza4x = NumericProperty(items_ordered[3][1])
    pizza5x = NumericProperty(items_ordered[4][1])
    pizza6x = NumericProperty(items_ordered[5][1])
    pizza7x = NumericProperty(items_ordered[6][1])
    pizza8x = NumericProperty(items_ordered[7][1])
    pizza9x = NumericProperty(items_ordered[8][1])
    pizza10x = NumericProperty(items_ordered[9][1])
    pizza11x = NumericProperty(items_ordered[10][1])
    pizza12x = NumericProperty(items_ordered[11][1])

    def add_product(self, index, root):
        items_ordered[index][1] = items_ordered[index][1] + 1
        # when this button is pressed it increments the quantity ordered

        # this updates all the values
        root.pizza1x = (items_ordered[0][1])
        root.pizza2x = (items_ordered[1][1])
        root.pizza3x = (items_ordered[2][1])
        root.pizza4x = (items_ordered[3][1])
        root.pizza5x = (items_ordered[4][1])
        root.pizza6x = (items_ordered[5][1])
        root.pizza7x = (items_ordered[6][1])
        root.pizza8x = (items_ordered[7][1])
        root.pizza9x = (items_ordered[8][1])
        root.pizza10x = (items_ordered[9][1])
        root.pizza11x = (items_ordered[10][1])
        root.pizza12x = (items_ordered[11][1])

    def remove_product(self, index, root):
        if items_ordered[index][1] > 0:  # As long as the amount is >0 this button will decrement the quantity
            items_ordered[index][1] = items_ordered[index][1] - 1

        # this updates all the values
        root.pizza1x = (items_ordered[0][1])
        root.pizza2x = (items_ordered[1][1])
        root.pizza3x = (items_ordered[2][1])
        root.pizza4x = (items_ordered[3][1])
        root.pizza5x = (items_ordered[4][1])
        root.pizza6x = (items_ordered[5][1])
        root.pizza7x = (items_ordered[6][1])
        root.pizza8x = (items_ordered[7][1])
        root.pizza9x = (items_ordered[8][1])
        root.pizza10x = (items_ordered[9][1])
        root.pizza11x = (items_ordered[10][1])
        root.pizza12x = (items_ordered[11][1])


class DrinkOrdering(Screen):
    # These values set the number visible on the item to the quantity of that item in the cart
    drink1x = NumericProperty(items_ordered[12][1])
    drink2x = NumericProperty(items_ordered[13][1])
    drink3x = NumericProperty(items_ordered[14][1])
    drink4x = NumericProperty(items_ordered[15][1])
    drink5x = NumericProperty(items_ordered[16][1])
    drink6x = NumericProperty(items_ordered[17][1])
    drink7x = NumericProperty(items_ordered[18][1])
    drink8x = NumericProperty(items_ordered[19][1])
    drink9x = NumericProperty(items_ordered[20][1])
    drink10x = NumericProperty(items_ordered[21][1])
    drink11x = NumericProperty(items_ordered[22][1])
    drink12x = NumericProperty(items_ordered[23][1])

    def add_product(self, index, root):
        items_ordered[index][1] = items_ordered[index][1] + 1
        # when this button is pressed it increments the quantity ordered

        # this updates all the values
        root.drink1x = (items_ordered[12][1])
        root.drink2x = (items_ordered[13][1])
        root.drink3x = (items_ordered[14][1])
        root.drink4x = (items_ordered[15][1])
        root.drink5x = (items_ordered[16][1])
        root.drink6x = (items_ordered[17][1])
        root.drink7x = (items_ordered[18][1])
        root.drink8x = (items_ordered[19][1])
        root.drink9x = (items_ordered[20][1])
        root.drink10x = (items_ordered[21][1])
        root.drink11x = (items_ordered[22][1])
        root.drink12x = (items_ordered[23][1])

    def remove_product(self, index, root):
        if items_ordered[index][1] > 0:  # As long as the amount is >0 this button will decrement the quantity
            items_ordered[index][1] = items_ordered[index][1] - 1

        # this updates all the values
        root.drink1x = (items_ordered[12][1])
        root.drink2x = (items_ordered[13][1])
        root.drink3x = (items_ordered[14][1])
        root.drink4x = (items_ordered[15][1])
        root.drink5x = (items_ordered[16][1])
        root.drink6x = (items_ordered[17][1])
        root.drink7x = (items_ordered[18][1])
        root.drink8x = (items_ordered[19][1])
        root.drink9x = (items_ordered[20][1])
        root.drink10x = (items_ordered[21][1])
        root.drink11x = (items_ordered[22][1])
        root.drink12x = (items_ordered[23][1])


pricing_info = [0, 0, 0]  # [Total Cost, Amount of GST, Cost excluding GST]


class CartScreen(Screen):
    def on_enter(self):
        pricing_info = [0, 0, 0]  # resets the value of pricing_info to prepare for calculations
        items = ""  # sets all values to nothing so that they start off empty
        amount_ordered = ""
        item_cost = ""
        subtotal_cost = ""
        for i in range(len(items_ordered)):
            if items_ordered[i][1] > 0:  # makes sure that it only displays items bought
                items += str(items_ordered[i][0]) + '\n'  # progressively makes a list of all items bought
                amount_ordered += str(items_ordered[i][1]) + '\n'  # progressively makes a list of the quantities
                item_cost += "$" + str(items_ordered[i][2]) + '\n'  # progressively makes a list of the individual costs
                subtotal_cost += "$" + str(float(items_ordered[i][1] * items_ordered[i][
                    2])) + '\n'  # progressively makes a list of the total costs of each item
                pricing_info[0] += float(items_ordered[i][1] * items_ordered[i][2])

        pricing_info[1] = round(pricing_info[0] * (1 / 11), 2)  # calculates GST to 2 decimal points
        pricing_info[2] = round(pricing_info[0] - pricing_info[1], 2)  # calculates total - excluding GST

        # sets all the labels on the GUI to the values calculated
        self.ids.itemnames.text = items
        self.ids.quantity.text = amount_ordered
        self.ids.item_cost.text = item_cost
        self.ids.totalitemcost.text = subtotal_cost
        self.ids.total.text = "GST: $" + str(float(pricing_info[1])) + "\n" + "\n" + "Product Cost: $" + str(
            float(pricing_info[2])) + '\n' + "\n" + "Total: $" + str(float(pricing_info[0]))


receipt_time = [['']]  # sets a global variable for receipt_time


class CheckoutScreen(Screen):

    def print_receipt(self, root):
        dbpath = 'Databases/' + str(datetime.datetime.now())[0:10] + '.csv'
        if Path(dbpath).is_file():
            print('File Exists')
        else:
            print('Creating New Database')
            dbpath = "Databases/" + str(
                datetime.datetime.now())[0:10] + ".csv"
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

        pricing_info = [0, 0, 0]  # resets pricing_info for calculations
        df = pd.read_csv(dbpath)  # using the 'Pandas' library begins reading the csv file
        df = df[['ItemType', 'Quantity']]  # finds the two columns named 'ItemType' and 'Quantity'
        importedQuantities = [*df['Quantity']]  # creates an array of all the quantities listed in the csv file
        for i in range(0, 24):  # for every value in the array increments it by the amount ordered in the cart
            importedQuantities[i] += items_ordered[i][1]

        df['Quantity'] = importedQuantities  # updates the column in the database to new values
        df.to_csv(dbpath)  # updates the csv file

        # Sets the receipt name to the current time (to the second)
        receipt_time[0] = datetime.datetime.now().strftime("%c")

        # Creates a new file in the folder
        filename = "Receipts/" + str(
            receipt_time[0]) + ".txt"
        f = open(filename, "w+")
        receipt_data = "Order processed at" + ' ' + str(receipt_time[0]) + '\n\n'

        # Displays the first row of the table
        receipt_data += "+-------------------------+---------------+----------+----------+\n" \
                        "|      Product Name       |    Quantity   |   Cost   | Subtotal | \n" \
                        "+-------------------------+---------------+----------+----------+"
        for i in range(len(items_ordered)):
            if items_ordered[i][1] > 0:
                # This adds each of the pricing info for each item with formatting to line up with the table
                receipt_data += "\n| " + str(items_ordered[i][0]) \
                                + str(" " * (24 - len(items_ordered[i][0]))) \
                                + "|       " + str(items_ordered[i][1]) \
                                + " " * (8 - len(str(items_ordered[i][1]))) \
                                + "|   $" + str(items_ordered[i][2]) \
                                + " " * (6 - len(str(items_ordered[i][2]))) \
                                + "|  $" + str(items_ordered[i][2] * items_ordered[i][1]) \
                                + " " * (7 - len(str(items_ordered[i][2] * items_ordered[i][1]))) \
                                + "|"

                pricing_info[0] += float(items_ordered[i][1] * items_ordered[i][2])
        # This adds the bottom of the table
        receipt_data += "\n+-------------------------+---------------+----------+----------+"

        pricing_info[1] = round(pricing_info[0] * (1 / 11), 2)  # calculates GST
        pricing_info[2] = round(pricing_info[0] - pricing_info[1], 2)  # calculates Product Cost

        # adds pricing info at the bottom of the receipt
        receipt_data += "\nGST: $" + str(pricing_info[1]) + "\n" + "Product Cost: $" + str(
            pricing_info[2]) + '\n' + "Total: $" + str(int(pricing_info[0]))

        f.write(receipt_data)
        f.close()  # closes the file

    def validcc(self, ccnumber, ccexpiry, cvv, ccname, root):
        # checks if the credit card number is an integer and between 8 and 19 characters
        if ccnumber.replace(' ', '').isdecimal() and 8 <= len(ccnumber.replace(' ', '')) <= 19:
            print(str(sys.getsizeof(ccnumber)) + ' cc')
            # checks if the date is a valid date in correct format
            if ccexpiry.replace('/', '').isdecimal() and len(ccexpiry) == 5:
                print(str(sys.getsizeof(ccexpiry)) + ' exp')
                # checks if the cvv is an integer and either 3 or 4 characters
                if cvv.isdecimal() and (len(cvv) == 4 or len(cvv) == 3):
                    print(str(sys.getsizeof(cvv)) + ' cvv')
                    # checks if a ccname has been entered
                    if ccname:
                        print(str(sys.getsizeof(ccname)) + ' name')
                        # if all conditions are met returns True enabling the button
                        return True
        # return True ## for testing purposes


class Thx(Screen):
    def open_receipt(self, root):
        rpath = "Receipts/" + str(receipt_time[0]) + ".txt"  # creates a variable for the location of the receipt
        subprocess.call(('open', rpath))  # opens the receipt

    def open_db(self, root):
        date = str(datetime.datetime.now())[0:10]  # sets variable to today's date

        # creates two buttons for use in the dialog box later
        closeButton = MDFlatButton(text='Close', on_release=self.close_dialog)
        fileLocation = MDFlatButton(text='View in Excel', on_release=self.open_dbpath)

        df = pd.read_csv('Databases/' + str(datetime.datetime.now())[
                                        0:10] + '.csv')  # opens the database associated with today's date
        df = df[["ItemType", "Quantity"]]  # selects the main two columns

        # creates the dialog box
        self.dialog = MDDialog(title='Database for ' + date + '.',
                               text=tabulate(df, headers='keys'),
                               size_hint=(0.4, 1),
                               buttons=[fileLocation, closeButton])
        self.dialog.open()  # opens the dialog box

    def close_dialog(self, obj):
        self.dialog.dismiss()  # closes the dialog box

    def open_dbpath(self, root):
        dbpath = 'Databases/' + str(datetime.datetime.now())[0:10] + '.csv'
        subprocess.call(('open', dbpath))  # opens the database


class WindowManager(ScreenManager):  # this class defines the ScreenManager
    pass


class PapasPizzas(MDApp):
    def build(self):  # Opening the App
        return Builder.load_file('main.kv')

    def stop(self):  # Closing the App
        self.stop()

    def restart(self):  # Restarting the App
        for i in range(len(items_ordered)):
            items_ordered[i][1] = 0


Window.fullscreen = 'auto'  # Sets the app's default state to fullscreen
PapasPizzas().run()  # Opens the app
