import Bike

### Junk testing goes here.... 
my_bikeshop = Bike.BikeShop("Shop O'Bikes", {'Huffy': 10, 'Schwinn': 20}, {'Huffy':.25, 'Schwinn':.33})

print my_bikeshop.inventory

print my_bikeshop.inventory.values()
print my_bikeshop.inventory.items()

print my_bikeshop.inventory['Huffy']

print 'We have ', my_bikeshop.inventory['Huffy'], ' Huffys in stock.  We mark them up by ', my_bikeshop.margin['Huffy'], ' percent'

what_i_cleared = my_bikeshop.profit({'Huffy':5, 'Schwinn': 3},{'Huffy': 10, 'Schwinn': 20}, {'Huffy':.25, 'Schwinn':.33})

for items,moola in what_i_cleared.items():
	print 'The Shop made', moola, 'on the' , items


cust1 = Bike.Customers("Adam",200)
cust2 = Bike.Customers("Betty",10)
