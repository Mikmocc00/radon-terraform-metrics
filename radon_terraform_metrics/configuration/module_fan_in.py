import re


class ModuleFanIn:

    def __init__(self, script):
        self.script = script

    def count(self):

        return len(re.findall(r"module\.[a-zA-Z0-9_]+", self.script))