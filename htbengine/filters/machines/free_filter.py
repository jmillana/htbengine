"""Machine free filter."""
from htbengine.models.machine import HTBMachine


def filter_by_free(
    machines: dict[str, HTBMachine], free: bool
) -> dict[str, HTBMachine]:
    """Filter the machines by free."""
    return {k: v for k, v in machines.items() if v.free == free}
