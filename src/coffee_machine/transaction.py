from .cli import console
from . import inventory


_ACCEPTED_COINS = {"quarters": 0.25, "dimes": 0.10, "nickels": 0.05, "pennies": 0.01}
_available_balance = 0


def get_balance():
    """Return available balance in vending machine."""
    return _available_balance


def request_coins():
    """Request payment from user via coin insertion."""
    total_amount = 0
    for coin_name in _ACCEPTED_COINS:
        coin_amount = console.int_input(f"Insert {coin_name}: ")
        total_amount += coin_amount * _ACCEPTED_COINS[coin_name]
    return total_amount


def process_order(item):
    """Ensure proper transaction handling."""
    global _available_balance
    available_resources = inventory.get_available_resources()
    needed_resources = inventory.get_ingredient(item)

    resources_to_update = dict()

    # Ensure resources are available.
    for resource in available_resources:
        if resource in needed_resources:
            if available_resources[resource] >= needed_resources[resource]:
                resources_to_update[resource] = available_resources[resource] - needed_resources[resource]
            else:
                console.error(f"Sorry there is not enough {resource}.")
                return

    # Ensure successful payment.
    item_price = inventory.get_cost(item)
    console.print(f"Please pay [white]${item_price:.2f}[/].")
    received_amount = request_coins()
    console.alert(f"You have paid ${received_amount:.2f}.")


    if received_amount >= item_price:
        if received_amount > item_price:
            console.print(f"Here is [white]${received_amount - item_price:.2f}[/] in change.")
        _available_balance += item_price
        inventory.update_resources(resources_to_update)
        console.print(f"Here is your {item}. Enjoy!")
    else:
        console.error("Sorry that's not enough money. Money refunded.")
