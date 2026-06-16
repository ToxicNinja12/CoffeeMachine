from .cli import console
from . import data
from .transaction import get_balance


def get_menu():
    """Return string of available menu items separated by '/'."""
    return "/".join(data.MENU)


def get_available_resources():
    """Return amount of ingredients in vending machine."""
    return data.resources


def get_report():
    """Return formatted table containing information of remaining ingredients and balance in vending machine."""
    to_display = data.resources.copy()

    # Adding units to amount.
    for key in to_display:
        if key == "coffee":
            unit = "g"
        else:
            unit = "ml"
        to_display[key] = str(to_display[key]) + f" {unit}"

    # Formatting resource names.
    for key in to_display:
        to_display[key.capitalize()] = to_display.pop(key)

    return console.table(
        to_display,
        title_text="Inventory Report",
        header=("resource", "amount"),
        caption_text=f"Balance: ${get_balance():.2f}"
    )


def get_ingredient(drink):
    """Return resources needed to create the drink."""
    return data.MENU[drink]["ingredients"]


def get_cost(drink):
    """Return price of the drink."""
    return data.MENU[drink]["cost"]
