#!/usr/bin/env python

from sys import argv
from SwitchAudioSource import set_input

query = argv[1]
set_input(query)
