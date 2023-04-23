from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Names",["Tamil","Sanjai","Yoga","Telugu Boy"])
table.add_column("Occupation", ["Software Developer","Architect","Isha Volunteer","Doctor"])
table.align = "l"

print(table)

