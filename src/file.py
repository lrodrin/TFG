"""
This module implements ...

Copyright (c) 2016-2017 Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>

Distributed under MIT license
[https://opensource.org/licenses/MIT]
"""
import src.final.Clan as c

__author__ = 'Laura Rodriguez Navas'
__license__ = 'MIT'

file = open("/Users/laura/PycharmProjects/graphs-edges-equivalences-code/src/file.txt", "w")
file.write("strict digraph "" {\n")
file.write("\tcompound=true;\n")

clansList = [{'C'}, {'A'}, {'E'}, {'D'}, {'B'}, {'E', 'D'}, {'D', 'E', 'A'}, {'D', 'E', 'A', 'B'}, {'D', 'B', 'E', 'A',
                                                                                                    'C'}]
external, internal = c.Clan.listClansDivision(clansList)

# nodes
for e in external:
    file.write("\t%s;\n" % "".join(e))

# subgraphs
info = '[label=" ",fillcolor=white,fixedsize=true,width=0.2];'

i = len(internal) - 1
j = i - 1
while i >= 0:
    if i != 0:
        file.write("\tsubgraph cluster_%s {\n" % "".join(internal[i]))
        file.write("\t\ts_%s %s\n" % ("".join(internal[j]), info))
        file.write("\t\ts_%s %s\n" % ("".join(internal[i].difference(internal[j])), info))
        file.write('\t\t{rank="same"; s_%s -> s_%s [arrowhead=none, color=black]; }\n\t}\n' %
                   ("".join(internal[i].difference(internal[j])), "".join(internal[j])))
    else:
        internal_i_aux = internal[i].copy()
        internal_i_aux2 = internal[i].copy()
        file.write("\tsubgraph cluster_%s {\n" % "".join(internal[i]))
        file.write("\t\ts_%s %s\n" % ("".join(internal_i_aux.pop()), info))
        file.write("\t\ts_%s %s\n" % ("".join(internal_i_aux), info))
        file.write('\t\t{rank="same"; s_%s -> s_%s [arrowhead=none, color=black]; }\n\t}\n' % (
            "".join(internal_i_aux2.pop()), "".join(internal_i_aux2)))
    i -= 1
    j -= 1

# links
for e in external:
    file.write('\ts_%s -> %s [arrowhead="none"];\n' % ("".join(e), "".join(e)))

i = len(internal) - 2
j = i - 1
while i >= 0:
    if i != 0:
        file.write('\ts_%s -> s_%s [arrowhead="none", lhead=cluster_%s];\n' % ("".join(internal[i]),
                                                                               "".join(internal[j]),
                                                                               "".join(internal[i])))
    else:
        internal_i_aux = internal[i].copy()
        file.write('\ts_%s -> s_%s [arrowhead="none", lhead=cluster_%s];\n' % (
            "".join(internal[i]), "".join(internal[i].pop()), "".join(internal_i_aux)))
    i -= 1
    j -= 1

file.write("}")
file.close()
