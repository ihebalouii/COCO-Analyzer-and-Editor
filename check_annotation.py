import json
import matplotlib.pyplot as plt
from collections import Counter

def load_annotations(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    return data

def extract_label_info(data):
    # Dictionnaire pour associer category_id à son nom
    category_map = {category['id']: category['name'] for category in data['categories']}
    
    labels = []
    images = set()  # Ensemble pour stocker les images uniques
    
    for annotation in data['annotations']:
        images.add(annotation['image_id'])  # Compte les images uniques
        category_id = annotation['category_id']
        labels.append(category_map[category_id])  # Associe les annotations à leurs labels respectifs
    
    # Retourne les labels annotés et le nombre d'images uniques
    return labels, len(images), category_map

def plot_annotation_stats(labels, num_images, category_map):
    # Comptage des labels avec leurs annotations
    label_counts = Counter(labels)
    
    # Inclure tous les labels, même ceux sans annotations
    for category in category_map.values():
        if category not in label_counts:
            label_counts[category] = 0
    
    # Graphique du nombre d'annotations par label
    plt.figure(figsize=(12, 6))
    bars = plt.bar(label_counts.keys(), label_counts.values(), color='skyblue')
    
    # Ajouter le nombre d'annotations au-dessus de chaque barre
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, int(yval), ha='center', va='bottom')
    
    plt.title('Nombre d\'annotations par label', fontsize=16)
    plt.xlabel('Label', fontsize=12)
    plt.ylabel('Nombre d\'annotations', fontsize=12)
    plt.xticks(rotation=45, ha="right")  # Rotation des étiquettes pour meilleure lisibilité
    plt.tight_layout()  # Ajustement pour que tout tienne dans la figure
    plt.show()
    
    # Calcul du pourcentage des annotations par label
    total_annotations = sum(label_counts.values())
    label_percentages = {label: (count / total_annotations) * 100 for label, count in label_counts.items()}
    
    # Graphique circulaire (pie chart) pour la répartition des labels
    fig, ax = plt.subplots(figsize=(8, 8))
    wedges, texts = ax.pie(label_percentages.values(), labels=label_counts.keys(), startangle=90, colors=plt.cm.Paired.colors)
    plt.title('Répartition des labels en pourcentage', fontsize=16)
    plt.axis('equal')  # Assure que le pie chart est circulaire
    
    # Affiche les pourcentages sous le graphique
    plt.figtext(0.5, 0.02, "\n".join([f"{label}: {percentage:.2f}%" for label, percentage in label_percentages.items()]), 
                ha="center", fontsize=12, bbox={"facecolor": "lightgrey", "alpha": 0.5, "pad": 5})
    
    plt.show()
    
    # Imprime le nombre total d'images et d'annotations
    print(f"Nombre total d'images : {num_images}")
    print(f"Nombre total d'annotations : {total_annotations}")

# Exemple d'utilisation
json_file = 'new_data13_final/annotations.json'  # Remplacer par le chemin du fichier d'annotations
data = load_annotations(json_file)
labels, num_images, category_map = extract_label_info(data)
plot_annotation_stats(labels, num_images, category_map)
