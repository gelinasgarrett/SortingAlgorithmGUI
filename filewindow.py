import tkinter as tk
import random
import time
from matplotlib import pyplot as plt, animation
from matplotlib.backends.backend_tkagg import (
	FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import bubbleSort, selectionSort, insertionSort

import numpy as np
from tkinter import *

root = Tk()
root.title('Algorithm Visualization Application')
root.geometry("600x200")

class AlgorithmApplication:
	def __init__(self, parent):
		welcomeFrame = Frame(parent)
		welcomeFrame.grid(row = 0, column = 0)

		self.bubbleSelectionState = tk.IntVar()
		self.selectionSelectionState = tk.IntVar()
		self.insertionSelectionState = tk.IntVar()

		self.bubbleSort = Checkbutton(parent,text="Bubble Sort", variable = self.bubbleSelectionState)
		self.bubbleSort.grid(row=0, column=0,padx=5,pady=5)

		self.selectionSort = Checkbutton(parent,text="Selection Sort", variable = self.selectionSelectionState)
		self.selectionSort.grid(row=0, column=1,padx=5,pady=5)

		self.insertionSort = Checkbutton(parent, text="Insertion Sort", variable = self.insertionSelectionState)
		self.insertionSort.grid(row = 0, column = 2,padx=5,pady=5)

		self.inputArrSizeLabel = Label(parent, text="Enter the length of the array to sort: ")
		self.inputArrSizeLabel.grid(row = 2, column = 1,padx=5,pady=5)
		self.inputArrSize = Entry(parent, width= 20)
		self.inputArrSize.grid(row = 3, column = 1,padx=5,pady=5)

		self.sortButton = Button(parent, text="Begin Sorting", command=lambda: self.mainWindow(self.bubbleSelectionState.get(), self.selectionSelectionState.get(),self.insertionSelectionState.get()) )
		self.sortButton.grid(row = 4, column = 1,padx=5,pady=5)
	

	def mainWindow(self, *args):
		selectionDict = {"bubbleSort.createBubbleSortAnim": args[0], 
											"selectionSort.createSelectionSortAnim": args[1], 
											"insertionSort.createInsertionSortAnim": args[2]}
		for key,val in selectionDict.items():
			if(val == 1):
				eval(key + "(self.inputArrSize.get())")
		

algoApp = AlgorithmApplication(root)
root.mainloop()
