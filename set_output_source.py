#!/usr/bin/env python3

from sys import argv
from SwitchAudioSource import set_output

query = argv[1]
set_output(query)
