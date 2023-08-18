# diaxi-training-tools

Herramientas desarrolladas en el marco del [desafío _"IA por la Identidad"_](https://desafio-ia-por-la-identidad.fundacionsadosky.org.ar/) organizado por la Fundación Sadosky, el Ministerio de Ciencia, Tecnología e Innovación y Abuelas de Plaza de Mayo (🥈 2do Lugar)

[Solicitar acceso al repositorio principal](https://github.com/epassaro/diaxi-training-tools/issues/3) | [Descargar el modelo y dataset]() | [Integrantes del equipo](https://github.com/epassaro/diaxi-training-tools/blob/main/EQUIPO.md) | [Notas de prensa](https://github.com/epassaro/diaxi-training-tools/blob/main/PRENSA.md)

## Instalación

> Requiere una instalación de [**Miniconda**](https://docs.conda.io/en/latest/miniconda.html) o alguna variante de [**Miniforge**](https://github.com/conda-forge/miniforge/releases/latest).

```
$ conda env create -f environment.yml
$ conda activate diaxi-training-tools
```

## Herramientas
- `notebooks/create_detectron2_model.ipynb` [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1pnmmeUib-3sAUGxYIjcz-Vh4zT9xnQzi?usp=sharing)

  > En esta notebook se explica cómo entrenamos el modelo de segmentación que luego implementamos en el software. Fue pensada para ejecutarse en Google Colab ya que no contábamos con una GPU.

- `notebooks/create_diaxi_dataset.ipynb`

  > En esta notebook se detalla paso a paso cómo se creó el dataset en formato COCO y los problemas que fuimos solucionando en el camino.

-  `scripts/bbox2mask.py`

    > Este script crea máscaras de segmentación rectangulares para datasets en formato COCO que solamente contienen *bounding boxes*.

- `scripts/catfilter.py`

  > Este script permite descartar las etiquetas que no queremos utilizar para entrenar el modelo.

- `scripts/imgidfix.py`

  > Este script mapea las IDs de las imágenes entre `0..N`. Es necesario para fusionar datasets con `pyodi`.
  