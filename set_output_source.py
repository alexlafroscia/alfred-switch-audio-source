#!/usr/bin/env python

from sys import argv
from SwitchAudioSource import set_output

query = argv[1]
set_output(query)
