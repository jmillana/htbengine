"""Machines filter."""
from htbengine import filters, models
from htbengine.models.machine import HTBMachine


def filter_machines(
    machines: dict[str, HTBMachine], user_filters: list[str]
) -> dict[str, HTBMachine]:
    """Filter the machines by the given filters."""
    for status in models.machine.STATUS:
        if status in user_filters:
            machines = filters.machines.filter_by_status(machines, status)

    if models.machine.BOOL_ATTRS.FREE in user_filters:
        machines = filters.machines.filter_by_free(machines, True)
    if models.machine.BOOL_ATTRS.SPAWNED in user_filters:
        machines = filters.machines.filter_by_spawned(machines, True)
    if models.machine.BOOL_ATTRS.OWNED in user_filters:
        machines = filters.machines.filter_by_owned(machines, True)

    os_machines = []
    for os in models.os.ALL:
        if os in user_filters:
            os_machines.append(filters.machines.filter_by_os(machines, os))

    if os_machines:
        machines = {}
        for os_machine in os_machines:
            machines.update(os_machine)

    difficulty_machines = []
    for difficulty in models.difficulty.ALL:
        if difficulty in user_filters:
            difficulty_machines.append(
                filters.machines.filter_by_difficulty(machines, difficulty)
            )

    if difficulty_machines:
        machines = {}
        for difficulty_machine in difficulty_machines:
            machines.update(difficulty_machine)

    return machines
