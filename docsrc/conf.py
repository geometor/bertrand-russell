from photon_platform.publish.global_conf import *
import geometor.bertrand_russell as module

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "bertrand-russell"
repo_name = "bertrand-russell"

setup_globals(org, org_name, repo, repo_name)

project = "GEOMETOR • bertrand-russell"
author = "Bertrand Russell • Digital Edition GEOMETOR"
copyright = "1897, 1903 Cambridge University Press • Digital Edition GEOMETOR"

# Exclude top-level AutoAPI index included directly inside docsrc/modules/index.rst
_pkg_api_index = "modules/api/geometor/bertrand_russell/index.rst"
if _pkg_api_index not in exclude_patterns:
    exclude_patterns.append(_pkg_api_index)

# Retain only locally cached intersphinx inventories so offline builds emit zero network warnings
intersphinx_mapping = {
    name: target
    for name, target in intersphinx_mapping.items()
    if isinstance(target, tuple) and len(target) == 2 and target[1] is not None
}
