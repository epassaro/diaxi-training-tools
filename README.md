# diaxi-training-tools

Herramientas para la creación del dataset y el entrenamiento del modelo de Desafío IA por la Identidad

## Instalación

> Requiere tener instalado [**Miniconda**](https://docs.conda.io/en/latest/miniconda.html) o una variante de [**Miniforge**](https://github.com/conda-forge/miniforge/releases/latest) (se recomienda `mambaforge`).

```
$ conda env create -f environment.yml
$ conda activate diaxi-training-tools
```

## Herramientas

### Jupyter Notebooks
- `create_diaxi_dataset.ipynb`

  > En esta notebook se explica paso a paso cómo se creo el dataset final en formato COCO y los problemas que fuimos solucionando en el camino.

- `create_detectron2_model.ipynb` [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1pnmmeUib-3sAUGxYIjcz-Vh4zT9xnQzi?usp=sharing)

  > En esta notebook se explica cómo entrenamos el modelo de segmentación que luego implementamos en el software. Está originalmente pensada para correr en Google Colab ya que no contábamos con una GPU.

### Scripts

-  `bbox2mask.py`

    > Este script crea máscaras de segmentación rectangulares para *datasets* en formato COCO que solamente contienen *bounding boxes*.

- `catfilter.py`

  > Este script permite descartar las etiquetas que no queremos utilizar en el modelo.

- `imgidfix.py`

  > Este script mapea las IDs de las imágenes entre `0..N`. Es necesario para *mergear* datasets con `pyodi`.
