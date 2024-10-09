"""Core modules for Duty Rooster.

This module handles the import of the roostercore package from the core
submodule.
"""

# Copyright 2024 Qi Tianshi. All rights reserved.


import os
import sys

# Appends the core submodule to PYTHONPATH.
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'core'))

# pylint: disable-next=wildcard-import,unused-wildcard-import,wrong-import-position
from roostercore import *
