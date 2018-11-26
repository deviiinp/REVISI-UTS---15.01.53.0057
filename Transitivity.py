import networkx as nx 
import matplotlib.pyplot as plt

G=nx.DiGraph() 

G.add_edge('UU Nomor 22 Tahun 2001','UUD 1945') 
G.add_edge('UU Nomor 22 Tahun 2001','Ketetapan MPR Nomor XV/MPR/1998')
G.add_edge('UU Nomor 39 Tahun 2007','UUD 1945')
G.add_edge('UU Nomor 39 Tahun 2007','UUD 1945')
G.add_edge('UU Nomor 1 Tahun 2017','UU Nomor 24 Tahun 2000')
G.add_edge('UU Nomor 18 Tahun 2017','UUD 1945') 
G.add_edge('UU Nomor 18 Tahun 2017','UU Nomor 13 Tahun 2003')
G.add_edge('UU Nomor 18 Tahun 2017','UU Nomor 6 Tahun 2012')
G.add_edge('UU Nomor 2 Tahun 2018',' UUD 1945')
G.add_edge('UU Nomor 2 Tahun 2018 ','UU Nomor 17 Tahun 2014') 

nx.draw_networkx(G)
plt.axis('off')
plt.show()

#transivity
print(nx.transitivity(G))
