#!/usr/bin/env python3

import os


def print_venv():
    try:
        print("Your current virtual env is", os.environ['VIRTUAL_ENV'])
    except KeyError as err:
        print("KeyError: no virtual environment", err)


if __name__ == '__main__':
    print_venv()


# python3 -m virtualenv scornhol
# source scornhol/bin/activate
# deactivate
