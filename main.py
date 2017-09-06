#!/usr/bin/python

import csv
import config
import networkx as nx
import matplotlib.pyplot as plt


G=nx.Graph()
with open(config.csvfile, newline='') as dataset:
	alldata = csv.reader(dataset, delimiter=',',quotechar="|")
	for row in alldata:
		G.add_edge(row[0],row[1],weight=float(row[5]))
		#print(row[0],row[1],int(row[5]))

satu=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >=1]
kosong=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0]
dua=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >=2]
tiga=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >=3]

pos=nx.spring_layout(G)
# nodes
nx.draw_networkx_nodes(G,pos,node_size=100)
# edges

nx.draw_networkx_edges(G,pos,edgelist=kosong,
                    width=0.01,alpha=0.5,edge_color='b',style='dashed')
nx.draw_networkx_edges(G,pos,edgelist=satu,
                    width=1)
nx.draw_networkx_edges(G,pos,edgelist=dua,
					width=2)
nx.draw_networkx_edges(G,pos,edgelist=tiga,
					width=3)


# labels
nx.draw_networkx_labels(G,pos,font_size=9,font_family='sans-serif')

with open('dc.csv', 'w', newline='') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for x,y in nx.degree_centrality(G).items():
		spamwriter.writerow([x, y])

with open('cc.csv', 'w', newline='') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for x,y in nx.closeness_centrality(G).items():
		spamwriter.writerow([x, y])
		
with open('bc.csv', 'w', newline='') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for x,y in nx.betweenness_centrality(G).items():
		spamwriter.writerow([x, y])




plt.axis('off')
plt.savefig("graph.png")
