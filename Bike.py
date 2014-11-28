class Bicycle(object):
	def __init__(self, model, weight, production_cost):
		self.model = model
		self.weight = weight
		self.production_cost = production_cost
		
		
class BikeShop(object):
	def __init__(self,shop_name,inventory,margin):
		self.shop_name = shop_name
		self.inventory  = inventory # pass in inventory as dictionary  item(bike): value(qty on hand)
		self.margin  = margin #pass in same item as in inventory but value will be margin as percent of cost
	def profit(self,inventory_sold, cost, margin):
		#iterate dict inventory sold... for each item:  #sold * prod_cost * margin
		return_profit = {}
		for bikes, bikes_sold in inventory_sold.items():
			cost_of = cost[bikes]
			margin_of = margin[bikes]
			return_profit[bikes] = bikes_sold * cost_of * margin_of
		return return_profit
	
	
class Customers(object):
	def __init__(self,name,bike_fund):
		self.name = name
		self.bike_fund = bike_fund
	def what_can_i_buy(self,model):
		if self.bike_fund > model.production_cost:
			print '>'
		else:
			print '<'
		




