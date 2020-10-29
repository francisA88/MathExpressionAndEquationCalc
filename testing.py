#This file is for tests purposes only
#This is used to carry out quick tests and prototypes

from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.base import runTouchApp
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.togglebutton import ToggleButton

top = height = Window.height
right = width =Window.width
class Test(FloatLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.size_hint = None, None
		self.cursor_col=6
		self.btn = Button(text="sup", size=[width, 100], pos=[0,350], size_hint=[None, None])
		self.isSuperMode = False
		self.btn.height = 100
		self.inp = TextInput(multiline=False, size=[width, 100], pos=[0, top-100], size_hint=[None, None])
		self.btn.bind(on_release=self.changeMode)
		func=lambda y: self.inp.insert_text("\n"+" "*len(self.inp.text)+"_"*5+" "*len(self.inp.text))
		btn2=Button(text=r"\n", size_hint=[None, None], pos=[0,self.btn.top])
		btn2.bind(on_release=func)
		self.add_widget(btn2)
		self.add_widget(self.btn)
		self.add_widget(self.inp)
		
	def changeMode(self, m):
	#	initial = self.inp.padding_y
		if not self.isSuperMode:
			self.inp.padding_y[0]*=3
		else:
			self.inp.padding_y[0]=0
			
runTouchApp(Test())
help(TextInput.do_cursor_movement)	
print(dir(TextInput))
print(dir(ToggleButton))