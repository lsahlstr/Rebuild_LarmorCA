import matplotlib.pyplot as plt
import numpy as np

def simple_plot(arr):
	fig = plt.figure()
	plt.plot(arr)
	plt.show()
	
def simple_plot_overlay(arr1, arr2):
	fig = plt.figure()
	plt.plot(arr1)
	plt.plot(arr2)
	plt.show()
	