import pandas as pd
import networkx as nx
import ast
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
import json

filePath = '~/Data/ml_15year.csv'
df = pd.read_csv(filepath_or_buffer=filePath, usecols=['id', 'authors'])
authorList = df[1:]['authors']
print authorList

G = nx.Graph()
list = []
for authorString in authorList:
    authors = ast.literal_eval(authorString)
    if len(authors) == 1:
        G.add_node(authors[0])
    else:
        for i, author in enumerate(authors):
            for x in authors[i+1:]:
                list.append((author, x))
        G.add_edges_from(list)

print len(G.nodes())
print len(G.edges())

degree_hist = nx.degree_histogram(G)


x = range(len(degree_hist))
y = [i / float(sum(degree_hist)) for i in degree_hist]

plt.plot(x, y, color='blue', linewidth=2, marker='o')
plt.title('Degree Distribution(loglog, 15 years)')
plt.ylabel('Probability')
plt.xlabel('Degree')
plt.show()

data = json_graph.adjacency_data(G)
with open('/home/ASUAD/kding9/Data/graph_15.json', 'w') as file:
    json.dump(data, file)
file.close()

