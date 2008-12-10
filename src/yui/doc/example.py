#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging, logging.config, os, shutil, sys
from os.path import abspath
from optparse import OptionParser
from pkg_resources import resource_filename, resource_string

try:
    logging.config.fileConfig(os.path.join(sys.path[0], const.LOGCONFIG))
except:
    try:
        logging.config.fileConfig(resource_filename(__name__, const.LOGCONFIG))
    except:
        pass

log = logging.getLogger('yuidoc.example')


class DocExample(object):

    def __init__(self, rootdir='./',
                 inputdirs=["src"],
                 parseroutdir="docs/parser",
                 outputdir="docs/generator",
                 templatedir="template",
                 showprivate=False,
                 version="1.0.0",
                 yuiversion="2"):

        # Created directories if they don't exists
        self.make_dir(rootdir)

        vars = {
            'parser_out': parseroutdir,
            'generator_out': outputdir,
        }

        for key in vars:
            dir_path = os.path.join(rootdir, vars[key])
            self.make_dir(dir_path)
            vars[key] = os.path.abspath(dir_path)

        vars['parser_in'] = []
        for dir_path in inputdirs:
            dir_path = os.path.join(rootdir, dir_path)
            self.make_dir(dir_path)
            vars['parser_in'].append(os.path.abspath(dir_path))
        vars['parser_in'] = ' '.join(vars['parser_in'])

        templatedir = os.path.join(rootdir, templatedir)
        self.create_template(templatedir)
        vars['template'] = os.path.abspath(templatedir)

        vars['version'] = version
        vars['yui_version'] = yuiversion

        if showprivate:
            vars['extra'] = "-s"
        else:
            vars['extra'] = ""

        self.create_file(os.path.join(rootdir, 'example.sh'),
                         unicode(resource_string(__name__, 'bin/example.sh'), 'utf-8'),
                         vars)
        self.create_file(os.path.join(rootdir, 'example.bat'),
                         unicode(resource_string(__name__, 'bin/example.bat'), 'utf-8'),
                         vars)


    def create_template(self, template_dir):
        if os.path.exists(template_dir):
            log.info( 'Template already exists (%s)', template_dir )
            return

        log.info( 'Creating template in "%s"...', template_dir )
        shutil.copytree( resource_filename( __name__, 'template' ), template_dir )

    def make_dir(self, dir_path):
        if os.path.exists(dir_path):
            return

        log.info('Creating "%s"...', dir_path)
        os.makedirs(dir_path)

    def create_file(self, file_path, template, vars):
        if os.path.exists(file_path):
            log.warning('%s already exists.', file_path)
            return

        log.info('Creating "%s"...', file_path)
        content = template % vars
        open(file_path, 'wb').write(content.encode('utf-8'))


def main():
    optparser = OptionParser("usage: %prog inputdir [options] [inputdir]")

    optparser.add_option( "-r", "--rootdir",
        action="store", dest="rootdir", type="string",
        help="Directory to write the yui example" )
    optparser.add_option( "-p", "--parseroutdir",
        action="store", dest="parseroutdir", type="string",
        help="Directory to write the parser temp data" )
    optparser.add_option( "-o", "--outputdir",
        action="store", dest="outputdir", type="string",
        help="Directory to write the html documentation" )
    optparser.add_option( "-t", "--template",
        action="store", dest="templatedir", type="string",
        help="The directory containing the html tmplate" )
    optparser.add_option( "-s", "--showprivate",
        action="store_true", dest="showprivate",
        help="Should private properties/methods be in the docs?" )
    optparser.add_option( "-v", "--version",
        action="store", dest="version", type="string",
        help="The version of the project" )
    optparser.add_option( "-Y", "--yuiversion",
        action="store", dest="yuiversion", type="string",
        help="The version of YUI library used in the project.  This parameter applies to the output for attributes, which differs between YUI2 and YUI3." )

    (options, inputdirs) = optparser.parse_args()

    kargs = {}
    for key, value in options.__dict__.iteritems():
        if value:
            kargs[key] = value

    if len(inputdirs) > 0:
        kargs['inputdirs'] = inputdirs

    DocExample(**kargs)

if __name__ == '__main__':
    main()
