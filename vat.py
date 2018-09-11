def price_no_vat(full_price, vat_rate):
	price_no_vat=full_price*100/(100+vat_rate)
	price=price_no_vat*(100+vat_rate)/100
	print('без ндс = ' )
	print(price_no_vat)

	print ('с ндс = ')
	print (price)


price1=118
vat_rate1=18
price_no_vat(price1, vat_rate1)
price_no_vat (100,18)