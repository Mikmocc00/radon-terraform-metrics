from radon_terraform_metrics.configuration.num_dynamic_blocks import NumDynamicBlocks
from radon_terraform_metrics.configuration.num_conditionals import NumConditionals
from radon_terraform_metrics.configuration.num_provisioners import NumProvisioners
from radon_terraform_metrics.configuration.num_resources import NumResources


class ComplexityScore:
    """
    Misura la complessità strutturale del file Terraform.
    Formula: (num_dynamic_blocks + num_conditionals + num_provisioners) / num_resources
    Alto = file strutturalmente complesso per risorsa dichiarata.
    """

    def __init__(self, script):
        self.script = script

    def compute(self):

        dynamic = NumDynamicBlocks(self.script).count()
        conditionals = NumConditionals(self.script).count()
        provisioners = NumProvisioners(self.script).count()
        resources = NumResources(self.script).count()

        if resources == 0:
            return 0.0

        return (dynamic + conditionals + provisioners) / resources