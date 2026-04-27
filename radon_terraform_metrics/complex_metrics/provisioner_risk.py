from ..configuration.num_provisioners import NumProvisioners
from ..configuration.provisioners_per_resource import ProvisionersPerResource
from complexity_score import ComplexityScore

class ProvisionerRisk:
    """
    Rischio provisioner:
    num_provisioners * provisioners_per_resource * complexity_score
    """

    def __init__(self, script):
        self.script = script

    def count(self):

        num = NumProvisioners(self.script).count()
        per_res = ProvisionersPerResource(self.script).count()
        complexity = ComplexityScore(self.script).count()

        return num * per_res * complexity