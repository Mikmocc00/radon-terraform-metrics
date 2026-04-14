import math
from radon_terraform_metrics.general.text_entropy import TextEntropy
from radon_terraform_metrics.general.num_tokens import NumTokens


class VocabularyRichness:
    """
    Misura la diversità lessicale del file: quanto il vocabolario
    è ricco e non ripetitivo rispetto all'entropia massima possibile.
    Formula: text_entropy / log2(num_tokens)
    Valore in [0, 1]: vicino a 1 = vocabolario ricco e vario.
    """

    def __init__(self, script):
        self.script = script

    def compute(self):

        entropy = TextEntropy(self.script).count()
        tokens = NumTokens(self.script).count()

        if tokens < 2:
            return 0.0

        max_entropy = math.log2(tokens)

        if max_entropy == 0:
            return 0.0

        return entropy / max_entropy