
import csv
import pandas

# with open("weather-data.csv") as data:
#     data_file = csv.reader(data)
#     temperatures = []
#
#     for row in data_file:
#         temperatures.append(int(row[1]))
#
#     print(temperatures)

data = pandas.read_csv("weather-data.csv")

# convert to dictionart
data_dict = data.to_dict()
print(data_dict)

# convert to list
temp_list = data["temp"].to_list()
print(temp_list)

# average temp
avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp)

# get data in row
print(data[data["day"] == "Monday"])

# get the highest temp row
# highest_temp = 0
# for temp in temp_list:
#     if temp > highest_temp:
#         highest_temp = temp
#
# print(data[data["temp"] == highest_temp])

print(data[data["temp"] == data["temp"].max()])

monday = data[data["day"] == "Monday"]
print(monday.condition)

#convert monday temp to farenheight
monday_temp = int(monday.temp)
print(monday_temp * 9/5 + 32)

#create a dataframe from scratch

data_dict = {
    "students": ["Amy", "Dickson", "Lord"],
    "scores": [34, 56, 67]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("new_data.csv")






