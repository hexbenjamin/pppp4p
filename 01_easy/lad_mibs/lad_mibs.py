from random import shuffle
from time import sleep
from typing import Dict, Protocol

from rich.console import Console
from rich.theme import Theme

CONSOLE = Console(color_system="256", theme=Theme(inherit=False))


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

    TEMPLATE = '''According to all known {noun1}s of {field_of_study}, there is no way a(n) {animal} should be able to fly. Its' wings are too {adjective1} to get its' {adjective2} little {noun2} off the {noun3}.
    
    The {animal}, of course, flies anyway, because {animal}s don't care what humans think is {adjective3}.
    
    "{color1}, {color2}. {color1}, {color2}."
    
    "{color1}, {color2}. {color1}, {color2}."
    
    "Ooh, {color2} and {color1}! Let's {verb} it up a little."
    
    "{first_name}! {noun4} is ready!"
    
    "{gerund}!"'''

    def get_printable(self):
        return self.TEMPLATE.format(**self.slots)


class PrayRightLM(LadMib):
    slots = {
        "90sband": "band from the 1990s",
        "adlib1": "ad-lib",
        "adlib2": "ad-lib",
        "adlib3": "ad-lib",
        "animal": "animal",
        "artformat": "type of artwork",
        "biblical_figure": "biblical figure",
        "biome": "biome (climate region)",
        "bodypart1": "body part",
        "bodypart2": "body part",
        "bodypart3": "body part",
        "city1": "city",
        "city2": "foreign city",
        "direction": "direction",
        "dismissive": "dismissive address (e.g. 'bruh', 'my guy', 'lil bitch')",
        "exclamation": "exclamation",
        "fruit": "fruit",
        "profession": "profession (e.g. 'doctor', 'lawyer', 'forklift operator')",
        "noun1": "noun",
        "number1": "number",
        "number2": "number",
        "placetype": "non-specific place (e.g. 'mall', 'bookstore', 'bottom of a well')",
        "pluralnoun1": "plural noun",
        "pluralnoun2": "plural noun",
        "pluralnoun3": "plural noun",
        "timeperiod": "measure of time",
        "verb1": "verb",
        "verb2": "verb",
    }

    TEMPLATE = """
[bold green]BONG HAMPER[/] - [italic]'IF U PRIGHT'[/]

[[italic]Verse 1:[/] [bold red]Domic Lemnon[/]]
{exclamation}, holy {animal}, word to {biblical_figure}
How I'm supposed to, ({adlib1}) trust what you say is the truest? ({direction})
Haile Selassie, ({adlib2}) insha'Allah if I gotta ({adlib3})
Spin my {noun1}s around as if you wanted a mandala for {90sband}
Singin' a {artformat} towards our karma
Did a rain dance, bringin' commas from {city1} to {city2}
I got spirits in my {bodypart1} that make my {bodypart2} move like it's water
Flow into the moment and {verb1} the melodrama
Gotta {verb2} for a {timeperiod}
Can't believe anybody still testin'
My whole team is a force to be reckoned with
Operatin' like {pluralnoun1}
{number1} to the {number2} to the who are you?
Sendin' out {pluralnoun2} with prejudice
My attention to detail is in scale with classic {profession}s
So the lesson is that prerequisites are irrelevant to my {pluralnoun3} ({direction})
It's a deficit in your {placetype}, you better learn to mind all your manners ({direction})
My whole troop been goin' {fruit}s
Try and step inside of our {biome} ({direction})
You can try to take all your chances
We won't help your {bodypart3} if you stumble, {dismissive}"""

    def get_printable(self):
        return self.TEMPLATE.format(**self.slots)


def fill_ladmib(ladmib: LadMib) -> None:
    CONSOLE.print(
        "\n[bold yellow]!!![/] send 'QUIT', in caps, at any time to quit.\n+++"
    )

    keys = list(ladmib.slots.keys())
    shuffle(keys)

    for key in keys:
        CONSOLE.print(f"\nEnter a(n) [bold]{ladmib.slots[key]}[/].")
        res = CONSOLE.input("  [bold blue]>[/] ")
        quit() if res == "QUIT" else None
        ladmib.slots[key] = f"[bold blue]{res}[/bold blue]"


if __name__ == "__main__":
    while True:
        CONSOLE.clear()
        CONSOLE.print("L A D   M I B S  !", style="bold underline blue")

        CONSOLE.print("\nPlease select a [bold blue]LAD MIB[/] by number.")
        sel = CONSOLE.input("\n1: B. Movie\n2: B. Hampton\n\n  [bold green]>[/] ")

        if sel in ["1", "2"]:
            break

        CONSOLE.print("\n[bold red]invalid selection.[/] try again, big homie.")
        CONSOLE.input("[italic]press [[bold]ENTER[/]] to continue.]")

    CONSOLE.clear()

    ladmib = [BeeMovieLM(), PrayRightLM()][int(sel) - 1]
    fill_ladmib(ladmib)

    CONSOLE.print("\nLAD MIB complete.", style="bold green")

    CONSOLE.print("\nprinting result...", style="italic")
    sleep(3)
    CONSOLE.print("\n---\n" + ladmib.get_printable())
