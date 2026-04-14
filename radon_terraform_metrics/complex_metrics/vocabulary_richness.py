import math
import re
from collections import Counter

class VocabularyRichness:
    """
    Ricchezza lessicale:
    entropia / log2(token)
    """

    def __init__(self, script):
        self.script = script

    def count(self):

        tokens = re.findall(r'\S+', self.script)

        if len(tokens) < 2:
            return 0.0

        counts = Counter(tokens)
        total = len(tokens)

        entropy = -sum((c / total) * math.log2(c / total) for c in counts.values())

        max_entropy = math.log2(total)

        if max_entropy == 0:
            return 0.0

        return entropy / max_entropy