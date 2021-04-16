#
# @file   util.py
# @brief  Contains utility functions for this discord bot.
# @author ben <bwilliams@lincoln.ac.uk>
#

import os 
import json

def get_kv_format(key, value) -> str:

    # List? Return csv format
    if isinstance(value, list):
        return f"&{key}={','.join(value)}"

    # Otherwise return normal format
    else:
        return f"&{key}={value}"


def load_json(uri) -> object:
    with open(uri, 'r') as fp:
        return json.load(fp);


def get_token_from_file(filename) -> str:

    # No file? Die:
    if not os.path.isfile(filename):
        raise FileNotFoundError(
            f"Couldn't find {filename} (token for discord bot).")

    # File? cool, strip, return:
    with open(filename, 'r') as f:
        return f.readline().strip()
