"""Define the parser for the HTB Engine."""
import argparse

from htbengine import models


class EmptyIsTrueAction(argparse.Action):
    """Action to treat empty arguments as True."""

    def __call__(self, parser, namespace, values, option_string=None):
        """Override the __call__ method to treat empty arguments as True."""
        if len(values) == 0:
            values = [True]
        setattr(namespace, self.dest, values)


def get_args():
    """Set the arguments for the script.

    Returns:
        argparse.Namespace: The arguments
    """
    parser = argparse.ArgumentParser(
        description="Get the machines from HTB API and"
        " save them in a cache file.",
        add_help=False,
    )
    explore_choices = (
        models.os.ALL
        + models.machine.STATUS
        + models.difficulty.ALL
        + [
            models.machine.BOOL_ATTRS.OWNED,
            models.machine.BOOL_ATTRS.SPAWNED,
            models.machine.BOOL_ATTRS.FREE,
        ]
    )

    parser.add_argument(
        "-e",
        "--explore",
        choices=explore_choices,
        nargs="*",
        action=EmptyIsTrueAction,
    )
    parser.add_argument(
        "-n",
        "--name",
        nargs="+",  # Allow multiple names, but at least one
        help="Filter machines by name",
    )
    parser.add_argument(
        "-i",
        "--ip",
        nargs="+",  # Allow multiple ip addresses, but at least one
        help="Filter machines by IP address",
    )
    parser.add_argument(
        "-r",
        "--reset",
        action=argparse.BooleanOptionalAction,
        help="Reset the given machines in the --name argument",
    )
    parser.add_argument(
        "-d",
        "--deploy",
        action=argparse.BooleanOptionalAction,
        help=(
            "Deploy the given machine in the --name argument, if more than "
            "one is given none will be deployed",
        ),
    )
    parser.add_argument(
        "-s",
        "--stop",
        action=argparse.BooleanOptionalAction,
        help=(
            "Stop the given machine in the --name argument, if more than "
            "one is given none will be stopped",
        ),
    )
    parser.add_argument(
        "-u",
        "--user",
        nargs="+",  # Allow multiple names, but at least one
        help="Get the information of the given user",
    )
    parser.add_argument(
        "-v",
        "--vpn",
        help=(
            "Download the VPN configuration file an store it in the given path"
        ),
    )
    parser.add_argument("-h", "--help", action=argparse.BooleanOptionalAction)
    return parser.parse_args()
