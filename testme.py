import Bike

bikes_to_sell = ['Huffy','Schwinn','ModelA','Neato','Turbo','Junky']

bike_list = []
bike_inventory = {}
bike_wholesale = {}

for index, bikes in enumerate(bikes_to_sell):
	print bikes
	bike_list.append(Bike.Bicycle(bikes,0,1))	
	print bike_list

for bike in bike_list:
	print bike.model
	print bike.weight
	print bike.production_cost

	
my_bikeshop = Bike.BikeShop("Shop O'Bikes", {'Huffy': 1, 'Schwinn': 2, 'ModelA':1,'Neato':1,'Turbo':1,'Junky':3}, {'Huffy': .2, 'Schwinn': .2, 'ModelA':.2,'Neato':.2,'Turbo':.2,'Junky':.2})

#Huffy = Bike.Bicycle("Huffy",10,182.00)
#Schwinn = Bike.Bicycle("Schwinn",10,800.00)
#ModelA = Bike.Bicycle("ModelA",10,900.00)
#Neato = Bike.Bicycle("Neato",8,201.00)
#Turbo = Bike.Bicycle("Turbo",10,800.00)
#Junky = Bike.Bicycle("Junky",15,90.00)


cust1 = Bike.Customers("Adam",200)
cust2 = Bike.Customers("Betty",500)
cust3 = Bike.Customers("Charlie",1000)


#cust1.what_can_i_buy(Neato)