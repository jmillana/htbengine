"""Machine ip filter."""
from htbengine.models.machine import HTBMachine


def ip_filter(
    machines: dict[str, HTBMachine], ip_list: list[str]
) -> dict[str, HTBMachine]:
    """Filter machines by name.

    Args:
        machines (dict[str, HTBMachine]): The machines to filter.
        names (list[str]): The names to filter by.

    Returns:
        dict[str, HTBMachine]: The filtered machines.
    """
    filtered_machines = {}
    for machine in machines.values():
        if machine.ip in ip_list:
            filtered_machines[machine.name] = machine
    return filtered_machines
