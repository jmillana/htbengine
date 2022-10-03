"""Machine Manager module.

This module contains the MachineManager class.
This class is used to manage the machines, store and restore the locally
cached files and updates it's contents via the HTB API.
"""
import json
import os
from datetime import datetime, timedelta

from htbengine.api import endpoints
from htbengine.api import machines as api_machines
from htbengine.models.machine import HTBMachine

MACHINES_CACHE = "machines.json"


class MachineManager:
    """Machine Manager class."""

    def __init__(
        self,
        token: str,
        cache_path: str = MACHINES_CACHE,
    ):
        """Class constructor of the MachineManager.

        Args:
            token (str): The HTB API token
            cache_path (str, optional): Path to the cache file. Defaults to
                                        MACHINES_CACHE.
        """
        self.cache_path = cache_path
        self.token = token
        self.machines: dict[str, HTBMachine] = {}

    def save_machines(self, machines: dict) -> None:
        """Save the machines in a cache file.

        Args:
            machines (dict): The machines to save
        """
        machines_dict = {
            "machines": machines,
            "last_update": datetime.now().isoformat(),
        }
        with open(MACHINES_CACHE, "w") as f:
            json.dump(machines_dict, f, indent=4)

    def load_machines(self, force: bool = False) -> dict[str, HTBMachine]:
        """Load the machines from the cache file or from the API.

        If the cache file exists and the last update was less than 24 hours
        ago, load the machines from the cache file. Otherwise, load the
        machines from the API.

        Args:
            force (bool, optional): Force the update ignoring the cache.
                                    Defaults to False.

        Returns:
            list[HTBMachine]: The list of machines
        """
        machines: dict[str, HTBMachine] = {}
        machines_cache = None
        if force:
            return self.get_machines_from_api()

        # Check if cache exists and load its data
        if os.path.exists(MACHINES_CACHE):
            with open(MACHINES_CACHE, "r") as f:
                machines_cache = json.load(f)
        if machines_cache and datetime.fromisoformat(
            machines_cache["last_update"]
        ) > datetime.now() - timedelta(days=1):
            # If cache exists and is older than 1 day, update it
            for machine in machines_cache["machines"].values():
                htbmachine = HTBMachine(**machine)
                machines[htbmachine.name] = htbmachine
        else:
            # If the cache do not exits or is newer than 1 day, update/crate it
            machines = self.get_machines_from_api()
        return machines

    def get_machines_from_api(self) -> dict[str, HTBMachine]:
        """Get all the machines from the API.

        Returns:
            dict[str, HTBMachine]: Dictionary with the machines indexed by name
        """
        machines = {}
        machines_dict = {}
        active_machines, active_machines_dict = api_machines.get_machines(
            endpoints.HTB_MACHINES_ACTIVE_URL, self.token
        )
        for machine in active_machines.values():
            machine.active = True
            active_machines_dict[machine.name]["active"] = True
        retired_machines, retired_machines_dict = api_machines.get_machines(
            endpoints.HTB_MACHINES_RETIRED_URL, self.token
        )
        machines.update(active_machines)
        machines.update(retired_machines)
        machines_dict.update(active_machines_dict)
        machines_dict.update(retired_machines_dict)
        self.save_machines(machines_dict)
        return machines
