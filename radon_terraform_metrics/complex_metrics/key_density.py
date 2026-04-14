from radon_terraform_metrics.general.num_keys import NumKeys
from radon_terraform_metrics.configuration.num_resources import NumResources


class KeyDensity:
    """
    Misura la densità di configurazione: quante chiavi HCL
    sono presenti per ogni risorsa dichiarata.
    Formula: num_keys / num_resources
    Alto = risorse molto configurate/verbose.
    """

    def __init__(self, script):
        self.script = script

    def compute(self):

        keys = NumKeys(self.script).count()
        resources = NumResources(self.script).count()

        if resources == 0:
            return 0.0

        return keys / resources