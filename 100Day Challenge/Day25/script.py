# with open("./weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")

temp_list = data['temp'].to_list()
print(temp_list)

total = 0;
avg = 0
for temp in temp_list:
    total += temp

avg = total / len(temp_list)

avg_temp = data["temp"].mean()
max_temp = data["temp"].max()

print(data[data.day == "Monday"])

max_temp_day = data[data.temp == max_temp]
print(max_temp_day)

data_dictionary = {
    "students": ["Tamil", "Sanjai", "Selvan"],
    "marks": [56, 79, 90]
}

pandas_data = pandas.DataFrame(data_dictionary)
pandas_data.to_csv("created_data_new.csv")