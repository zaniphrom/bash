#!/bin/bash

# Set these to get the HTML files and appropriate CSS files
# Note: as this searches the HTML files, you need to have that built
files="$(find _build/html/*.html -type f)"
CSS="$(find _build/html/_static/bootstrap-4.0.0-alpha2/css/bootstrap.css -type f)"

# Get the CSS properties by matching what's before the "{" on each line. Then
# for those lines with multiple properties, change the "'" separator to a
# newline and remove whitespace before and after each.

x=`awk 'match($0, "\.{") {print substr($0, 0, RSTART -1)}' $CSS | tr ',' '\n' \
  | awk '{printf "%s\n", $0}' | awk '{$1=$1}1'`

# For each CSS tag, iterate through the HTML files and get a match.
# Count the matches. A 0 count should mean the CSS is not used.
# 'Should', but not guaranteed. For example 'p.caption' is definitely used in
# this doc set. Setting the IFS to a new line is necessary as the default
# space, " ", breaks when it encounters CSS properties with a space, for example
# ".pagination-lg .page-item:first-child .page-link"
IFS=$'\n'
for i in $x
  do
    awk -v pat=$i '$0 ~ pat { nmatches++ } END \
      {print "-", pat, ": Total matches:", nmatches, "found"}' $files
  done

# Usage tips
# .scripts/find-css-properties.sh | grep -ie "  found" # unmatched CSS
# .scripts//find-css-properties.sh | grep -v "  found"