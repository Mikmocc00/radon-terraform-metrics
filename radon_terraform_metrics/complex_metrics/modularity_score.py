from radon_terraform_metrics.configuration.num_locals import NumLocals

from radon_terraform_metrics.configuration.module_reuse_count import ModuleReuseCount
from radon_terraform_metrics.configuration.num_resources import NumResources


class ModularityScore:
    """
    Misura quanto il file sfrutta l'astrazione tramite locals e moduli riusati.
    Formula: (num_locals + module_reuse_count) / num_resources
    Alto = buon uso dell'astrazione rispetto alle risorse dichiarate.
    """

    def __init__(self, script):
        self.script = script

    def compute(self):

        locals_ = NumLocals(self.script).count()
        reuse = ModuleReuseCount(self.script).count()
        resources = NumResources(self.script).count()

        if resources == 0:
            return 0.0

        return (locals_ + reuse) / resources