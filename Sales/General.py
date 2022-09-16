import Car
import Furniture
import Phone


def welcome():
    hello = input("Welcome \nWe Sell Everything \n1)Cars \n2)Furniture \n3)Phones \n")

    match hello:
        case "1":
            sell_car()
        case "2":
            sell_furniture()
        case "3":
            sell_phone()


def sell_car():
    hello = input("\nThe Cars we sell \n1)Benz \n2)Bmw \n3)Audi \n")

    match hello:
        case "1":
            select_benz()
        case "2":
            select_bmw()
        case "3":
            select_audi()


def select_benz():
    s = input("Please Select the Type of Benz you want...\n1)C-Class \n2)G-Class \n3)S-Class \n")
    match s:
        case "1":
            print(f"You have selected Benz \n Model : {Car.Benz1.model} \n Your total is : ${Car.Benz1.price}")
            print("Kindly Come to our Car Dealer to collect your Car")
        case "2":
            print(f"You have selected Benz \n Model : {Car.Benz2.model} \n Your total is : ${Car.Benz2.price}")
            print("Kindly Come to our Car Dealer to collect your Car")
        case "3":
            print(f"You have selected Benz \n Model : {Car.Benz3.model} \n Your total is : ${Car.Benz3.price}")
            print("Kindly Come to our Car Dealer to collect your Car")


def select_bmw():
    s = input("Please Select the Type of BMW you want...\n1)X3 \n2)X5 \n3)X6 \n")
    match s:
        case "1":
            print(f"You have selected Benz \n Model : {Car.BMW1.model} \n Your total is : ${Car.BMW1.price}")
            print("Kindly Come to our Car Dealer to collect your Car")
        case "2":
            print(f"You have selected Benz \n Model : {Car.BMW2.model} \n Your total is : ${Car.BMW2.price}")
            print("Kindly Come to our Car Dealer to collect your Car")
        case "3":
            print(f"You have selected Benz \n Model : {Car.BMW3.model} \n Your total is : ${Car.BMW3.price}")
            print("Kindly Come to our Car Dealer to collect your Car")


def select_audi():
    s = input("Please Select the Type of Audi you want...\n1)A4 \n2)A5 \n3)A7 \n")
    match s:
        case "1":
            print(f"You have selected Benz \n Model : {Car.Audi1.model} \n Your total is : ${Car.Audi1.price}")
            print("Kindly Come to our Car Dealer to collect your Car")
        case "2":
            print(f"You have selected Benz \n Model : {Car.Audi2.model} \n Your total is : ${Car.Audi2.price}")
            print("Kindly Come to our Car Dealer to collect your Car")
        case "3":
            print(f"You have selected Benz \n Model : {Car.Audi3.model} \n Your total is : ${Car.Audi3.price}")
            print("Kindly Come to our Car Dealer to collect your Car")


def sell_furniture():
    hello = input("\nThe Furniture we sell \n1)Table \n2)Chair \n3)Wardrobe \n")

    match hello:
        case "1":
            select_table()
        case "2":
            select_chair()
        case "3":
            select_wardrobe()


def select_table():
    s = input("Please Select the Type of Table you want...\n1)Glass Table \n2)Wooden Table \n3)Marble Table \n")
    match s:
        case "1":
            print(f"Model : {Furniture.Table1.title} \n Your total is : ${Furniture.Table1.price}")
            print("Kindly Come to our Store to collect your Furniture")
        case "2":
            print(f"Model : {Furniture.Table2.title} \n Your total is : ${Furniture.Table2.price}")
            print("Kindly Come to our Store to collect your Furniture")
        case "3":
            print(f"Model : {Furniture.Table3.title} \n Your total is : ${Furniture.Table3.price}")
            print("Kindly Come to our Store to collect your Furniture")


def select_chair():
    s = input("Please Select the Type of Chair you want...\n1)Glass Chair \n2)Wooden Chair \n3)Marble Chair \n")
    match s:
        case "1":
            print(f"Model : {Furniture.Chair1.title} \n Your total is : ${Furniture.Chair1.price}")
            print("Kindly Come to our Store to collect your Furniture")
        case "2":
            print(f"Model : {Furniture.Chair2.title} \n Your total is : ${Furniture.Chair2.price}")
            print("Kindly Come to our Store to collect your Furniture")
        case "3":
            print(f"Model : {Furniture.Chair3.title} \n Your total is : ${Furniture.Chair3.price}")
            print("Kindly Come to our Store to collect your Furniture")


def select_wardrobe():
    s = input("Please Select the Type of Wardrobe you want...\n1)Brown Wood Wardrobe \n2)Yellow Wood Wardrobe "
              "\n3)Black Wardrobe \n")
    match s:
        case "1":
            print(f"Model : {Furniture.Wardrobe1.title} \n Your total is : ${Furniture.Wardrobe1.price}")
            print("Kindly Come to our Store to collect your Furniture")
        case "2":
            print(f"Model : {Furniture.Wardrobe2.title} \n Your total is : ${Furniture.Wardrobe2.price}")
            print("Kindly Come to our Store to collect your Furniture")
        case "3":
            print(f"Model : {Furniture.Wardrobe3.title} \n Your total is : ${Furniture.Wardrobe3.price}")
            print("Kindly Come to our Store to collect your Furniture")


def sell_phone():
    hello = input("\nThe Phones we sell \n1)Samsung \n2)Iphone \n")

    match hello:
        case "1":
            select_samsung()
        case "2":
            pass


def select_samsung():
    s = input("Please Select the Type of Samsung you want...\n1)S10 \n2)S20 \n3)S22 \n")

    match s:
        case "1":
            print(f"Model : {Phone.S10.model} \n Your total is : ${Phone.S10.price}")
            print("Kindly Come to our Store to collect your Phone")
        case "2":
            print(f"Model : {Phone.S20.model} \n Your total is : ${Phone.S20.price}")
            print("Kindly Come to our Store to collect your Phone")
        case "3":
            print(f"Model : {Phone.S22.model} \n Your total is : ${Phone.S22.price}")
            print("Kindly Come to our Store to collect your Phone")

