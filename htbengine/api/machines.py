"""Machine API endpoints."""
import logging

import requests

from htbengine.models.machine import HTBMachine

logger = logging.getLogger(__name__)


def get_machines(url: str, token: str) -> tuple[dict[str, HTBMachine], dict]:
    """Get the machines from the API.

    Args:
        url (str, optional): URL to get the data from.
        token (str, optional): Token to authenticate on the API. Defaults to
                               API_TOKEN.
        cache (dict | None, optional): Cache to be used. Defaults to None.

    Returns:
        dict[str, HTBMachine]: Dictionary with the machines indexed by name
        dict: The cache dictionary
    """
    logger.debug("Getting machines from HTB API: %s", url)
    headers = {"User-Agent": "htbengine", "Authorization": f"Bearer {token}"}
    r = requests.get(url, headers=headers)
    data = r.json()
    machines: dict[str, HTBMachine] = {}
    for machine in data["info"]:
        htbmachine = HTBMachine(**machine)
        machines[htbmachine.name] = htbmachine
    machines_dict = {machine["name"]: machine for machine in data["info"]}
    return machines, machines_dict
