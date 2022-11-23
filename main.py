import os
import time

# local packages
import dataManager
import localColors

inserted_coins = {}  # empty list for coins processing.


# get data by self-oriented index from data with staticmethod.
class getDrink:
    @staticmethod
    def name(index_number) -> int:
        return list(dataManager.drinks.types.keys())[index_number]

    @staticmethod
    def value(index_number) -> int:
        return list(dataManager.drinks.types.values())[index_number][0]

    @staticmethod
    def inventory(index_number) -> int:
        return list(dataManager.drinks.types.values())[index_number][1]


# before accepting the coin, checking if the coins supported.
def check_if_coin_supported(user_coin):
    if user_coin in dataManager.coins.types:
        update_inserted_coins_dict(user_coin)
    else:
        print("coin not supported")


# this function will handle all refunds and update inventory
def refunds_handler():
    # refund by available coins
    # refund from larger to smaller
    # should update coins once refunded
    return None


# before processing the order, this function will check if we have change to return to customer in case he overpaid.
def coins_inventory_validation():
    # before processing the order, need to make sure we have a change for the customer
    # if not have change then process a refund of the same coin and cancel.
    return None


# api credit card processing (DEMO).
def credit_card_processing():
    # need to make sure no coins will be updated.
    # need to make sure it will validate the credit card and funds by api.
    # once approved, should process the order. no refunds will be processed.
    return None


# admin panel will be here.
def admin_panel():
    # secret key to enter the admin panel
    # need to add the admin menu and functionality
    # should consider to place the admin panel in a separate file.
    return None


# function to fix a bug
def check_type(parameter):
    if type(parameter) == list:
        return sum(parameter)
    else:
        return parameter

    # adds 1 to inventory of each coin that was inserted into the machine.


# create key:value in dictionary or find by key and insert +1 to value.
def update_inserted_coins_dict(user_coin: str):
    if user_coin in inserted_coins.keys():
        inserted_coins.update({user_coin: inserted_coins.get(user_coin, 0) + 1})
    else:
        inserted_coins.update({user_coin: 1})


# calculating total sum of all coins in the inserted_coins dictionary.
def calculate_sum_of_inserted_coins():
    total_value = [round(float(value_loop), 1) * quantity for value_loop, quantity in inserted_coins.items()]
    return round(sum(total_value), 1)


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

            # check if item exist and if in stock before continue.
            if selected_drink_by_user < len(dataManager.drinks.types.keys()) and getDrink.inventory(selected_drink_by_user) > 0:
                while True:
                    try:
                        input_user_coin = round(float(input("Insert a coin: ")), 1)
                        if input_user_coin == 99:
                            inserted_coins.clear()
                            break
                        else:
                            check_if_coin_supported(input_user_coin)
                            more_needed = getDrink.value(selected_drink_by_user) - calculate_sum_of_inserted_coins()
                            if more_needed > 0:
                                print(
                                    f"Insert more: {getDrink.value(selected_drink_by_user) - calculate_sum_of_inserted_coins()}")
                            else:
                                print("Processing...")
                                time.sleep(1)
                                print("Preparing your drink...")
                                time.sleep(1)

                                # refund the change
                                if more_needed < 0:
                                    print(
                                        f'Refunding: {round(calculate_sum_of_inserted_coins() - getDrink.value(selected_drink_by_user), 1)} ILS')
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

                    # everything that falling under "error" in the 2nd loop.
                    except Exception as err:
                        print(f"{localColors.select.FAIL}{err}{localColors.select.ENDC}")
                        pass
                        # raise # for debug purposes

            # everything that doesn't match general conditions therefore can type here new conditions.
            else:
                if selected_drink_by_user == 99:
                    print("You already in main menu!")
                    time.sleep(1)
                elif getDrink.inventory(selected_drink_by_user) <= 0:
                    print(f"{localColors.select.FAIL}Sorry, this drink out of stock!{localColors.select.ENDC}")
                    time.sleep(1)
                else:
                    print("Invalid drink number")
                    time.sleep(1)

        # everything that falling under "error" in first loop.
        except Exception as err:
            print(f"{localColors.select.FAIL}{err}{localColors.select.ENDC}")
            pass
            # raise


if __name__ == '__main__':
    start_vending_machine()
