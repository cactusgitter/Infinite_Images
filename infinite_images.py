# This is a program that will draw all possible black and white
# images that are within a 100 x 100 bounding box.

import kivy
kivy.require('1.11.1') 

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.graphics.instructions import Instruction
from kivy.lang import Builder
from kivy.clock import Clock

import random

from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '500')

class RootBoxLayout(BoxLayout):	
	def __init__(self, **kwargs):
		super(RootBoxLayout, self).__init__(**kwargs)
		self.event = None
		# create the matrix
		self.matrix = [[0 for x in range(10)] for x in range(10)] # a 10 x 10 grid
		print(self.matrix)
			
	def play(self):
		if self.event == None:
			self.event = Clock.schedule_interval(self.matrix_up, 0.00001) # new image every 0.1 seconds
		else:
			self.event.cancel()
			self.event = None
		
	def matrix_up(self, *args):
		"""Increment the matrix"""
		
		i = 0
		j = 0
		while i < 10:
			j = 0
			while j < 10:
				if self.matrix[i][j] == 0:	# If the current square is black
					self.matrix[i][j] = 1		
					
					# Done making the matrix
					i = 10 # Break out of the outer loop
					j = 10 # Break out of the inner loop
					
				else: # If the current square is white do this
					self.matrix[i][j] = 0					
				j += 1
			i += 1
		# Ready to draw the image
		self.draw_next_image()
				
	def draw_next_image(self, *args):
		self.ids.print_box.canvas.clear()
		
		with self.ids.print_box.canvas:
			"""Pixel here refers to a rectangle that represents pixels"""
			pixel_width = self.ids.print_box.width * 0.1    # how wide to draw the pixel
			pixel_height = self.ids.print_box.height * 0.1  # how tall to draw the pixel
			pixel_x = self.ids.print_box.x					# x position of the pixel
			pixel_y = self.ids.print_box.y					# y position of the pixel
			
			i = 0
			j = 0
			
			while i < 10:
				j = 0
				while j < 10:
					new_pos = (pixel_x + (j * pixel_width), pixel_y + (i * pixel_height))
				
					if self.matrix[i][j] == 0:	# If the matrix is 0
						Color(rgba=(0,0,0,1)) # Draw a black rectangle						
					else: # If the matrix is 1
						Color(rgba=(1,1,1,1)) # Draw a white rectangle
						
					Rectangle(pos = new_pos,
							  size = (pixel_width, pixel_height))
					j += 1
				i += 1
			
			# Draw the rectangle
			Rectangle(pos = new_pos,
					  size = (pixel_width, pixel_height))
		

class Main(App):
	def build(self):
		Builder.load_file("infinity.kv")
		root = RootBoxLayout()
		return root

if __name__ == '__main__':
	Main().run()
