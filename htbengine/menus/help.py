"""Command line help menu."""
from termcolor import colored

RED_COLOR = "red"
GREEN_COLOR = "green"
YELLOW_COLOR = "yellow"
BLUE_COLOR = "blue"
MAGENTA_COLOR = "magenta"
CYAN_COLOR = "cyan"
WHITE_COLOR = "white"
GREY_COLOR = "grey"


def help_menu() -> None:
    """Argparse help menu."""
    print(f"\n{colored('[!] Usage: ./htbengine.py', RED_COLOR)}")
    msg = "Explore Mode: The options can be combined"
    print(
        f"\n\t{colored('[-e, --explore]', GREY_COLOR)}"
        f"\t\t{colored(msg, YELLOW_COLOR)}"
        f"\t{colored('Example:', RED_COLOR)}"
        f" {colored('./htbengine.py', GREEN_COLOR)}"
        f" {colored('-e', GREY_COLOR)}"
        f" {colored('active linux spawned owned', MAGENTA_COLOR)}"
    )
    for machine_status in ["all", "active", "retired"]:
        print(
            f"\t\t{colored(machine_status, MAGENTA_COLOR)}"
            f"\t\t\t{colored(f'List {machine_status} machines', YELLOW_COLOR)}"
        )
    for os_name in ["windows", "linux", "freebds", "openbsd", "other"]:
        print(
            f"\t\t{colored(os_name, MAGENTA_COLOR)}"
            f"\t\t\t{colored(f'List {os_name} machines', YELLOW_COLOR)}"
        )

    print(
        f"\t\t{colored('spawned', MAGENTA_COLOR)}"
        f"\t\t\t{colored('List spawned machines', YELLOW_COLOR)}"
        f" {colored(' [Only for VIP members]', RED_COLOR)}"
    )
    print(
        f"\t\t{colored('owned', MAGENTA_COLOR)}"
        f"\t\t\t{colored('List owned machines', YELLOW_COLOR)}\n"
    )

    example_base = (
        f"\t{colored('Example:', RED_COLOR)}"
        f" {colored('./htbengine.py', GREEN_COLOR)}"
    )
    # Name arg
    print(
        f"\t{colored('[-n, --name]', GREY_COLOR)}"
        f"\t\t{colored('Search by machine name', YELLOW_COLOR)}"
        f"\t\t{example_base}"
        f" {colored('-n', GREY_COLOR)}"
        f" {colored('RedPanda', MAGENTA_COLOR)}\n"
    )
    print(
        f"\t{colored('[-i, --ip]', GREY_COLOR)}"
        f"\t\t{colored('Search by IP address', YELLOW_COLOR)}"
        f"\t\t{example_base}"
        f" {colored('-i', GREY_COLOR)}"
        f" {colored('10.10.11.170', MAGENTA_COLOR)}\n"
    )
    print(
        f"\t{colored('[-r, --reset]', GREY_COLOR)}"
        f"\t\t{colored('Reset a machine, requires --name', YELLOW_COLOR)}"
        f"{example_base}"
        f" {colored('-n', GREY_COLOR)}"
        f" {colored('RedPanda', MAGENTA_COLOR)}\n"
    )
    print(
        f"\t{colored('[-d, --deploy]', GREY_COLOR)}"
        f"\t\t{colored('Deploy a machine, requires --name', YELLOW_COLOR)}"
        f"{example_base}"
        f" {colored('-n', GREY_COLOR)}"
        f" {colored('RedPanda', MAGENTA_COLOR)}\n"
    )
    print(
        f"\t{colored('[-s, --stop]', GREY_COLOR)}"
        f"\t\t{colored('Stop a machine, requires --name', YELLOW_COLOR)}"
        f"\t{example_base}"
        f" {colored('-n', GREY_COLOR)}"
        f" {colored('RedPanda', MAGENTA_COLOR)}\n"
    )
    print(
        f"\t{colored('[-u, --user]', GREY_COLOR)}"
        f"\t\t{colored('Search a username', YELLOW_COLOR)}"
        f"\t\t{example_base}"
        f" {colored('-u', GREY_COLOR)}"
        f" {colored('jmillana', MAGENTA_COLOR)}\n"
    )
    print(
        f"\t{colored('[-v, --vpn]', GREY_COLOR)}"
        f"\t\t{colored('Download the VPN config file', YELLOW_COLOR)}"
        f"\t{example_base}"
        f" {colored('-v', GREY_COLOR)}"
        f" {colored('jmillana.ovpn', MAGENTA_COLOR)}\n"
    )
