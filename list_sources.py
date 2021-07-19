#!/usr/bin/env python

from sys import stdout, argv
from json import dumps
from SwitchAudioSource import get_sources



output_items = filter(lambda source: source.type == argv[1], get_sources())
items = map(lambda source: source.__dict__, output_items)

json_output = dumps({
    "items": items
})

stdout.write(json_output)
