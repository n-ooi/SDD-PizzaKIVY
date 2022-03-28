from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.properties import ListProperty, NumericProperty, StringProperty, ReferenceListProperty
import time


class PizzaOrdering(Screen):
    sumPQ = NumericProperty(0)
    sumPP = NumericProperty(0)
    pizza1x = NumericProperty(0)
    pizza2x = NumericProperty(0)
    pizza3x = NumericProperty(0)
    pizza4x = NumericProperty(0)
    pizza5x = NumericProperty(0)
    pizza6x = NumericProperty(0)
    pizza7x = NumericProperty(0)
    pizza8x = NumericProperty(0)
    pizza9x = NumericProperty(0)
    pizza10x = NumericProperty(0)
    pizza11x = NumericProperty(0)
    pizza12x = NumericProperty(0)
    pizzas = ListProperty([pizza1x,pizza2x,pizza3x,pizza4x,pizza5x,pizza6x,pizza7x,pizza8x,pizza9x,pizza10x,pizza11x,pizza12x])

    def sum_pizzas(self, root):
        root.sumPQ = root.pizza1x + root.pizza2x + root.pizza3x + root.pizza4x + root.pizza5x + root.pizza6x + root.pizza7x + root.pizza8x + root.pizza9x + root.pizza10x + root.pizza11x + root.pizza12x

    def sum_pizza_price(self, root):
        root.sumPP = root.pizza1x*18.5 + root.pizza2x*18.0 + root.pizza3x*19.5 + root.pizza4x*20.0 + root.pizza5x*18.5 + root.pizza6x*16.0 + root.pizza7x*11.5 + root.pizza8x*12.5 + root.pizza9x*17.0 + root.pizza10x*16.5 + root.pizza11x*18 + root.pizza12x*17.0

    def n_plus1(self,root):
        root.pizza1x +=1
        # root.sum = sum(pizzas)

    def n_minus1(self,root):
        if root.pizza1x > 0:
            root.pizza1x += -1

    def n_plus2(self, root):
        root.pizza2x += 1

    def n_minus2(self, root):
        if root.pizza2x > 0:
            root.pizza2x += -1

    def n_plus3(self, root):
        root.pizza3x += 1

    def n_minus3(self, root):
        if root.pizza3x > 0:
            root.pizza3x += -1

    def n_plus4(self, root):
        root.pizza4x += 1

    def n_minus4(self, root):
        if root.pizza4x > 0:
            root.pizza4x += -1

    def n_plus5(self, root):
        root.pizza5x += 1

    def n_minus5(self, root):
        if root.pizza5x > 0:
            root.pizza5x += -1

    def n_plus6(self,root):
        root.pizza6x +=1

    def n_minus6(self,root):
        if root.pizza6x > 0:
            root.pizza6x += -1

    def n_plus7(self, root):
        root.pizza7x += 1

    def n_minus7(self, root):
        if root.pizza7x > 0:
            root.pizza7x += -1

    def n_plus8(self, root):
        root.pizza8x += 1

    def n_minus8(self, root):
        if root.pizza8x > 0:
            root.pizza8x += -1

    def n_plus9(self, root):
        root.pizza9x += 1

    def n_minus9(self, root):
        if root.pizza9x > 0:
            root.pizza9x += -1

    def n_plus10(self, root):
        root.pizza10x += 1

    def n_minus10(self, root):
        if root.pizza10x > 0:
            root.pizza10x += -1

    def n_plus11(self, root):
        root.pizza11x += 1

    def n_minus11(self, root):
        if root.pizza11x > 0:
            root.pizza11x += -1

    def n_plus12(self, root):
        root.pizza12x += 1

    def n_minus12(self, root):
        if root.pizza12x > 0:
            root.pizza12x += -1

    def printstuff(self):
        pass


class DrinkOrdering(Screen):
    sumDQ = NumericProperty(0)
    sumDP = NumericProperty(0)
    drink1x = NumericProperty(0)
    drink2x = NumericProperty(0)
    drink3x = NumericProperty(0)
    drink4x = NumericProperty(0)
    drink5x = NumericProperty(0)
    drink6x = NumericProperty(0)
    drink7x = NumericProperty(0)
    drink8x = NumericProperty(0)
    drink9x = NumericProperty(0)
    drink10x = NumericProperty(0)
    drink11x = NumericProperty(0)
    drink12x = NumericProperty(0)

    def sum_drinks(self, root):
        root.sumDQ = root.drink1x + root.drink2x + root.drink3x + root.drink4x + root.drink5x + root.drink6x + root.drink7x + root.drink8x + root.drink9x + root.drink10x + root.drink11x + root.drink12x

    def sum_drink_price(self, root):
        root.sumDP = root.drink1x*4.5 + root.drink2x*4.5 + root.drink3x*4.5 + root.drink4x*4.5 + root.drink5x*1.0 + root.drink6x*2.0 + root.drink7x*6.5 + root.drink8x*6.5 + root.drink9x*10.5 + root.drink10x*10.5 + root.drink11x*10.5 + root.drink12x*10.5

    def n_plus1(self,root):
        root.drink1x +=1

    def n_minus1(self,root):
        if root.drink1x > 0:
            root.drink1x += -1

    def n_plus2(self, root):
        root.drink2x += 1

    def n_minus2(self, root):
        if root.drink2x > 0:
            root.drink2x += -1

    def n_plus3(self, root):
        root.drink3x += 1

    def n_minus3(self, root):
        if root.drink3x > 0:
            root.drink3x += -1

    def n_plus4(self, root):
        root.drink4x += 1

    def n_minus4(self, root):
        if root.drink4x > 0:
            root.drink4x += -1

    def n_plus5(self, root):
        root.drink5x += 1

    def n_minus5(self, root):
        if root.drink5x > 0:
            root.drink5x += -1

    def n_plus6(self,root):
        root.drink6x +=1

    def n_minus6(self,root):
        if root.drink6x > 0:
            root.drink6x += -1

    def n_plus7(self, root):
        root.drink7x += 1

    def n_minus7(self, root):
        if root.drink7x > 0:
            root.drink7x += -1

    def n_plus8(self, root):
        root.drink8x += 1

    def n_minus8(self, root):
        if root.drink8x > 0:
            root.drink8x += -1

    def n_plus9(self, root):
        root.drink9x += 1

    def n_minus9(self, root):
        if root.drink9x > 0:
            root.drink9x += -1

    def n_plus10(self, root):
        root.drink10x += 1

    def n_minus10(self, root):
        if root.drink10x > 0:
            root.drink10x += -1

    def n_plus11(self, root):
        root.drink11x += 1

    def n_minus11(self, root):
        if root.drink11x > 0:
            root.drink11x += -1

    def n_plus12(self, root):
        root.drink12x += 1

    def n_minus12(self, root):
        if root.drink12x > 0:
            root.drink12x += -1

    def printstuff(self):
        pass


class CartScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class PapasPizzas(MDApp):
    def build(self):
        return Builder.load_file('main.kv')


Window.fullscreen = 'auto'
PapasPizzas().run()

