"""Machine spawned filter."""
from htbengine.models.machine import HTBMachine


def filter_by_spawned(
    machines: dict[str, HTBMachine], spawned: bool
) -> dict[str, HTBMachine]:
    """Filter the machines by spawned."""
    return {
        k: v for k, v in machines.items() if v.playInfo.isSpawned == spawned
    }
