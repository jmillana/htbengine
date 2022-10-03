"""Printer module.

This module contains the utility methods to print the machines.
"""
from terminaltables import SingleTable

from htbengine.models.machine import HTBMachine
from htbengine.style.rainbow_machine import RainbowMachine

DEFAULT_HEADERS = [
    "Name",
    "IP Address",
    "Opperating System",
    "Difficulty",
    "Points",
    "Rating",
    "User Owns",
    "Root Owns",
    "Active",
    "Release Date",
    "Free lab",
    "Machine ID",
]

DEFAULT_ENTRIES = [
    "name",
    "ip",
    "os",
    "difficultyText",
    "points",
    "stars",
    "user_owns_count",
    "root_owns_count",
    "active",
    "release",
    "free",
    "id",
]


def machines_to_table(
    machines: dict[str, HTBMachine], headers: list[str], entries: list[str]
) -> SingleTable:
    """List the given machines.

    Args:
        machines (dict[str, HTBMachine]): The machines to list
    """
    rows = []
    rows.append(headers)
    print(machines)
    for machine in machines.values():
        rows.append(machine_to_row(machine, entries))
    table = SingleTable(rows)
    table.inner_row_border = True
    return table


def machine_to_row(machine: HTBMachine, entries: list[str]) -> list[str]:
    """Convert a machine instance to a table row.

    Args:
        machine (HTBMachine): The machine to convert
        entries (list[str]): List of machine propperties to display
    """
    rb_machine = RainbowMachine.colorize(machine)

    row = []
    for entry in entries:
        row.append(getattr(rb_machine, entry))
    return row


def display(
    machines: dict[str, HTBMachine],
    headers: list[str] = DEFAULT_HEADERS,
    entries: list[str] = DEFAULT_ENTRIES,
) -> None:
    """List the given machines.

    Args:
        machines (dict[str, HTBMachine]): The machines to list
        headers (list[str], optional):
            The headers of the table. Defaults to DEFAULT_HEADERS.
        entries (list[str], optional):
            The entries of the table. Defaults to DEFAULT_ENTRIES.
    """
    table = machines_to_table(machines, headers, entries)
    print(table.table)
