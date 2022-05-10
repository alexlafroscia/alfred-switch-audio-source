#!/usr/bin/env python3

from sys import stdout, argv
from json import dumps
from SwitchAudioSource import get_sources


items = [source.__dict__ for source in get_sources() if source.type == argv[1]]

json_output = dumps({
    "items": list(items)
})

stdout.write(json_output)
