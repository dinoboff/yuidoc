#!/bin/sh

# The location of the files to parse.  Parses subdirectories, but will fail if
# there are duplicate file names in these directories.  You can specify multiple
# source trees:
#     parser_in="~/www/yui/src ~/www/event/src"
parser_in=%(parser_in)s

# The location to output the parser data.  This output is a file containing a
# json string, and copies of the parsed files.
parser_out=%(parser_out)s

# The directory to put the html file outputted by the generator
generator_out=%(generator_out)s

# The location of the template files.  Any subdirectories here will be copied
# verbatim to the destination directory.
template=%(template)s

# The version of your project to display within the documentation.
version="%(version)s"

# The version of YUI the project is using.  This effects the output for
# YUI configuration attributes.  This should start with '2' or '3'.
yuiversion=%(yui_version)s

##############################################################################

yuidoc $parser_in -p $parser_out -o $generator_out -t $template -v $version -Y $yuiversion %(extra)s
