"""Defina available filters for machines."""
from enum import Enum, EnumMeta


class ContainsEnumMeta(EnumMeta):
    """Add contains method to Enum class."""

    def __contains__(cls, item) -> bool:
        """Allow in opperator usage.

        Args:
            item (str): _description_

        Returns:
            bool: _description_
        """
        try:
            cls(str(item).lower())
        except ValueError:
            return False
        return True


class MachineFilters(Enum, metaclass=ContainsEnumMeta):
    """Machine filters enum."""

    ALL_MACHINES = "all"
    RETIRED_MACHINES = "retired"
    ACTIVE_MACHINES = "active"
    FREE_MACHINES = "free"
    SPAWNED_MACHINES = "spawned"
    OWNED_MACHINES = "owned"
    OS_WINDOWS = "windows"
    OS_LINUX = "linux"
    OS_FREEBSD = "freebsd"
    OS_OPENBSD = "openbsd"
    OS_OTHER = "other"
