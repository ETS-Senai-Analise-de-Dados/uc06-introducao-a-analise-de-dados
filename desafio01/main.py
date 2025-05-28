import re
import networkx as nx
import matplotlib.pyplot as plt
import os.path

# Implemente a função que recebe uma string chamada page_content
# que é uma página html da wikipedia. Você deve procurar todos
# href="/wiki/pagina/" do texto e retornar uma lista com apenas
# os nomes das páginas como [ "Bosch_(company)", "Spark_plug" ].
def extract_wikipedia_links(page_content):
    links = []
        
    return links

def get_file_path(url):
    file = url[1:] + ".html"
    if not os.path.isfile(file):
        return None
    return file

def get_wikipedia_page(url):
    path = get_file_path(url)
    if path is None:
        return None

    with open(path, 'r', encoding="utf-8") as file:
        return file.read()

# Existe um bug neste código. Você precisa verificar se a current_url
# já foi visitada. Use a sintaxe 'current_url in visited_pages' para
# descobrir isso. Além disso, você precisa adicionar o current_url no
# visited_pages para indicar que ela já foi visitada usando a sintaxe
# 'visited_pages.add(current_url)' para isso. Sem isso as páginas são
# acessadas infinitamente e o código nunca termina de rodar.
def create_wikipedia_graph(start_url):
    G = nx.Graph()
    pages_to_visit = [ start_url ]
    visited_pages = set()

    while pages_to_visit:
        current_url = pages_to_visit.pop(0)
        
        # Falta algo aqui...

        print("visiting", current_url)
        
        page_content = get_wikipedia_page(current_url)
        if page_content is None:
            continue
        
        links = extract_wikipedia_links(page_content)
        G.add_node(current_url[6:])
        
        for link in links:
            if get_file_path(f'/wiki/{link}') is None:
                continue
                
            if current_url[6:] == link:
                continue
            
            G.add_edge(current_url[6:], link)
            pages_to_visit.append(f'/wiki/{link}')
    
    return G

def visualize_graph(G):
    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=1000, node_color='lightblue')
    nx.draw_networkx_edges(G, pos, arrowstyle='-', arrowsize=20, arrows=True)
    nx.draw_networkx_labels(G, pos, font_size=12, font_color='black')

    plt.show()

start_url = '/wiki/Bosch_(company)'
G = create_wikipedia_graph(start_url)
visualize_graph(G)