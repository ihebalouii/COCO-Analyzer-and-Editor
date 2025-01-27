# COCO Tools for Dataset Analysis and Modification

## Description
This repository contains two Python scripts for working with COCO-format datasets:

1. **`check_annotation.py`**: Analyzes COCO annotations to visualize label distributions and extract useful statistics about annotations and images.
2. **`erase_labels.py`**: Removes specific annotations and modifies associated images by masking objects corresponding to chosen labels.

These tools are particularly useful for preparing and managing datasets for computer vision projects.

---

## Features

### 1. Annotation Analysis with `check_annotation.py`
- Loads COCO annotations.
- Visualizes statistics:
  - Histogram of the number of annotations per label.
  - Pie chart of label distribution in percentages.
- Extracts key information such as the total number of images and annotations.

### 2. Label Removal with `erase_labels.py`
- Masks annotated objects corresponding to specific labels.
- Updates JSON files to remove associated annotations.
- Outputs modified images in a specified directory.

---

## Repository Structure

```
.
├── scripts/
│   ├── check_annotation.py   # Annotation analysis
│   ├── erase_labels.py       # Label removal
│
├── examples/
│   ├── input_dataset/
│   │   ├── annotations.json  # Example COCO annotations
│   │   ├── images/           # Associated images
│   ├── output_dataset/       # Results produced by the scripts
│   │   ├── annotations.json
│   │   ├── images/
│
├── README.md                 # Project documentation
└── requirements.txt          # Python dependencies
```

---

## Prerequisites

### Requirements
- **Python 3.x**
- Python Libraries:
  - `opencv-python`
  - `matplotlib`
  - `json`
  - `collections`

### Installing Dependencies
Install the required dependencies using:
```bash
pip install -r requirements.txt
```

---

## Usage Guide

### Annotation Analysis with `check_annotation.py`

#### Running the script:
```bash
python scripts/check_annotation.py --json_file path/to/annotations.json
```

#### Results:
- Histogram showing the number of annotations per label.
- Pie chart illustrating the percentage distribution of labels.
- Total number of images and annotations displayed in the console.

### Label Removal with `erase_labels.py`

#### Running the script:
```bash
python scripts/erase_labels.py \
    --coco_annotation_path path/to/annotations.json \
    --images_dir path/to/images \
    --output_dir path/to/output \
    --labels_to_erase "LABEL1,LABEL2,..."
```

#### Arguments:
- `--coco_annotation_path`: Path to the JSON file containing annotations.
- `--images_dir`: Directory containing the dataset images.
- `--output_dir`: Directory where modified images and updated JSON file will be saved.
- `--labels_to_erase`: List of labels to remove (comma-separated).

#### Results:
- Images with objects corresponding to removed labels are modified (objects are masked with black rectangles).
- A new JSON file is generated without the annotations associated with the removed labels.

---

## Examples
### Plots for Dataset Analyses 
![Plots](https://imgur.com/oS8ZF8N.png)
### Before/After Label Removal
- Input Example:
  - JSON annotations containing categories such as `EYES`, `BLUSH`, etc.
  - Associated images with annotated objects.
- Output Example:
  - Images with objects corresponding to removed labels masked.
  - Updated JSON file with cleaned annotations.

---

## Contributions
Contributions are welcome! If you have suggestions, corrections, or features to add, feel free to open an **issue** or submit a **pull request**.

---

## Author
- **Iheb Aloui**

---

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute it.