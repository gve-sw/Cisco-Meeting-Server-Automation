# flake8: noqa

import pkg_resources
import warnings

try:

    __version__ = pkg_resources.get_distribution("et").version

except pkg_resources.DistributionNotFound as e:  # pragma: no cover

    warnings.warn("can't get __version__ because %s package isn't installed" % __package__, Warning)
    __version__ = None

