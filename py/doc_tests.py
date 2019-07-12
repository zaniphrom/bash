#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

fname = "../docs"
print "The files with images:\n"

# walk through files in directory
# find the ones with an image
for root, dirs, files in os.walk(fname):
  for file in files:
        if file.endswith(".rst"):
             sources = (os.path.join(root, file))
             with open(sources, 'r') as searchfile:
               for line in searchfile:
                 if re.search(r'\.\. image::', line, re.DOTALL):
                   print "- File: %s\n\t- Image: %s\n" % \
                         (sources, (line.strip()[10:]))
