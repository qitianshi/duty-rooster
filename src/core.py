"""Core modules for Duty Rooster.

This module handles the import of the roostercore package from the core
submodule.
"""

# Copyright 2024 Qi Tianshi. All rights reserved.


import sys
import os

# Appends the core submodule to PYTHONPATH.
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'core'))

from roostercore import *
