#!/usr/bin/env python3

from sys import argv
from SwitchAudioSource import set_input

query = argv[1]
set_input(query)
