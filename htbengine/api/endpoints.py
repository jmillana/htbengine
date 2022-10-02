"""HTB API info.

This module contains the HTB API info.
    * HTB_API_URL: The URL of the HTB API
    * HTB_API_VERSION: The version of the HTB API
    * HTB_API_BASE_URL: The base URL of the HTB API
"""
HTB_API_VERSION = "v4"
HTB_BASE_URL = f"https://www.hackthebox.eu/api/{HTB_API_VERSION}"
HTB_MACHINES_ACTIVE_URL = HTB_BASE_URL + "/machine/list"
HTB_MACHINES_RETIRED_URL = HTB_BASE_URL + "/machine/list/retired"
