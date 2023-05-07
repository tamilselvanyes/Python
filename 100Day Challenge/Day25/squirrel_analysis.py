import pandas


def get_color_count(list, color):
    total = 0
    for item in list:
        if item == color:
            total += 1
    return total


squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


gray_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])

cinnamon_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])

black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])


data_dict ={
    "Fur Color": ['Gray','Cinnamon', 'Black'],
    "Count":[gray_squirrels_count,cinnamon_squirrels_count,black_squirrels_count]
}


df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")