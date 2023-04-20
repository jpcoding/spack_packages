# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.build_systems.cmake import CMakeBuilder
from spack.package import *

class Numcpp(CMakePackage):
    """NumCpp: A Templatized Header Only C++ Implementation of the Python NumPy Library"""

    homepage = "https://dpilger26.github.io/NumCpp/doxygen/html/index.html"
    url = "https://github.com/dpilger26/NumCpp/archive/refs/tags/Version_2.10.1.tar.gz"
    git = "https://github.com/dpilger26/NumCpp.git"

    maintainers("jpcoding")

    version("master", branch="master")
    version("2.10.1", branck="6058ecdd0a0cc49422862b85a5256ead91600e8b")
