from .cli import console
from . import inventory, transaction


def main():
    menu = inventory.get_menu()

    with console.screen():
        console.show_cursor(True)

        while True:
            choice = console.input(f"What would you like? [magenta]({menu})[/]: ").lower()

            match choice:
                case coffee if coffee in inventory.data.MENU:
                    transaction.process_order(coffee)
                case "report":
                    console.print(inventory.get_report())
                case "off":
                    console.spinner("Turning off coffee machine.")
                    return
                case _:
                    console.error("Please enter an option listed above")


if __name__ == "__main__":
    main()
