import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(G, distances, current_vertex=None, path=None):
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
    
    if current_vertex is not None:
        nx.draw_networkx_nodes(G, pos, nodelist=[current_vertex], node_color='red', node_size=700)
    
    if path is not None:
        nx.draw_networkx_edges(G, pos, edgelist=path, edge_color='blue', width=2)
    
    plt.show()

def Deikstra(G, start):
    
    distances = {node: float('infinity') for node in G.nodes()}
    distances[start] = 0
    
    unvisited = set(G.nodes())
    
    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        unvisited.remove(current_vertex)
        
        if distances[current_vertex] == float('infinity'):
            break
        
        for neighbor, data in G[current_vertex].items():
            alternative_route = distances[current_vertex] + data['weight']
            
            if alternative_route < distances[neighbor]:
                distances[neighbor] = alternative_route
                
        draw_graph(G, distances, current_vertex=current_vertex)


G = nx.Graph()
G.add_edge(0, 1, weight=1)
G.add_edge(0, 2, weight=3)
G.add_edge(1, 2, weight=1)
G.add_edge(1, 3, weight=1)
G.add_edge(2, 3, weight=1)
G.add_edge(2, 4, weight=1)
G.add_edge(3, 4, weight=1)

Deikstra(G, 0)



#Я с этим визуализатором 4 часа бодался. ради всего святого и моих мучений - примите эту штуку. я честно выдал максимум (улыбчивый смайлик со слезами на глазах)