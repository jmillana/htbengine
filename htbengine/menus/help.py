"""Command line help menu."""
from termcolor import colored

from htbengine.style import colors


def help_menu() -> None:
    """Argparse help menu."""
    print(f"\n{colored('[!] Usage: ./htbengine.py', colors.RED)}")
    msg = "Explore Mode: The options can be combined"
    print(
        f"\n\t{colored('[-e, --explore]', colors.GREY)}"
        f"\t\t{colored(msg, colors.YELLOW)}"
        f"\t{colored('Example:', colors.RED)}"
        f" {colored('./htbengine.py', colors.GREEN)}"
        f" {colored('-e', colors.GREY)}"
        f" {colored('active linux spawned owned', colors.MAGENTA)}"
    )
    for machine_status in ["all", "active", "retired"]:
        print(
            f"\t\t{colored(machine_status, colors.MAGENTA)}"
            "\t\t\t"
            f"{colored(f'List {machine_status} machines', colors.YELLOW)}"
        )
    for os_name in ["windows", "linux", "freebds", "openbsd", "other"]:
        print(
            f"\t\t{colored(os_name, colors.MAGENTA)}"
            f"\t\t\t{colored(f'List {os_name} machines', colors.YELLOW)}"
        )

    print(
        f"\t\t{colored('spawned', colors.MAGENTA)}"
        f"\t\t\t{colored('List spawned machines', colors.YELLOW)}"
        f" {colored(' [Only for VIP members]', colors.RED)}"
    )
    print(
        f"\t\t{colored('owned', colors.MAGENTA)}"
        f"\t\t\t{colored('List owned machines', colors.YELLOW)}\n"
    )

    example_base = (
        f"\t{colored('Example:', colors.RED)}"
        f" {colored('./htbengine.py', colors.GREEN)}"
    )
    # Name arg
    print(
        f"\t{colored('[-n, --name]', colors.GREY)}"
        f"\t\t{colored('Search by machine name', colors.YELLOW)}"
        f"\t\t{example_base}"
        f" {colored('-n', colors.GREY)}"
        f" {colored('RedPanda', colors.MAGENTA)}\n"
    )
    print(
        f"\t{colored('[-i, --ip]', colors.GREY)}"
        f"\t\t{colored('Search by IP address', colors.YELLOW)}"
        f"\t\t{example_base}"
        f" {colored('-i', colors.GREY)}"
        f" {colored('10.10.11.170', colors.MAGENTA)}\n"
    )
    print(
        f"\t{colored('[-r, --reset]', colors.GREY)}"
        f"\t\t{colored('Reset a machine, requires --name', colors.YELLOW)}"
        f"{example_base}"
        f" {colored('-n', colors.GREY)}"
        f" {colored('RedPanda', colors.MAGENTA)}\n"
    )
    print(
        f"\t{colored('[-d, --deploy]', colors.GREY)}"
        f"\t\t{colored('Deploy a machine, requires --name', colors.YELLOW)}"
        f"{example_base}"
        f" {colored('-n', colors.GREY)}"
        f" {colored('RedPanda', colors.MAGENTA)}\n"
    )
    print(
        f"\t{colored('[-s, --stop]', colors.GREY)}"
        f"\t\t{colored('Stop a machine, requires --name', colors.YELLOW)}"
        f"\t{example_base}"
        f" {colored('-n', colors.GREY)}"
        f" {colored('RedPanda', colors.MAGENTA)}\n"
    )
    print(
        f"\t{colored('[-u, --user]', colors.GREY)}"
        f"\t\t{colored('Search a username', colors.YELLOW)}"
        f"\t\t{example_base}"
        f" {colored('-u', colors.GREY)}"
        f" {colored('jmillana', colors.MAGENTA)}\n"
    )
    print(
        f"\t{colored('[-v, --vpn]', colors.GREY)}"
        f"\t\t{colored('Download the VPN config file', colors.YELLOW)}"
        f"\t{example_base}"
        f" {colored('-v', colors.GREY)}"
        f" {colored('jmillana.ovpn', colors.MAGENTA)}\n"
    )
