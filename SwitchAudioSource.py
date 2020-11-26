from subprocess import check_output, call
from json import dumps
from sys import stdout
from os import environ


PATH_TO_SWITCH_AUDIO_OUTPUT = environ['SWITCH_AUDIO_SOURCE_PATH']
LOOKUP_WARNING = "Error: Could not find SwitchAudioSource"


class AudioSource:
    def __init__(self, description, active):
        words = description.split(' ')
        output = words.pop(-1)
        title = ' '.join(words)

        self.uid = title
        self.title = title
        self.arg = title
        self.autocomplete = title

        self.output = output.find('output') > -1
        self.input = not self.output
        self.icon = { "path": "icons/active.png" if active == title else "icons/inactive.png" }

    def __str__(self):
        return str(self.__dict__)


def get_sources():
    active = check_output([
        PATH_TO_SWITCH_AUDIO_OUTPUT, '-c'
    ]).strip()

    command_output = check_output([
        PATH_TO_SWITCH_AUDIO_OUTPUT, '-a'
    ])

    return map(lambda line: AudioSource(line, active), command_output.splitlines())


def set_output(device):
    command_output = check_output([
        PATH_TO_SWITCH_AUDIO_OUTPUT, '-s', device, '-t', 'output'
    ]).capitalize()
    stdout.write(command_output)

def set_input(device):
    command_output = check_output([
        PATH_TO_SWITCH_AUDIO_OUTPUT, '-s', device, '-t', 'input'
    ]).capitalize()
    stdout.write(command_output)


def no_path_provided():
    stdout.write(dumps({
        "items": [{
            "title": LOOKUP_WARNING
        }]
    }))
    exit()
