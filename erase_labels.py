# Author : Iheb ALOUI
# All comments are in French
import cv2
import os
import json

class_names = [
    'background', 'BLUSH', 'BRONZER', 'CHEVEUX', 'CORPS', 'CRAYON', 
    'CREME SOLAIRE', 'GLOSS', 'HIGHLIGHTER', 'LEVRES', 'MASCARA', 'OMBRES A PAUPITRE', 
    'ONGLES', 'PALETTES', 'PARFUMS', 'POUDRE', 'PROTECTION SOLAIRE', 'ROUGE A LEVRES', 
    'ROUGE A LEVRE LIQUIDE', 'SOINS PEAU', 'SOURCILS', 'TEINT', 'VERNIS A ONGLES', 'YEUX','MANQUANT'
]

def erase_labels_coco(coco_annotation_path, images_dir, output_dir, labels_to_erase):
    # Charger les annotations COCO
    with open(coco_annotation_path, 'r') as f:
        coco_data = json.load(f)

    # Créer le dossier de sortie s'il n'existe pas
    erased_image_dir = os.path.join(output_dir, 'images')
    if not os.path.exists(erased_image_dir):
        os.makedirs(erased_image_dir)

    # Extraire les catégories et créer des dictionnaires pour accéder aux données rapidement
    categories = coco_data['categories']
    category_dict = {category['id']: category['name'] for category in categories}
    image_dict = {image['id']: image for image in coco_data['images']}
    processed_images = {}
    new_annotations = []

    # Parcourir les annotations
    for annotation in coco_data['annotations']:
        image_id = annotation['image_id']
        bbox = annotation['bbox']
        category_id = annotation['category_id']

        # Récupérer les informations de l'image
        image_info = image_dict[image_id]
        image_filename = image_info['file_name']
        image_path = os.path.join(images_dir, image_filename)

        # Charger l'image si elle n'a pas encore été traitée
        if image_id not in processed_images:
            image = cv2.imread(image_path)
            if image is None:
                print(f"Erreur : Impossible de charger {image_filename}.")
                continue
            processed_images[image_id] = image
        else:
            image = processed_images[image_id]

        # Si le label doit être supprimé, masquer l'objet
        if category_dict[category_id] in labels_to_erase:
            x_min, y_min = int(bbox[0]), int(bbox[1])
            width, height = int(bbox[2]), int(bbox[3])
            x_max, y_max = x_min + width, y_min + height

            if width > 0 and height > 0:
                x_min, y_min = max(0, x_min), max(0, y_min)
                x_max, y_max = min(image.shape[1], x_max), min(image.shape[0], y_max)
                # Dessiner un rectangle noir pour masquer l'objet
                cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 0, 0), -1)
        else:
            new_annotations.append(annotation)

    # Sauvegarder les images modifiées et non modifiées
    for image_id, image in processed_images.items():
        output_image_path = os.path.join(erased_image_dir, image_dict[image_id]['file_name'])
        cv2.imwrite(output_image_path, image)

    # Mettre à jour les annotations et sauvegarder le fichier JSON
    coco_data['annotations'] = new_annotations
    output_annotation_path = os.path.join(output_dir, 'annotations.json')
    with open(output_annotation_path, 'w') as f:
        json.dump(coco_data, f, indent=4)

    print(f"Traitement terminé. Les images annotées et non modifiées sont enregistrées dans : {output_dir}")

# Exemple d'utilisation
coco_annotation_path = 'annotations.json'
images_dir = 'images'
output_dir = 'erased_data13'
labels_to_erase = [  'YEUX','BLUSH','PALETTE','PROTECTOIN SOLAIRE','GLOSS','CORPS','CHEVEUX','BRONZER','HIGHLIGHTER','CREME SOLAIRE','ONGLES' ]
      

erase_labels_coco(coco_annotation_path, images_dir, output_dir, labels_to_erase)
