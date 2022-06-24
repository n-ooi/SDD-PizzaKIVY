import datetime

print(str(datetime.datetime.now())[0:10])

from pathlib import Path

path = Path(str(datetime.datetime.now())[0:10] + '.csv')

if path.is_file():
    print('True')
else:
    print('False')



currentCSV = "/Users/nooi23/Desktop/Minor Project/SDDPizzaAssessmentMDv2-master-master/" + str(datetime.datetime.now())[0:10] + ".csv"
ff = open(currentCSV, "w+")

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

"""from kivy.core.window import Window
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class Test(Screen):
    pass

class TestApp(App):
    def build(self):  # Opening the App
        return Builder.load_file('test.kv')


Window.fullscreen = 'auto'  # Sets the app's default state to fullscreen
TestApp().run()  # Opens the app"""
