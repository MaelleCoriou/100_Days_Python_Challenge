travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#TODO: Write the function that will allow new countries

def add_new_country(new_country, new_visits, new_cities):
	new_dic = {}
	new_dic["country"] = new_country
	new_dic["visits"] = new_visits
	new_dic["cities"] = new_cities
	travel_log.append(new_dic)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



