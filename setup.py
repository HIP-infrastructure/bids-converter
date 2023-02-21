#!/usr/bin/env python

# Copyright (C) 2022, The HIP team and Contributors, All rights reserved.
#  This software is distributed under the open-source XXX license.

"""`Setup.py` for bids_tools."""
from os import path as op
from setuptools import setup
import versioneer


def main():
    """Main function of bids_tools ``setup.py``"""
    root_dir = op.abspath(op.dirname(__file__))

    version = None
    cmdclass = {}
    if op.isfile(op.join(root_dir, "bids_tools", "VERSION")):
        with open(op.join(root_dir, "bids_tools", "VERSION")) as vfile:
            version = vfile.readline().strip()

    if version is None:
        version = versioneer.get_version()
        cmdclass = versioneer.get_cmdclass()

    # Setup configuration
    setup(
        name="bids_tools",
        version=version,
        cmdclass=cmdclass,
    )


if __name__ == "__main__":
    main()
