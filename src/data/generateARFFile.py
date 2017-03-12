"""
This module implements generate a ARFF file

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import re

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

d = {'gardai-plan-crackdown-on-troublemakers-at-protest-2438316.html': {'dail': 1, 'focus': 1, 'actions': 1, 'trade': 2,
                                                                        'protest': 1, 'identify': 1}}

for original_filename in d.keys():
    m = re.search('^(.*)\.html$', original_filename, )
    if not m:
        print("Ignoring the file:", original_filename)
        continue
    output_filename = m.group(1) + '.arff'
    with open(output_filename, "w") as fp:
        fp.write('''@RELATION wordcounts

@ATTRIBUTE word string
@ATTRIBUTE count numeric

@DATA
''')
        for word_and_count in d[original_filename].items():
            fp.write("%s,%d\n" % word_and_count)
