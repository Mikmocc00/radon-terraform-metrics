import re


class NumKeys:

    def __init__(self, script):
        self.script = script

    def count(self):

        pattern = r'^\s*[a-zA-Z0-9_\-]+\s*='

        return len(re.findall(pattern, self.script, re.MULTILINE))