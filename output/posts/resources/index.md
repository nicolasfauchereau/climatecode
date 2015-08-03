<!--
.. title: resources
.. slug: resources
.. date: 2015-08-03 14:02:05 UTC+12:00
.. tags: resources,libraries,books,ipython notebooks,tutorials
.. category: resources
.. link:
.. description:
.. type: text
-->

A [incomplete] list of resources on Python and Python for data analysis and visualization, loosely organized by category:


### Object Oriented Programming in Python

+ [www.google.com](http://www.google.com)
+ [A good tutorial by Alan Gauld](http://www.freenetpages.co.uk/hp/alan.gauld/tutclass.htm)
+ The [classes](http://docs.python.org/2/tutorial/classes.html) entry from the official Python doc
 A short [pdf](http://www1.gly.bris.ac.uk/~walker/PythonEarthSci/PfES_3.pdf) from Andrew Walker's [Python for Earth Scientists](http://www1.gly.bris.ac.uk/~walker/PythonEarthSci/) course


### Python as a glue: wrapping of C, C++, Fortran or the Cython module  

+ [using python as a *glue*](http://docs.scipy.org/doc/numpy/user/c-info.python-as-glue.html)
+ [SWIG (Simplified Wrapper and Interface Generator)](http://www.swig.org/Doc1.3/Python.html)
+ [Cython](http://cython.org)
+ [f2py](http://www.f2py.com/)
+ [A notebook on using C and Fortran with Python](http://nbviewer.ipython.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-6A-Fortran-and-C.ipynb)

### Real-time acquisition, physical programming

+ [pyserial](http://pyserial.sourceforge.net): Module that encapsulates the access for the serial port
+ [Real World Instrumentation, Automated Data Acquisition and Control Systems](http://www.amazon.com/Real-World-Instrumentation-Python-Acquisition/dp/0596809565): A book available on Amazon.
+ [Programming Raspberry Pi: Getting Started with Python](http://www.monkmakes.com/?page_id=63): book (not free) with code (free)
+ [PyVISA](https://pyvisa.readthedocs.org/en/latest/): The PyVISA package enables you to control all kinds of measurement equipment through various busses (GPIB, RS232, USB) with Python programs

### Image processing

+ PIL [(Python Image Library)](http://www.pythonware.com/products/pil/): Image processing capabilities to your Python interpreter.
+ [pillow](http://python-pillow.github.io/): A more user-friendly `fork` of PIL
+ [scikit-image](http://scikit-image.org): more Image processing, built on top of Numpy / Scipy.

### Symbolic maths

+ The [SymPy](www.sympy.org) library is a Python library for symbolic mathematics. It supports polynomials, calculus, solving equations, etc
+ The [sage](http://www.sagemath.org/) software: `Mission: Creating a viable free open source alternative to Magma, Maple, Mathematica and Matlab`

### Geospatial statistics

+ [PySAL](http://pysal.readthedocs.org/en/v1.6/): PySAL is a cross-platform library of spatial analysis functions written in Python. It is intended to support the development of high level applications for spatial analysis.
+ [GeoPandas](http://geopandas.org/): A project based on [Pandas](http://pandas.pydata.org/) to make working with geospatial data in python easier
+ [Rasterio](https://github.com/mapbox/rasterio): Clean and fast and geospatial raster I/O with Numpy support, developed by the team at [https://www.mapbox.com/](https://www.mapbox.com/)
+ [Pyproj](https://code.google.com/p/pyproj/): Performs cartographic transformations and geodetic computations. Wrapper around the Proj version 4 library
+ [Python GDAL/OGR](https://pypi.python.org/pypi/GDAL/): Python bindings + tools around the Geospatial Data Abstraction Library
+ [Python GIS resources](http://pythongisresources.wordpress.com/interpolation): a blog on geospatial python
+ [High Performance Geostatistics Library](http://hpgl.mit-ufa.com/): A library written in C++ / Python implementing geostatistical algorithms (*e.g.* kriging, correlograms, etc)

### Biology, ecology

+ [Biopython](http://biopython.org/wiki/Main_Page): Biopython is a set of freely available tools for biological computation written in Python by an international team of developers.
+[GeoEco](https://pypi.python.org/pypi/GeoEco): Open source geoprocessing toolbox designed for coastal and marine researchers and GIS analysts who work with spatially-explicit ecological and oceanographic data. For Windows (> XP) only.
+ [Galaxy](http://galaxyproject.org/): Galaxy is a scientific workflow, data integration and data and analysis persistence and publishing platform that aims to make computational biology accessible to research scientists that do not have computer programming experience.

### Computational Fluid Dynamics and PDE solvers

+ [CFD Python: 12 steps to Navier-Stokes](http://lorenabarba.com/blog/cfd-python-12-steps-to-navier-stokes/)
+ [github repository for the above](https://github.com/barbagroup/CFDPython)
+ [Python bindings to OpenFOAM](http://openfoamwiki.net/index.php/Contrib_PyFoam)
+ [FiPy: A Finite Volume PDE Solver Using Python](http://matforge.org/fipy/)
+ ["Practical Numerical Methods with Python" MOOC](http://openedx.seas.gwu.edu/courses/GW/MAE6286/2014_fall/about)

### Python on the GPU

+[PyCUDA](http://mathema.tician.de/software/pycuda/): PyCUDA lets you access Nvidia‘s CUDA parallel computation API from Python

### Parallel computing with Python / IPython

+ [IPython parallel introduction](http://ipython.org/ipython-doc/2/parallel/parallel_intro.html)
+ [Interactive Parallel computing with IPython](https://www.youtube.com/watch?v=y4hgalfhc1Y&index=49&list=PLYx7XA2nY5GfuhCvStxgbynFNrxr3VFog): tutorials by Min. Raglan-Kelley at Scipy2014 (3 parts in the youtube list)
+ [IPython parallel for distributed computing](https://www.youtube.com/watch?v=eyUeYnT-18s&index=32&list=PLs4CJRBY5F1Jm7H1dlesRvEgr-28QGXpR): A talk at PyCON Australia by Nathan Faggian
+ [IPython & Jupyter in depth: high productivity interactive and parallel python](https://www.youtube.com/watch?v=05fA_DXgW-Y): A talk at PyCON 2015 by Thomas Kluyver and Kyle Kelley

### Signal processing in Python

+ [scipy.signal](http://docs.scipy.org/doc/scipy/reference/tutorial/signal.html)
+ [Python for signal processing blog](http://python-for-signal-processing.blogspot.co.nz/)
+ [Python for signal processing github repository](https://github.com/unpingco/Python-for-Signal-Processing)
+ [Python for signal processing book](http://www.springer.com/engineering/signals/book/978-3-319-01341-1)

### Python for Matlab and R users

+ [Moving from MATLAB matrices to NumPy arrays - A Matrix Cheatsheet](http://sebastianraschka.com/Articles/2014_matlab_vs_numpy.html)

+ [NumPy for Matlab Users](http://wiki.scipy.org/NumPy_for_Matlab_Users)


### Some URLs and blogs

+ [Python Scientific Lectures Notes](http://scipy-lectures.github.io): Tutorial material on the scientific Python ecosystem, a quick introduction to central tools and techniques.

+ [Python for earth scientists](http://www1.gly.bris.ac.uk/~walker/PythonEarthSci/): A two afternoons course by Andrew Walker (University of Bristol) on Python in the earth sciences.

+ [oceanpython](http://oceanpython.org/): Python for oceanography

+ [PyAOS](http://pyaos.johnny-lin.com/): Python for the Atmospheric and Oceanic Sciences

+ [python4oceanographers](http://ocefpaf.github.io/): Learn python with examples applied to marine sciences.

+ [Pythonic perambulations](http://jakevdp.github.io): A blog by Jake VanderPlas

### Github repositories: notebooks and accompanying material

+ [A gallery of interesting IPython Notebooks](https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks)
"...a curated collection of IPython notebooks that are notable for some reason."

+ [Scikit-learn tutorial](https://github.com/jakevdp/sklearn_scipy2013): Files and other info associated with the Scipy 2013 scikit-learn tutorial developed by Gaël Varoquaux, Olivier Grisel and Jake VanderPlas.

+ [Statistical Analysis tutorial](https://github.com/fonnesbeck/statistical-analysis-python-tutorial) from Chris. Fonnesbeck.

+ [Bayesian Statistical Analysis in Python](https://github.com/fonnesbeck/scipy2014_tutorial): Ipython notebooks for the Scipy 2014 tutorial on Bayesian data analysis with Python, by Chris. Fonnesbeck.

+ [AstroML: Machine Learning and Data Mining for Astronomy](http://www.astroml.org): A library and tutorial by Jake VanderPlas and co-authors, accompanying the book [Statistics, Data Mining, and Machine Learning in Astronomy](http://www.amazon.com/Statistics-Mining-Machine-Learning-Astronomy/dp/0691151687/)

+ [Scientific Python lectures from Robert Johansson](https://github.com/jrjohansson/scientific-python-lectures)

+ [Data Science in Python](http://blog.yhathq.com/posts/data-science-in-python-tutorial.html): A series of annotated notebooks on data science (i.e. geared towards machine learning) in python

+ [http://earthpy.org/](http://earthpy.org/): EarthPy is a collection of IPython notebooks with examples of Earth Science related Python code

+ [data science notebooks): IPython notebooks for data science, continually updated Data Science Python Notebooks: Spark, Hadoop MapReduce, HDFS, AWS, Kaggle, scikit-learn, matplotlib, pandas, NumPy, SciPy.

### Some books

+ [Python for Data Analysis](http://shop.oreilly.com/product/0636920023784.do): From Wes McKinney (Developer of [Pandas](www.pandas.pydata.org))

+ [Think stats](http://www.greenteapress.com/thinkstats/): Probability and statistics for programmers, from Allen Downey, pdf available for free.

+ [Think complexity](http://www.greenteapress.com/compmod/): Complexity science (graphs, cellular automata, agent-based models), from Allen Downey, pdf available for free.

+ [Python in hydrology](http://www.greenteapress.com/pythonhydro/pythonhydro.html): A book freely available in pdf, from Sat Kumar Tomer.

+ [Programming collective intelligence](http://shop.oreilly.com/product/9780596529321.do): By Toby Segaran, Good intro on (general) Machine Learning algorithms.

+ [Machine Learning in action](http://www.manning.com/pharrington/): By Peter Harrington.

+ [Introduction to Python for Econometrics, Statistics and Numerical Analysis: Second Edition](http://www.kevinsheppard.com/images/0/09/Python_introduction.pdf): By Kevin Sheppard, Oxford Uni.

+ [A Hands-On Introduction to Using Python in the Atmospheric and Oceanic Sciences](http://www.johnny-lin.com/pyintro/): By [Johnny Lin](http://www.johnny-lin.com), Professor of physics and head of the Climate Research Group at North Park University.

+ [principles of planetary climate](http://geosci.uchicago.edu/~rtp1/PrinciplesPlanetaryClimate/index.html): by Ray Pierrehumbert. Excellent book on the physics of planetary climates, with freely downloadable python code to follow the examples given in the book.

### Some interesting libraries, built on top of the main Scientific stack

+ [PYMC](http://pymc-devs.github.io/pymc/): By Chris Fonnesbeck, Bayesian statistical models and fitting algorithms, including Markov chain Monte Carlo.

+ [Seaborn](http://www.stanford.edu/~mwaskom/software/seaborn/): Statistical data visualization, by Michael Waskom. Its [graphical representation of linear models](http://www.stanford.edu/~mwaskom/software/seaborn/linear_models.html) is particularly interesting.

+ [ggplot](https://github.com/yhat/ggplot/): For [R](http://cran.r-project.org) users, a 'port' of the [ggplot2](http://ggplot2.org) package to Python, see [here](http://blog.yhathq.com/posts/ggplot-0.4-released.html) for what's new in the latest release.

+ [coards](https://pypi.python.org/pypi/coards): A COARDS compliant time parser. See also [netcdftime](http://netcdf4-python.googlecode.com/svn/trunk/docs/netcdftime.netcdftime-module.html) which is part of the [NetCDF4 module](https://code.google.com/p/netcdf4-python/)

+ [seawater](http://www.imr.no/~bjorn/python/seawater/index.html): Similar to the MATLAB toolboxes SEAWATER from CSIRO and parts of OCEANS from Woods Hole Institute.

+ [fluid](https://pypi.python.org/pypi/fluid): Procedures to study fluids on Python, focused for oceanography, meteorology and related sciences.

+ [kyPyWavelet](https://github.com/regeirk/kPyWavelet): Continuous wavelet transform module for Python *ala* Torrence and Compo. Some manual edits were necessary to make it work for me ...

+ [pyresample](https://code.google.com/p/pyresample/): Resampling (reprojection) of geospatial image data in Python

+ [Rpy2](http://rpy.sourceforge.net/rpy2.html): calling R from Python

### Some articles on open and reproducible research

+ [Reproducible Research in Computational Science](http://dx.doi.org/10.1126/science.1213847), Roger D. Peng, Science 334, 1226 (2011).

+ [Shining Light into Black Boxes](http://dx.doi.org/10.1126/science.1218263), A. Morin et al., Science 336, 159-160 (2012).

+ [The case for open computer programs](http://dx.doi.org/doi:10.1038/nature10836), D.C. Ince, Nature 482, 485 (2012).

+ [Best practices for scientific computing](http://www.plosbiology.org/article/info%3Adoi%2F10.1371%2Fjournal.pbio.1001745): Paper in PLOS Biology exposing some of the tools and methods to build better Scientific software.
