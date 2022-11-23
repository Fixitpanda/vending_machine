# calculating total sum of all coins in the inserted_coins dictionary.
def calculate_sum_of_inserted_coins(inserted_coins_dict):
    total_value = [round(float(value_loop), 1) * quantity for value_loop, quantity in inserted_coins_dict.items()]
    return round(sum(total_value), 1)


# function to fix a bug // should be simplified.
def check_type(parameter):
    if type(parameter) == list:
        return sum(parameter)
    else:
        return parameter


# create key:value in dictionary or find by key and insert +1 to value.
def update_inserted_coins_dict(user_coin: str, inserted_coins_dict: dict):
    if user_coin in inserted_coins_dict.keys():
        inserted_coins_dict.update({user_coin: inserted_coins_dict.get(user_coin, 0) + 1})
    else:
        inserted_coins_dict.update({user_coin: 1})


##########################################
# FEATURES THAT SHOULD BE ADDED IS BELOW #
##########################################

# TO ADD: if coins inserted but order cancelled by "99" then refund coins.

# TO ADD: before accepting the coin, checking if the coins supported.
def check_if_coin_supported(user_coin, user_data, inserted_coins_dict):
    if user_coin in user_data:
        update_inserted_coins_dict(user_coin, inserted_coins_dict)
    else:
        print("coin not supported")


# TO ADD: this function will handle all refunds and update inventory
def refunds_handler():
    # refund by available coins
    # refund from larger to smaller
    # should update coins once refunded
    return None


# TO ADD: before processing the order, this function will check if we have change to return to customer in case he overpaid.
def coins_inventory_validation():
    # before processing the order, need to make sure we have a change for the customer
    # if not have change then process a refund of the same coin and cancel.
    return None


# TO ADD: api credit card processing (DEMO).
def credit_card_processing():
    # need to make sure no coins will be updated.
    # need to make sure it will validate the credit card and funds by api.
    # once approved, should process the order. no refunds will be processed.
    return None


# TO ADD: admin panel will be here.
def admin_panel():
    # secret key to enter the admin panel
    # need to add the admin menu and functionality
    # should consider to place the admin panel in a separate file.
    return None
