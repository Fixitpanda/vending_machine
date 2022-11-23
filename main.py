import os
import time
from components.functions import *
from components import localColors, dataManager
from components import classes

inserted_coins = {}  # empty list for coins processing.
getDrink = classes.getDrink(dataManager.drinks.types)  # passing drinks to class getDrinks
p

# creating colorful menu based on drinks/stock inside the inventory.json file.
def drinks_menu_type_out():
    zero = 0
    print(
        f"This machine support credit cards or coins ==> {localColors.select.WARNING}Supported Coins: {[i for i in dataManager.coins.types]}{localColors.select.ENDC}")
    print(f"{localColors.select.HEADER}Select your drink from the list below:{localColors.select.ENDC}")
    for key_loop, values in dataManager.drinks.types.items():
        print(
            f'   {zero}. {key_loop} ---> [PRICE: {float(values[0])} ILS] ---> {localColors.select.FAIL}[{values[1]} in stock]{localColors.select.ENDC}')
        zero += 1
    print(f"{localColors.select.OKBLUE}   TYPE --> 99 to return to main screen at any time.{localColors.select.ENDC}")


# this function start the vending machine.
def start_vending_machine():
    while True:
        try:
            os.system('cls')  # cleaning terminal after each loop.
            drinks_menu_type_out()
            selected_drink_by_user = int(
                input(f"{localColors.select.BOLD}What is the drink number?: {localColors.select.ENDC}"))
            if selected_drink_by_user < 0:
                raise ValueError("Negative index not supported by the menu.")

            # check if item exist and if in stock before continue, otherwise will be thrown to exception.
            if selected_drink_by_user < len(dataManager.drinks.types.keys()) and getDrink.inventory(
                    selected_drink_by_user) > 0:
                while True:
                    try:
                        input_user_coin = round(float(input("Insert a coin: ")), 1)
                        if input_user_coin == 99:
                            inserted_coins.clear()
                            break
                        else:
                            check_if_coin_supported(input_user_coin, dataManager.coins.types, inserted_coins)
                            more_needed = getDrink.value(selected_drink_by_user) - calculate_sum_of_inserted_coins(
                                inserted_coins)
                            if more_needed > 0:
                                print(
                                    f"Insert more: {getDrink.value(selected_drink_by_user) - calculate_sum_of_inserted_coins(inserted_coins)}")
                            else:
                                print("Processing...")
                                time.sleep(1)
                                print("Preparing your drink...")
                                time.sleep(1)

                                # refund the change
                                if more_needed < 0:
                                    print(
                                        f'Refunding: {round(calculate_sum_of_inserted_coins(inserted_coins) - getDrink.value(selected_drink_by_user), 1)} ILS')
                                    time.sleep(1)
                                    print('Dont forget your exchange!')
                                    time.sleep(1)
                                print("Order Completed, Thank you!")
                                time.sleep(2)

                                # updating the inventory once order completed.
                                for key, value in inserted_coins.items():
                                    get_value_from_inventory = check_type(dataManager.available_coins.types.get(key, 0))
                                    dataManager.available_coins.types.update(
                                        {str(key): [value + get_value_from_inventory]})

                                # save updated inventory to json file
                                dataManager.update_file("CoinsStock", dataManager.available_coins.types)

                                # resetting the inventory
                                inserted_coins.clear()

                                # updating inventory
                                dataManager.drinks.types.update({getDrink.name(selected_drink_by_user): [
                                    getDrink.value(selected_drink_by_user),
                                    getDrink.inventory(selected_drink_by_user) - 1]})
                                dataManager.update_file("Drinks", dataManager.drinks.types)
                                break

                    # error handling inside the internal loop
                    except Exception as err:
                        print(f"{localColors.select.FAIL}{err}{localColors.select.ENDC}")
                        pass
                        # raise  # use raise for debug purposes

            # if it doesn't match general conditions will be thrown to error exception.
            else:
                raise

        # errors output handled here. you can customize output put just or just it be.
        except Exception as err:
            try:
                if getDrink.inventory(selected_drink_by_user) == 0:
                    print(f"{localColors.select.FAIL}Sorry, this drink out of stock!{localColors.select.ENDC}")
                    time.sleep(1)
                else:
                    print(f"{localColors.select.FAIL}{err}{localColors.select.ENDC}")
                    time.sleep(1)
            except Exception as err:
                if selected_drink_by_user == 99:
                    print("You already in main menu!")
                    time.sleep(1)
                elif "Error --> main loop." or "list index out of range" or "invalid literal for int()" in str(err):
                    print(f"{localColors.select.FAIL}Not in menu, invalid drink number!{localColors.select.ENDC}")
                    time.sleep(1)
                else:
                    print(
                        f"{localColors.select.WARNING}Oh Oh something is really fucked up here!{localColors.select.ENDC} Error inside the error handler: {localColors.select.FAIL}{err}{localColors.select.ENDC}")


if __name__ == '__main__':
    start_vending_machine()
