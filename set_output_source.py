#!/usr/bin/env python

from sys import argv
from SwitchAudioSource import set_output, set_input, get_built_in_microphone, get_built_in_speaker

query = argv[1]

set_output(query)
if (query == get_built_in_speaker()):
  set_input(get_built_in_microphone())
else:
  set_input(query)