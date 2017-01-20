# ignorem repetits

# nodes
for i in range(0, len(colNames)):
	for row in rows:
    	G.add_node("%s:%s" % (colNames[i], rows[i]))

# arestes
for (u, v) in itertools.combinations(G.nodes(), 2):  # For each pair (x, y) in the subset combinations
	G.edge(u, v, color='white')

for row in rows:
	for (u, v) in intertools.combinations(row, 2)
		G.add_edge(u, v, color='black')


# no ignorem repetits
# comptem quants repetits

# arestes
d = dict()
cont = 0
for row in rows:
	for (u, v) in intertools.combinations(row, 2)
	if d[tuple(u, v)] not in d:
		d[tuple(u, v)] = 1
	else:
		cont += 1
		d[tuple(u, v)] = cont
