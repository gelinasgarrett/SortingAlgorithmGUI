from matplotlib import pyplot as plt, animation
from matplotlib.backends.backend_tkagg import (
	FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from tkinter import *
import random
import bubbleSort, insertionSort, selectionSort

def createAnimation(sortName,displayName, aLen):
	N = int(aLen)
	A = list(range(1, N + 1))
	random.shuffle(A)	
	name = sortName
	N = len(A)
	generator = eval(name + ".run" + name + "(A)")
	fig, ax = plt.subplots()
	ax.set_title(displayName)
	bar_sub = ax.bar(range(len(A)), A, align="edge")
		
	ax.set_xlim(0, N)
	text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
	iteration = [0]
		
	def update(A, rects, iteration):
			for rect, val in zip(rects, A):
					rect.set_height(val)
			iteration[0] += 1
			text.set_text(f"# of operations: {iteration[0]}")

	anim = animation.FuncAnimation(
			fig,
			func=update,
			fargs=(bar_sub, iteration),
			frames=generator,
			repeat=False,
			blit=False,
			interval=100,
			save_count=90000,
	)
	plt.show()
