from time import sleep
from rich.console import Console
from rich.live import Live
from rich.spinner import Spinner
from rich.table import Table


def _error(message):
    """Display an error formatted message."""
    console.print(f"[red]{message}[/red]")


def _alert(message):
    """Display an alert formatted message."""
    console.print(f"[cornflower_blue]{message}[/cornflower_blue]")


def _spinner(message):
    """Display a loading message with a spinner."""
    spinner = Spinner("line", f"[yellow]{message}[/yellow]", style="yellow")
    with Live(spinner, refresh_per_second=10):
        sleep(1)


def _table(entries, title_text, caption_text, header=("key", "value")):
    """Display a formatted table from given dictionary."""
    table = Table(title=title_text, caption=caption_text)

    table.add_column(header[0])
    table.add_column(header[1])

    for key, value in entries.items():
        table.add_row(key, value)
    return table


def _int_input(prompt):
    """Ensure user inputs a positive integer."""
    while True:
        user_response = console.input(prompt)
        if user_response.isdigit():
            return int(user_response)
        else:
            _error("Please enter a positive integer.")

console = Console()
console.error = _error
console.alert = _alert
console.spinner = _spinner
console.table = _table
console.int_input = _int_input
