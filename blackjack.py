"""The game of blackjack"""
import tkinter as tk

"""
Ace 2660 
Club 2663
Heart 2665
Diamond 2666
"""


def main():
	width = 1100
	height = 600

	root = tk.Tk()
	canvas = tk.Canvas(root, width=width, height=height)

	# fill canvas with green background
	canvas.create_rectangle(0, 0, width, height, fill='green')

	# Draw card
	# card_width = width * .10
	# card_height = height * .25

	# temp card size
	card_width = width * .3
	card_height = height * .75

	# center of card
	center_x = card_width / 2
	center_y = card_height / 2

	# card coords
	x1 = (width / 2) - center_x
	y1 = (height / 2) - center_y
	x2 = x1 + card_width
	y2 = y1 + card_height

	# create card white background
	canvas.create_rectangle(x1, y1, x2, y2, fill='white')
	
	# create symbol on card
	font_size = 128
	spade = chr(0x2660)
	center_symbol_x = center_x + x1
	center_symbol_y = center_y + y1

	canvas.create_text(center_symbol_x, center_symbol_y, text=spade, font=('', font_size))

	value_font_size = int(font_size * 0.3)
	
	corner_x_offset = x1 * 0.1
	corner_y_value_offset = y1 * 0.5

	top_left_x = x1 + corner_x_offset
	top_left_value_y = y1 + corner_y_value_offset
	
	bot_right_x = x2 - corner_x_offset
	bot_right_value_y = y2 - corner_y_value_offset

	top_left_symbol_y = y1 + (corner_y_value_offset * 2)
	bot_right_symbol_y = y2 - (corner_y_value_offset * 2)

	canvas.create_text(top_left_x, top_left_value_y,
		text="A", font=('', value_font_size))
	canvas.create_text(top_left_x, top_left_symbol_y,
		text=spade, font=('', value_font_size))
	canvas.create_text(bot_right_x, bot_right_value_y,
		text="A", font=('', value_font_size), angle=180)
	canvas.create_text(bot_right_x, bot_right_symbol_y,
		text=spade, font=('', value_font_size), angle=180)


	canvas.pack()
	root.mainloop()


if __name__ == "__main__":
	main()
