from .cli import console
from . import data


def main():
    menu_items = "/".join(data.MENU)

    with console.screen():
        console.show_cursor(True)

        while True:
            choice = console.input(f"What would you like? [magenta]({menu_items})[/]: ").lower()

            match choice:
                case coffee if coffee in data.MENU:
                    # TODO: Serve selected coffee to user.
                    console.print(f"Served {choice} to user.")
                    pass
                case "off":
                    console.spinner("Turning off coffee machine.")
                    return
                case _:
                    console.print("[red]Please enter an option listed above.[/]")


if __name__ == "__main__":
    main()
