import networkx as nx

import src.Clans as c
import src.iter_subsets as it
import src.primalClans as p

__author__ = "\"Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>"""

if __name__ == "__main__":

    G = nx.Graph()  # Create an empty graph structure (a “null graph”) with no nodes and no edges
    # Adding edges and edges attributes
    G.add_edges_from([('A', 'B'), ('B', 'D'), ('B', 'E'), ('D', 'E')], color='red')
    G.add_edges_from([('A', 'C'), ('B', 'C'), ('C', 'D'), ('C', 'E')], color='black')
    G.add_edges_from([('A', 'D'), ('A', 'E')], color='blue')
    subsetNodes = set(G.nodes())  # Subset of nodes from graph

    subset_isClan = {'D', 'E'}
    subset_notClan = {'A', 'B'}
    subset_isTrivial = {'A'}
    subset_notTrivial = {'A', 'D', 'B'}
    print(c.isAClan(G, subset_isClan))
    print(c.isAClan(G, subset_notClan))
    print((c.isATrivialClan(subset_isTrivial)))
    print(c.isATrivialClan(subset_notTrivial))
    print("-" * 20)

    clansList1 = []
    for s in it.all_subsets(subsetNodes):  # Subset iterator of each subsetNodes
        if c.isAClan(G, s):  # If s is a clan of graph
            clansList1.append(s)  # Add s to the list
    print(sorted(clansList1))  # Complete list of clans

    clansList2 = []
    for s in it.all_proper_subsets(subsetNodes):  # Subset iterator of each subsetNodes
        if c.isAClan(G, s):  # If s is a clan of graph
            clansList2.append(s)  # Add s to the list
    print(sorted(clansList2))  # Complete list of clans

    clansList3 = []
    for s in it.powerset_generator(subsetNodes):  # Subset iterator of each subsetNodes
        if c.isAClan(G, s):  # If s is a clan of graph
            clansList3.append(s)  # Add s to the list
    print(sorted(clansList3))  # Complete list of clans
    print("-" * 20)

    clansList = []
    for s in it.all_subsets(subsetNodes):  # Subset iterator of each subsetNodes
        if c.isAClan(G, s) and not c.isATrivialClan(s):  # If s is a clan of graph and isn't a trivial clan
            clansList.append(s)  # Add s to the list
    print(sorted(clansList))  # Complete list of clans less trivial clans

    clansList = []
    for s in it.all_proper_subsets(subsetNodes):  # Subset iterator of each subsetNodes
        if c.isAClan(G, s) and not c.isATrivialClan(s):  # If s is a clan of graph and isn't a trivial clan
            clansList.append(s)  # Add s to the list
    print(sorted(clansList))  # Complete list of clans less trivial clans

    clansList = []
    for s in it.powerset_generator(subsetNodes):  # Subset iterator of each subsetNodes
        if c.isAClan(G, s) and not c.isATrivialClan(s):  # If s is a clan of graph and isn't a trivial clan
            clansList.append(s)  # Add s to the list
    print(sorted(clansList))  # Complete list of clans less trivial clans
    print("-" * 20)

    print(p.primalClans(clansList1))
    print(p.primalClans(clansList2))
    print(p.primalClans(clansList3))
    print("-" * 20)
