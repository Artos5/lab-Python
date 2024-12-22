import csv

import os

flag = False

try:

    csvfile = open("C:/Users/Hacker/Downloads/lab_11.csv","r")

    reader = csv.DictReader(csvfile, delimiter = ",")

    print("Country Name: 2018 [YR2018],2019 [YR2019]")

    for row in reader:

        print(row['Country Name'], ',', row["2018 [YR2018]"])

    csvfile.close

except:

    print("ERR1: Файл lab_11.csv не знайдено!")

try:

    csvfile = open("C:/Users/Hacker/Downloads/lab_11.csv","r")

    reader = csv.DictReader(csvfile, delimiter = ",")

    indicator = input("\nВведіть назву країни для пошуку даних: ")

    while indicator.isnumeric():

        indicator = input("Введіть назву ще раз: ")

    os.system('clear')

    print("Country Name: 2018 [YR2018],2019 [YR2019]")

    for row in reader:

        if indicator == row["Country Name"]:

            flag = True

            print(row["Country Name"], ",",row["Country Code"], ",",row["Series Name"], ",",row["Series Code"], ",",row["2018 [YR2018]"], ",", row["2019 [YR2019]"])

            with open("C:/Users/Hacker/Downloads/new_lab_11.csv","a") as csvfile2:

                writer = csv.writer(csvfile2, delimiter = ",")

                writer.writerow((row["Country Name"],row["Country Code"],row["Series Name"],row["Series Code"],row["2018 [YR2018]"], row["2019 [YR2019]"]))

    csvfile.close

    if flag == False:

        os.system('clear')


except:

    print("ERR2: Файл lab_11.csv не знайдено!")
