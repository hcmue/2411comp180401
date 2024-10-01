import csv
with open("mycsv.csv", "w", encoding="utf8") as my_file:
    employee_writer = csv.writer(my_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(["Tèo Nguyễn", 22, 12090000])
    employee_writer.writerow(["Tý Nguyễn", 22, 12090000])