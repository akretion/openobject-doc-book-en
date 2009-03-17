# -*- coding: utf-8 -*-
#
# Logistic, Stock & MRP documentation build configuration file, created by
# sphinx-quickstart on Mon Mar  9 11:55:03 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed automatically).
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
from docutils import nodes
sys.path.append('../../source')
from conf import *

TO_BE_DEFINED = None

master_doc = 'index'

# General information about the project.
project = TO_BE_DEFINED
copyright = TO_BE_DEFINED

version = '1.0'
release = '1.0'

# List of documents that shouldn't be included in the build.
unused_docs = [
]

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = [
]

# Options for HTML output
# -----------------------

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
html_style = 'default.css'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = TO_BE_DEFINED

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

htmlhelp_basename = TO_BE_DEFINED


# Options for LaTeX output
# ------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'a4'

# The font size ('10pt', '11pt' or '12pt').
latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).

latex_documents = [
  TO_BE_DEFINED
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = '.static/openerp.jpg'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = True

# Additional stuff for the LaTeX preamble.
#latex_preamble = '' # DEPRECATED sinc sphinx 0.5 (use 'latex_elements')

tiny_latex_include = r"""
\usepackage{flowfram}
\usepackage{multicol}

\usepackage[]{geometry}
\geometry{papersize={189mm,246mm},top=15mm,bottom=28mm,left=15mm,right=15mm,bindingoffset=5mm}

\DeclareUnicodeCharacter{00A0}{~}

\definecolor{NoticeBoxBg}{rgb}{0.90,0.90,0.90}

\newlength{\boxwidth}

\newenvironment{NoticeBox}{%
  \def\FrameCommand{\fboxsep=\FrameSep \fboxrule=\FrameRule \fcolorbox{black}{NoticeBoxBg}}%
  \MakeFramed {\setlength{\boxwidth}{\textwidth}
  \addtolength{\boxwidth}{-2\FrameSep}
  \addtolength{\boxwidth}{-2\FrameRule}
  \setlength{\hsize}{\boxwidth} \FrameRestore}}%
{\endMakeFramed}

\makeatletter
\renewenvironment{notice}[2]{
  \begin{samepage}
  \begin{NoticeBox}
  \def\py@noticetypetip{tip}
  \def\py@noticetypenote{note}
  \def\py@noticetype{#1}

  \begin{tabular}{ccl}
    \ifx\py@noticetype\py@noticetypetip
      \scalebox{0.500000}{\includegraphics{tip.png}}
    \else
      \scalebox{0.8}{\includegraphics{note.png}}
    \fi
    &
    \raisebox{5mm}{\strong{#2}}
    \vspace{3mm}
  \end{tabular}
  \linebreak
  \nopagebreak[4]
}
{
  \end{NoticeBox}
  \end{samepage}
}
\makeatother

\renewenvironment{figure}[6]{
  \par
  \addvspace{5mm}
  \begin{staticfigure}
}{
  \end{staticfigure}
  \addvspace{10mm}
}
"""

latex_elements = {
    'preamble': tiny_latex_include,
}

#     self.body.append("\n".join(["\\mainmatter", "\\pagenumbering{arabic}", "\\setcounter{page}{1}", '']))

def end_foreword_directive(name, arguments, options, content, lineno,
                       content_offset, block_text, state, state_machine):

    return [nodes.Text('SPHINXENDFOREWORDDIRECTIVE')] # XXX cannot add a raw node for the moment
    # return [nodes.raw('latex', '\\mainmatter')]

# def create_new_reference(app, env, node, contnode):
#     """Convert a bad reference into a simple text."""
#     txt = node.astext()
#     return [nodes.emphasis(txt, txt)]


def setup(app):
    app.add_directive('end_foreword', end_foreword_directive, 1, (0, 0, 0))
    #app.connect('missing-reference', create_new_reference)



