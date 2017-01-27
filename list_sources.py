#!/usr/bin/env python

from sys import stdout
from json import dumps
from SwitchAudioSource import get_sources


output_items = filter(lambda source: source.output, get_sources())
items = map(lambda source: source.__dict__, output_items)

json_output = dumps({
    "items": items
})

stdout.write(json_output)
