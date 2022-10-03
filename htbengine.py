# -*- coding: utf-8 -*-
"""HTB search engine main module.

@Author: Jordi Marimon (jmillana)
"""

import logging
import os
import sys

import dotenv
from termcolor import colored

from htbengine import filters, parser
from htbengine.api import token as api_token
from htbengine.machine_manager import MachineManager
from htbengine.machine_printer import machine_printer
from htbengine.menus.help import help_menu
from htbengine.style import colors

dotenv.load_dotenv()
HTB_API_TOKEN = os.getenv("HTB_API_TOKEN")
HTB_USER = os.getenv("HTB_USER")
HTB_PWD = os.getenv("HTB_PWD")


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def load_token() -> str | None:
    """Load the token from the environment variables."""
    token = None
    if HTB_API_TOKEN:
        token = HTB_API_TOKEN
        logger.debug("Using HTB_API_TOKEN from environment")
    elif HTB_USER and HTB_PWD:
        logger.debug("Getting token from env. vars HTB_USER & HTB_PWD")
        token = api_token.get_api_token(HTB_USER, HTB_PWD)
    return token


def main():
    """Nice Main function."""
    args = parser.get_args()
    if args.help:
        help_menu()
        sys.exit(0)

    if not (token := load_token()):
        print(
            colored(
                "[!] API token or user credentials not provided", colors.ERROR
            )
        )
        sys.exit(1)
    machine_manager = MachineManager(token)
    machines = machine_manager.load_machines()

    if args.explore:
        filtered_machines = filters.filter_machines(machines, args.explore)
        # Add retired field to the filtered machines
        for machine in filtered_machines.values():
            machine.retired = not machine.active
        machine_printer.display(filtered_machines)
        sys.exit(0)

    filtered_machines = {}
    if args.name:
        filtered_machines.update(filters.name_filter(machines, args.name))

    if args.ip:
        filtered_machines.update(filters.ip_filter(machines, args.ip))
    machine_printer.display(filtered_machines)


if __name__ == "__main__":
    main()
