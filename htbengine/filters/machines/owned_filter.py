"""Machine owned filter."""
from htbengine.models.machine import HTBMachine


def filter_by_owned(
    machines: dict[str, HTBMachine], owned: bool
) -> dict[str, HTBMachine]:
    """Filter the machines by owned."""
    # TODO: Need to query to the user profile to get the owned machines
    return {}
