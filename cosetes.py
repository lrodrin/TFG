# ignorem repetits

# nodes
for i in range(0, len(colNames)):
	for row in rows:
    	G.add_node("%s:%s" % (colNames[i], rows[i]))

# arestes
for (u, v) in itertools.combinations(G.nodes(), 2):  
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

# llista per a l'estadística.
for num in d:
	if num == 0:
	elif num == 1:
	elif num == 2:
	elif 3 <= num <= 4:
	elif 5 <= num <= 8:
	elif 8 <= num <= 16:
