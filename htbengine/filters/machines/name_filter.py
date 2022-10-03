"""Machine name filter."""
from htbengine.models.machine import HTBMachine


def name_filter(
    machines: dict[str, HTBMachine], names: list[str]
) -> dict[str, HTBMachine]:
    """Filter machines by name.

    Args:
        machines (dict[str, HTBMachine]): The machines to filter.
        names (list[str]): The names to filter by.

    Returns:
        dict[str, HTBMachine]: The filtered machines.
    """
    filter_names = [name.lower() for name in names]
    filtered_machines = {}
    for machine in machines.values():
        if machine.name.lower() in filter_names:
            filtered_machines[machine.name] = machine
    return filtered_machines
