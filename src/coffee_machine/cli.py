from time import sleep
from rich.console import Console
from rich.live import Live
from rich.spinner import Spinner
from rich.table import Table


def _error(message):
    """Display an error formatted message."""
    console.print(f"[red]{message}[/red]")


def _spinner(message):
    """Display a loading message with a spinner."""
    spinner = Spinner("line", f"[yellow]{message}[/yellow]", style="yellow")
    with Live(spinner, refresh_per_second=10):
        sleep(1)


def _table(entries, title_text, caption_text, header=("key", "value")):
    """Display a formatted table from given dictionary."""
    table = Table(title=title_text, caption=caption_text, caption_justify="left")

    table.add_column(header[0])
    table.add_column(header[1])

    for key, value in entries.items():
        table.add_row(key, value)
    return table

console = Console()
console.error = _error
console.spinner = _spinner
console.table = _table
