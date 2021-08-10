from subprocess import check_output
from json import dumps, loads
from sys import stdout
from os import environ


PATH_TO_SWITCH_AUDIO= environ['SWITCH_AUDIO_SOURCE_PATH']
LOOKUP_WARNING = "Error: Could not find SwitchAudioSource"


class AudioSource:
    def __init__(self, description, active_output, active_input):
        audioSourceJSON = loads(description)
        title = audioSourceJSON["name"]
        self.uid = audioSourceJSON["uid"]
        self.arg = audioSourceJSON["id"]
        self.title = title
        self.autocomplete = title
        self.type = audioSourceJSON["type"]

        if self.type == "output":
            active = active_output
        else:
            active = active_input

        self.icon = {"path": "icons/active.png" if active ==
                     title else "icons/inactive.png"}

    def __str__(self):
        return str(self.__dict__)


def get_sources():
    active_output = check_output([
        PATH_TO_SWITCH_AUDIO, '-c', '-t' 'output'
    ]).strip()

    active_input = check_output([
        PATH_TO_SWITCH_AUDIO, '-c', '-t' 'input'
    ]).strip()

    command_output = check_output([
        PATH_TO_SWITCH_AUDIO, '-a', '-f', 'json'
    ])

    return map(lambda line: AudioSource(line, active_output, active_input), command_output.splitlines())


def get_current_output():
    command_output = check_output([
        PATH_TO_SWITCH_AUDIO, '-c', '-t', 'output', '-f', 'json' # being explicit, but should default to `-t output`
    ]).replace("\n", "")
    stdout.write(loads(command_output)["id"])

def get_current_input():
    command_output = check_output([
        PATH_TO_SWITCH_AUDIO, '-c', '-t', 'input', '-f', 'json'
    ]).replace("\n", "")
    stdout.write(loads(command_output)["id"])

def set_input(device):
    command_output = check_output([
        PATH_TO_SWITCH_AUDIO, '-i', device, '-t', 'input'
    ]).capitalize()
    stdout.write(command_output)


def set_output(device):
    check_output([
        PATH_TO_SWITCH_AUDIO, '-i', device, '-t', 'output'
    ])
    stdout.write(device)


def no_path_provided():
    stdout.write(dumps({
        "items": [{
            "title": LOOKUP_WARNING
        }]
    }))
    exit()
