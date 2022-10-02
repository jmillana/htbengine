"""Machine os filter."""
from htbengine.models.machine import HTBMachine


def filter_by_os(
    machines: dict[str, HTBMachine], os: str
) -> dict[str, HTBMachine]:
    """Filter the machines by OS."""
    return {k: v for k, v in machines.items() if v.os.lower() == os}
