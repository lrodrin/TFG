import networkx as nx
import src.clans as c
import src.iter_subsets as it
import src.primalClans as p

__author__ = "\"Laura Rodriguez Navas <laura.rodriguez.navas@upc.edu>"""

if __name__ == "__main__":

    G = nx.Graph()  # Create an empty graph structure (a “null graph”) with no nodes and no edges

    # Adding edges and edges attributes
    G.add_edges_from([('A', 'B'), ('B', 'D'), ('B', 'E'), ('D', 'E')], color='red')
    G.add_edges_from([('A', 'C'), ('B', 'C'), ('C', 'D'), ('C', 'E')], color='black')
    G.add_edges_from([('A', 'D'), ('A', 'E')], color='blue')

    subsetNodes = set(G.nodes())  # Subset of nodes from G

    subset_isTrue = {'D', 'E'}  # Subset that belongs to G
    subset_isFalse = {'A', 'B'}  # Subset that not belongs to G
    print(c.isAClan(G, subset_isTrue))
    print(c.isAClan(G, subset_isFalse))
    print("-" * 20)

    clansList = []
    for s in it.all_subsets(subsetNodes):  # Subset iterator of each subsetNodes
        if c.isAClan(G, s):  # If s is a clan of G
            clansList.append(s)  # Add s to the list
    print(sorted(clansList))  # Complete list of clans
    print("-" * 20)

    clansList = []
    for s in it.powerset_generator(subsetNodes):  # Subset iterator of each subsetNodes
        if c.isAClan(G, s):  # If s is a clan of G
            clansList.append(s)  # Add s to the list
    print(sorted(clansList))  # Complete list of clans
    print("-" * 20)

    clansList = []
    for s in it.all_subsets(subsetNodes):  # Subset iterator of each subsetNodes
        if c.isAClan(G, s) and not c.isATrivialClan(s):  # If s is a clan of G and isn't a trivial clan
            clansList.append(s)  # Add s to the list
    print(sorted(clansList))  # Complete list of clans less trivial clans
    print("-" * 20)

    clansList = []
    for s in it.powerset_generator(subsetNodes):  # Subset iterator of each subsetNodes
        if c.isAClan(G, s) and len(s) > 1:  # If s is a clan of G and isn't a trivial clan
            clansList.append(s)  # Add s to the list
    print(sorted(clansList))  # Complete list of clans less trivial clans
    print("-" * 20)

    print(p.primalClans(clansList))
    print("-" * 20)