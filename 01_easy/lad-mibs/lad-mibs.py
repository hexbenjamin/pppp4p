from random import shuffle
from time import sleep
from typing import Dict, Protocol

from rich.console import Console
from rich.theme import Theme

CONSOLE = Console(theme=Theme(inherit=False))


class LadMib(Protocol):
    slots: Dict[str, str]
    TEMPLATE: str

    def get_printable(self) -> None:
        ...


class BeeMovieLM(LadMib):
    slots = {
        "adjective1": "adjective",
        "adjective2": "adjective",
        "adjective3": "adjective",
        "animal": "animal",
        "color1": "color",
        "color2": "color",
        "field_of_study": "field of study",
        "first_name": "person's first name",
        "gerund": "present tense/'-ing' verb",
        "noun1": "noun",
        "noun2": "noun",
        "noun3": "noun",
        "noun4": "noun",
        "verb": "verb",
    }

    TEMPLATE = '''According to all known {noun1}s of {field_of_study}, there is no way a(n) {animal} should be able to fly. Its' wings are too {adjective1} to get its' {adjective2} little {noun2} off the {noun3}. The {animal}, of course, flies anyway, because {animal}s don't care what humans think is {adjective3}.\n\n"{color1}, {color2}. {color1}, {color2}."\n"{color1}, {color2}. {color1}, {color2}."\n"Ooh, {color2} and {color1}! Let's {verb} it up a little."\n\n"{first_name}! {noun4} is ready!"\n"{gerund}!"'''

    def get_printable(self):
        return self.TEMPLATE.format(**self.slots)


def fill_ladmib(ladmib: LadMib) -> None:
    CONSOLE.print("[bold yellow]!!![/] send 'QUIT', in caps, at any time to quit.\n+++")

    keys = list(ladmib.slots.keys())
    shuffle(keys)

    for key in keys:
        CONSOLE.print(f"\nEnter a(n) [bold]{ladmib.slots[key]}[/].")
        res = CONSOLE.input("  [bold red]>[/] ")
        quit() if res == "QUIT" else None
        ladmib.slots[key] = f"[bold red]{res}[/bold red]"


if __name__ == "__main__":
    ladmib = BeeMovieLM()
    fill_ladmib(ladmib)
    CONSOLE.print("\nLAD MIB complete.", style="bold green")
    CONSOLE.print("\nprinting result...", style="italic")
    sleep(3)
    CONSOLE.print("\n---\n" + ladmib.get_printable())
