"""Colored version of the HTBMachine class."""
import dataclasses

from termcolor import colored

from htbengine.models.machine import HTBMachine
from htbengine.style import colors


class RainbowMachine:
    """Class to add colors to the HTBMachine."""

    def __init__(self, machine: HTBMachine):
        """Class constructor of the RainbowMachine.

        Args:
            machine (HTBMachine): The machine to colorize
        """
        self.machine = machine

    @classmethod
    def colorize(cls, machine: HTBMachine) -> HTBMachine:
        """Colorize a string."""
        colored_machine = dataclasses.replace(machine)
        # Add the OS color to the desired properties
        os_color = colors.OS[machine.os.lower()]
        colored_machine.name = colored(machine.name, os_color)
        colored_machine.os = colored(machine.os, os_color)
        # Add the difficulty color to the desired properties
        difficulty_color = colors.DIFICULTY[machine.difficultyText.lower()]
        colored_machine.difficultyText = colored(
            machine.difficultyText, difficulty_color
        )
        colored_machine.difficulty = colored(
            str(machine.difficulty), difficulty_color
        )
        colored_machine.stars = RainbowMachine.get_rating_color(machine)
        colored_machine.points = RainbowMachine.get_points_color(machine)
        for field in machine.__dataclass_fields__:
            field_value = getattr(machine, field)
            if isinstance(field_value, bool):
                color = colors.BOOL[field_value]
                colored_field = colored(str(field_value), color)
                setattr(colored_machine, field, colored_field)
        return colored_machine

    @staticmethod
    def get_bool_color(value: bool, reverse=False) -> str:
        """Get the color for a boolean value.

        Args:
            value (bool): The value to colorize
            reverse (bool, optional): Reverse the color. Defaults to False.
                If True, the color will be the opposite of the default color.
        """
        color = colors.BOOL[value]
        if reverse:
            color = colors.BOOL[not value]
        return colored(str(value), color)

    @staticmethod
    def get_rating_color(machine: HTBMachine) -> str:
        """Get the color for the rating."""
        if float(machine.stars) >= 4.5:
            color = colors.GREEN
        elif float(machine.stars) >= 4:
            color = colors.YELLOW
        elif float(machine.stars) >= 3.5:
            color = colors.MAGENTA
        else:
            color = colors.RED
        return colored(str(machine.stars), color)

    @staticmethod
    def get_points_color(machine: HTBMachine) -> str:
        """Get the color for the points."""
        if not isinstance(machine.points, int):
            raise TypeError("Points must be an integer")
        if machine.points == 50:
            color = colors.MAGENTA
        elif machine.points >= 40:
            color = colors.RED
        elif machine.points >= 30:
            color = colors.YELLOW
        elif machine.points >= 20:
            color = colors.GREEN
        else:
            color = colors.WHITE
        return colored(str(machine.points), color)
