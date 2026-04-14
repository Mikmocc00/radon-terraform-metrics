from radon_terraform_metrics.configuration.num_resources import NumResources
from radon_terraform_metrics.configuration.resource_type_diversity import ResourceTypeDiversity


class ResourceSprawl:
    """
    Misura se le risorse sono molte ma omogenee (sprawl)
    oppure poche e diversificate.
    Formula: num_resources / resource_type_diversity
    Alto = tante risorse dello stesso tipo (sprawl).
    Basso = risorse eterogenee e ben diversificate.
    """

    def __init__(self, script):
        self.script = script

    def compute(self):

        resources = NumResources(self.script).count()
        diversity = ResourceTypeDiversity(self.script).count()

        if diversity == 0:
            return 0.0

        return resources / diversity