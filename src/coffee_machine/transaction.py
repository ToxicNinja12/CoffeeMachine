from .cli import console
from . import inventory


def process_order(item, coins):
    available_resources = inventory.get_available_resources()
    needed_resources = inventory.get_ingredient(item)

    # TODO: Ensure if coins are enough.

    # Ensure resources are available.
    for resource in available_resources:
        if resource in needed_resources:
            if available_resources[resource] >= needed_resources[resource]:
                available_resources[resource] -= needed_resources[resource]
            else:
                console.error(f"Sorry there is not enough {resource}.")
                return

    console.print(f"Served {item} to user.")
