"""Machine status filter."""
from htbengine.models.machine import HTBMachine


def filter_by_status(
    machines: dict[str, HTBMachine], status: str
) -> dict[str, HTBMachine]:
    """Filter the machines by status.

    Args:
        machines (dict[str, HTBMachine]): The machines to filter
        status (str): The status to filter

    Raises:
        ValueError: If the status is not valid

    Returns:
        dict[str, HTBMachine]: The filtered machines
    """
    if status == "all":
        return machines
    elif status == "active":
        return {k: v for k, v in machines.items() if v.active}
    elif status == "retired":
        return {k: v for k, v in machines.items() if not v.active}
    else:
        raise ValueError(f"Invalid status: {status}")
