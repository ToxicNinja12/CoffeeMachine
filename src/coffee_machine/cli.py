from time import sleep
from rich.console import Console
from rich.live import Live
from rich.spinner import Spinner


def _spinner(message):
    spinner = Spinner("line", f"[yellow]{message}[/yellow]", style="yellow")
    with Live(spinner, refresh_per_second=10):
        sleep(1)

console = Console()
console.spinner = _spinner
