#from kivy.app import App

import sys

#please remove the following line
#sys.path.append("/storage/4251-1617/site-packages")

#from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition, NoTransition
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.core.window import Window
#from kivy.graphics import *
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.clock import Clock

from kivymd.uix.textfield import MDTextField as TextField
from kivymd.uix.toolbar import MDToolbar as Toolbar
from kivymd.uix.navigationdrawer import MDNavigationDrawer as NavigationDrawer, NavigationLayout
from kivymd.theming import ThemeManager
from kivymd.app import MDApp as App

#print(dir(NavigationDrawer))

Builder.load_file("layout.kv")
Builder.load_file("keyboard.kv")
Builder.load_file('calc_area.kv')

#print(dir(NavigationLayout))
#print(dir(Toolbar))

class SpecialInput(TextField):# pass
	def _bind_keyboard(self):
		if self._keyboard is None:
			self._requested_keyboard = 1
		super().on_focus()
		#self.hide_keyboard()
		self.bind(on_touch_down = self.unfocus)
	
	def on_focus(self, *arg):
		super().on_focus(*arg)
		#export current textfield to global space
		
	def unfocus(self, arg, touch):
		if (not self.collide_point(*touch.pos) and not self.parent.ids.solvebtn.collide_point(*touch.pos)):
			self.focus = False
	
class CalculationArea(ScrollView):
	current = ObjectProperty(None)
	def __init__(self, **kwargs):
		super(CalculationArea, self).__init__(**kwargs)
	#	Clock.schedule_interval(self.getCurrent, 1/65)
		self.spbtn = Factory.Spbutton()
		#self.spbtn.bind(on_press = self.putText)
		
	def on_touch_down(self, touch):
		super().on_touch_down(touch)
		#if touch falls below the last textfield, add another textfield to the calculation space
			#Window.add_widget(Factory.Field(width=Window.width, pos=[0,self.children[0].children[0].y]))
		


#These classes are used in the kv files{
class STrig(Screen): pass
class SHome(Screen): pass
		
class SEdit(Screen): pass
class SMisc(Screen): pass
#}

class Spbutton(Button): pass

class Keyboard(Widget):
	#numkeys = ObjectProperty(None)
	spbutton = Factory.Spbutton
	#s1 = S1()
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.area = CalculationArea()
		#self.current = "kblayout1"
		

		
class MainLayout(NavigationLayout):
	pass
	
class MainWidget(ScreenManager):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	

class CalcApp(App):
	#theme_cls =  ThemeManager()
	#print(dir(theme_cls))
	#theme_cls.primary_palette = "Teal"
	#theme_cls.primary_color =
	current = ObjectProperty(None)
					
	def build(self):
		self.main=MainWidget()
		
		return self.main
	
	@property
	def getMain(self):
		return self.main
	
	@property
	def getCurrent(self):
		'''Gets current working TextField'''
		#loop through all children in CalculationArea's gridlayout
		for child in self.main.ids.calcArea.ids.container.children:
			for ch in child.children:
				if issubclass(ch.__class__, TextField):
					if ch.focused:
						return ch
	
	
if __name__=="__main__":		
	CalcApp().run()