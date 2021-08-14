# with open("weather_data.csv") as file:
#     # readlines to get each line
#     weather_data = file.readlines()
# print(weather_data)

import csv

with open("weather_data.csv") as file:
    data = csv.reader(file)
    temperature = []
    for temp in data:
        # get read of the temp line
        if temp[1] != "temp":
            # append the temp as int
            temperature.append(int(temp[1]))
    print(temperature)

import pandas as pd

data = pd.read_csv("weather_data.csv")
print(data)
temperatures = data.temp
print(temperatures)
data_dict = data.to_dict()
print(data_dict)
data_list = temperatures.to_list()
print(data_list)

# calculate average with pandas series
temperatures_avg = data.temp.mean()
print("Temperature average:\n", temperatures_avg)

# calculate average with a list
average = sum(data_list) / len(data_list)
print(average)

# get the max value
max_temp = data.temp.max()
print("Max temperature in dataframe:\n:", max_temp)

# filter data for monday
monday = data[data.day == "Monday"]
print("Monday temperature and condition :\n", monday)

# filter data max temp, which row has max temperature
data_max_temp = data[data.temp == data.temp.max()]
print("Data max temperature:\n", data_max_temp)

# Convert Monday temp to Fahrenheit


def convert_celsius_fahrenheit(column_value):
    convert = (column_value * 9/5) + 32
    return convert


celsius = data[data.day == "Monday"]
celsius.temp = convert_celsius_fahrenheit(celsius.temp)
print("Monday temp converted to Fahrenheit:\n", celsius)

# create dataframe from scratch
data_dic = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 80]
}
df = pd.DataFrame(data_dic)
print("Dataframe from scratch:\n", df)
df.to_csv("New_data.csv")