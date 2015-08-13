<!--
.. title: Miniconda installation
.. slug: miniconda-installation
.. date: 2015-08-13 16:40:15 UTC+12:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

Below is a `bash` script to install [Miniconda](http://conda.pydata.org/miniconda.html) and set up a root environment containing all the libraries that I routinely use and that are necessary to
replicate the examples given in this blog.
<!-- TEASER_END -->
<br>
<br>


    #!/usr/bin/env bash
    # DOWNLOAD AND INSTALLS THE MINICONDA Python distribution
    # and a suite of Scientific Python packages
    # Nicolas Fauchereau <Nicolas.Fauchereau@niwa.co.nz>
    # 13/08/2015
    # ==============================================================================

    # download the minimal anaconda distribution (! uncomment the line
    # corresponding to your platform [linux or mac])
    #wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
    #wget https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O miniconda.sh

    # make the installer executable
    chmod +x miniconda.sh

    # set the installation directory, by default your HOME directory
    INSTALL_DIR=${HOME}

    # run the installer
    ./miniconda.sh -b -p ${INSTALL_DIR}/miniconda

    # add this line in the end of your .bashrc (linux) or .bash_profile (mac)
    export PATH=${INSTALL_DIR}/miniconda/bin:${PATH}

    # update conda (the package and environment manager) to the latest version
    ${INSTALL_DIR}/miniconda/bin/conda update --yes conda

    # install the required packages into
    # $INSTALL_DIR/miniconda/lib/python3.4/site-packages
    # NOTE: this package list might be expanded in the future, so I might
    # want to read if off a "requirements.txt" file ...

    packages=("ipython-notebook"
    "numpy"
    "scipy"
    "pandas"
    "matplotlib"
    "basemap"
    "netcdf4"
    "xray"
    "seaborn"
    "scikit-learn"
    "statsmodels"
    "odo"
    "dask")

    for item in ${packages[*]}
    do
        echo "====================================================================="
        echo "installing ${item}";
        ${INSTALL_DIR}/miniconda/bin/conda install --yes ${item};
    done
