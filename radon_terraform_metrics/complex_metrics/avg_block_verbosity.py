from radon_terraform_metrics.general.num_tokens import NumTokens
from radon_terraform_metrics.configuration.num_resources import NumResources


class AvgBlockVerbosity:
    """
    Misura quanto è verboso in media ogni blocco risorsa
    in termini di token HCL.
    Formula: num_tokens / num_resources
    Alto = blocchi molto verbosi, potenzialmente over-engineered.
    """

    def __init__(self, script):
        self.script = script

    def compute(self):

        tokens = NumTokens(self.script).count()
        resources = NumResources(self.script).count()

        if resources == 0:
            return 0.0

        return tokens / resources