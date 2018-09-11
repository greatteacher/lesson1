def round_price(price):
	price = int(price)
	return 'Цена:'+str(price) + 'rubly'
display_price=round_price(56.78)
print(display_price)
