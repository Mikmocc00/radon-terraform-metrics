# General metrics
from general.lines_code import LinesCode
from general.lines_blank import LinesBlank
from general.lines_comment import LinesComment
from general.num_keys import NumKeys
from general.num_suspicious_comments import NumSuspiciousComments
from general.num_tokens import NumTokens
from general.text_entropy import TextEntropy


# Terraform configuration scope
from configuration.num_resources import NumResources
from configuration.num_modules import NumModules
from configuration.num_variables import NumVariables
from configuration.num_outputs import NumOutputs
from configuration.num_locals import NumLocals
from configuration.num_providers import NumProviders
from configuration.num_data_sources import NumDataSources
from configuration.num_provisioners import NumProvisioners
from configuration.num_dynamic_blocks import NumDynamicBlocks
from configuration.num_loops import NumLoops
from configuration.num_conditionals import NumConditionals
from configuration.resource_type_diversity import ResourceTypeDiversity
from configuration.avg_resource_size import AvgResourceSize
from configuration.num_dependencies import NumDependencies
from configuration.resource_density import ResourceDensity
from configuration.variables_per_resource import VariablesPerResource
from configuration.provisioners_per_resource import ProvisionersPerResource
from configuration.module_reuse_count import ModuleReuseCount
from configuration.resources_per_provider import ResourcesPerProvider
from configuration.variable_default_ratio import VariableDefaultRatio
from configuration.avg_dependencies_per_resource import AvgDependenciesPerResource
from configuration.implicit_dependencies import ImplicitDependencies
from configuration.module_fan_in import ModuleFanIn


# ---------------- GENERAL ----------------

general_metrics = {
    'lines_code': LinesCode,
    'lines_blank': LinesBlank,
    'lines_comment': LinesComment,
    'num_keys': NumKeys,
    'num_suspicious_comments': NumSuspiciousComments,
    'num_tokens': NumTokens,
    'text_entropy': TextEntropy
}


# ---------------- TERRAFORM CONFIGURATION ----------------

configuration_metrics = {

    # resources
    'num_resources': NumResources,
    'avg_resource_size': AvgResourceSize,
    'resource_type_diversity': ResourceTypeDiversity,
    'resource_density': ResourceDensity,

    # modules
    'num_modules': NumModules,
    'module_reuse_count': ModuleReuseCount,
    'module_fan_in': ModuleFanIn,

    # variables
    'num_variables': NumVariables,
    'variables_per_resource': VariablesPerResource,
    'variable_default_ratio': VariableDefaultRatio,

    # outputs / locals
    'num_outputs': NumOutputs,
    'num_locals': NumLocals,

    # providers
    'num_providers': NumProviders,
    'resources_per_provider': ResourcesPerProvider,

    # data sources
    'num_data_sources': NumDataSources,

    # provisioners
    'num_provisioners': NumProvisioners,
    'provisioners_per_resource': ProvisionersPerResource,

    # dynamic behaviour
    'num_dynamic_blocks': NumDynamicBlocks,
    'num_loops': NumLoops,
    'num_conditionals': NumConditionals,

    # dependencies
    'num_dependencies': NumDependencies,
    'avg_dependencies_per_resource': AvgDependenciesPerResource,
    'implicit_dependencies': ImplicitDependencies
}