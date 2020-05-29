# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# this one to build locally
# sys.path.insert(0, os.path.abspath('../../../c4h_timers/'))
# this one to build on RTD
# sys.path.insert(0, os.path.abspath('../../../../c4h_timers/'))
#sys.path.insert(0, os.path.abspath('../../c4h_timers/'))
# sys.path.insert(0, os.path.abspath('../c4h_timers/'))
# sys.path.insert(0, os.path.abspath('c4h_timers/'))
# sys.path.insert(0, os.path.abspath('c4h_timers'))
# sys.path.insert(0, os.path.abspath('docs'))
#sys.path.insert(0, os.path.abspath('.'))

#find the bloody path

mod_path = '../c4h_timers/'
if os.path.exists(os.path.abspath(mod_path)):
    sys.path.insert(0,os.path.abspath(mod_path))
    print('1 ',os.path.abspath(mod_path))

mod_path = '../'+mod_path
if os.path.exists(os.path.abspath(mod_path)):
    sys.path.insert(0,os.path.abspath(mod_path))
    print('2 ',os.path.abspath(mod_path))

mod_path = '../'+mod_path
if os.path.exists(os.path.abspath(mod_path)):
    sys.path.insert(0,os.path.abspath(mod_path))
    print('3 ', os.path.abspath(mod_path))

mod_path = '../'+mod_path
if os.path.exists(os.path.abspath(mod_path)):
    sys.path.insert(0,os.path.abspath(mod_path))
    print('4 ', os.path.abspath(mod_path))



# -- Project information -----------------------------------------------------

project = 'Courses4Horses Timers'
copyright = '2020, Geoffysicist'
author = 'Geoffysicist'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

master_doc = 'index'
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.coverage', #what is this for
    ]

napoleon_google_docstring = True

autodoc_mock_imports = [
    'neopixel',
    'board',
    ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']