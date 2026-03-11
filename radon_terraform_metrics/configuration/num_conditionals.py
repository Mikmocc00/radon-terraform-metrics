import re


class NumConditionals:

    def __init__(self, script):
        self.script = script

    def count(self):

        return len(re.findall(r"\?.*:", self.script))