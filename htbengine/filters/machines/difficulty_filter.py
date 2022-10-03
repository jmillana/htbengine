"""Machine difficutly filter."""
from htbengine.models.machine import HTBMachine


def filter_by_difficulty(
    machines: dict[str, HTBMachine], difficulty: str
) -> dict[str, HTBMachine]:
    """Filter the machines by OS."""
    return {
        k: v
        for k, v in machines.items()
        if v.difficultyText.lower() == difficulty
    }
