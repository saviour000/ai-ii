import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# --- Prolog Facts as Semantic Net ---

# Family relationships
relations = [
    ("john", "mary", "parent"),
    ("john", "steve", "parent"),
    ("mary", "alice", "parent"),
    ("mary", "bob", "parent"),
    ("alice", "carol", "parent"),
    ("alice", "david", "parent"),
    ("bob", "emily", "parent"),
    ("bob", "frank", "parent"),
]

# Genders
genders = [
    ("john", "male", "is-a"),
    ("steve", "male", "is-a"),
    ("bob", "male", "is-a"),
    ("carol", "male", "is-a"),
    ("david", "male", "is-a"),
    ("frank", "male", "is-a"),
    ("mary", "female", "is-a"),
    ("alice", "female", "is-a"),
    ("emily", "female", "is-a"),
]

# Add nodes & edges
for subj, obj, rel in relations + genders:
    G.add_edge(subj.capitalize(), obj.capitalize(), label=rel)

# Layout
pos = nx.spring_layout(G, k=0.8, seed=42)

# Draw graph
plt.figure(figsize=(10, 7))
nx.draw(
    G, pos,
    with_labels=True,
    node_size=3000,
    node_color="lightblue",
    font_size=9,
    font_weight="bold",
    arrowsize=15
)

# Edge labels
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red", font_size=9)

# Show Semantic Net
plt.title("Semantic Net from Prolog Knowledge Base", fontsize=12, fontweight="bold")
plt.show()
