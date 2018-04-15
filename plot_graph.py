from io import BytesIO
import urllib
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import numpy as np
import pandas as pd

def pg1(func):
	return func

def pg2(func):
	fig = Figure(dpi=120) #figsize=(8, 8)
	fig.subplots_adjust(left=0.075, bottom=0.05, right=0.95, top=0.97, wspace=0.15, hspace=0.15)
	ax = fig.add_subplot(1,1,1)
	xs = np.linspace(-np.pi, np.pi, 100)
	if func == 'sin':
		ys = np.sin(xs)
	elif func == 'cos':
		ys = np.cos(xs)
	elif func == 'tan':
		ys = np.tan(xs)
	else:
		ys = xs
	ax.plot(xs, ys)
	canvas = FigureCanvasAgg(fig)
	png_output = BytesIO()
	canvas.print_png(png_output)
	img_data = urllib.parse.quote(png_output.getvalue())
	return img_data

def pg3():
	num_points = 100
	gradient = 0.5
	x = np.array(range(num_points))
	y = np.random.randn(num_points) * 10 + x*gradient
	fig = Figure(dpi=120)
	fig.subplots_adjust(top=0.95)
	ax = fig.add_subplot(1,1,1)
	colors = np.random.rand(num_points)
	size = (2 + np.random.rand(num_points) * 8) ** 2
	ax.scatter(x, y, s=size, c=colors, alpha=0.5)
	canvas = FigureCanvasAgg(fig)
	png_output = BytesIO()
	canvas.print_png(png_output)
	img_data = urllib.parse.quote(png_output.getvalue())
	return img_data

def pg4():
	return