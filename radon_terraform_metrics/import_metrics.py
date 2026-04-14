# ---------------- COMPLEX METRICS ----------------

from .complex_metrics.complexity_score import ComplexityScore
from .complex_metrics.resource_sprawl import ResourceSprawl
from .complex_metrics.key_density import KeyDensity
from .complex_metrics.resource_concentration import ResourceConcentration
from .complex_metrics.avg_block_verbosity import AvgBlockVerbosity
from .complex_metrics.coupling_score import CouplingScore
from .complex_metrics.modularity_score import ModularityScore
from .complex_metrics.vocabulary_richness import VocabularyRichness



# ---------------- GENERAL METRICS ----------------

from .general.lines_code import LinesCode
from .general.lines_blank import LinesBlank
from .general.lines_comment import LinesComment
from .general.num_keys import NumKeys
from .general.num_suspicious_comments import NumSuspiciousComments
from .general.num_tokens import NumTokens
from .general.text_entropy import TextEntropy


# ---------------- TERRAFORM CONFIGURATION METRICS ----------------

# resources
from .configuration.num_resources import NumResources
from .configuration.avg_resource_size import AvgResourceSize
from .configuration.resource_type_diversity import ResourceTypeDiversity
from .configuration.resource_density import ResourceDensity
from .configuration.max_resources_per_file import MaxResourcesPerFile

# modules
from .configuration.num_modules import NumModules
from .configuration.module_reuse_count import ModuleReuseCount
from .configuration.module_fan_in import ModuleFanIn

# variables
from .configuration.num_variables import NumVariables
from .configuration.variables_per_resource import VariablesPerResource
from .configuration.variable_default_ratio import VariableDefaultRatio
from .configuration.variable_reference_count import VariableReferenceCount

# outputs / locals
from .configuration.num_outputs import NumOutputs
from .configuration.num_locals import NumLocals

# providers
from .configuration.num_providers import NumProviders
from .configuration.resources_per_provider import ResourcesPerProvider

# data sources
from .configuration.num_data_sources import NumDataSources

# provisioners
from .configuration.num_provisioners import NumProvisioners
from .configuration.provisioners_per_resource import ProvisionersPerResource

# dynamic behaviour
from .configuration.num_dynamic_blocks import NumDynamicBlocks
from .configuration.num_loops import NumLoops
from .configuration.num_conditionals import NumConditionals

# dependencies
from .configuration.num_dependencies import NumDependencies
from .configuration.avg_dependencies_per_resource import AvgDependenciesPerResource
from .configuration.implicit_dependencies import ImplicitDependencies
from .configuration.explicit_dependencies import ExplicitDependencies
from .configuration.dependency_graph_density import DependencyGraphDensity
from .configuration.max_dependency_lenght_chain import MaxDependencyChainLength

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

complex_metrics = {
    'complexity_score': ComplexityScore,
    'resource_sprawl': ResourceSprawl,
    'resource_concentration': ResourceConcentration,
    'avg_block_verbosity': AvgBlockVerbosity,
    'coupling_score': CouplingScore,
    'modularity_score': ModularityScore,
    'vocabulary_richness': VocabularyRichness,
    'key_density': KeyDensity,
}


# ---------------- TERRAFORM CONFIGURATION ----------------

configuration_metrics = {

    # resources
    'num_resources': NumResources,
    'avg_resource_size': AvgResourceSize,
    'resource_type_diversity': ResourceTypeDiversity,
    'resource_density': ResourceDensity,
    'max_resources_per_file': MaxResourcesPerFile,

    # modules
    'num_modules': NumModules,
    'module_reuse_count': ModuleReuseCount,
    'module_fan_in': ModuleFanIn,

    # variables
    'num_variables': NumVariables,
    'variables_per_resource': VariablesPerResource,
    'variable_default_ratio': VariableDefaultRatio,
    'variable_reference_count': VariableReferenceCount,

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
    'implicit_dependencies': ImplicitDependencies,
    'explicit_dependencies': ExplicitDependencies,
    'dependency_graph_density': DependencyGraphDensity,
    'max_dependency_chain_length': MaxDependencyChainLength
}