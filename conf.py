import sys
import os
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../..'))
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'MetPy'
copyright = '2016, MetPy Developers'
exclude_patterns = []
pygments_style = 'sphinx'
html_static_path = ['_static']
htmlhelp_basename = 'MetPydoc'
