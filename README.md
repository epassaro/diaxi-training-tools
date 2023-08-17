# diaxi-training-tools

Herramientas desarrolladas en el marco del [desafío _"IA por la Identidad"_](https://desafio-ia-por-la-identidad.fundacionsadosky.org.ar/) organizado por la Fundación Sadosky, el Ministerio de Ciencia, Tecnología e Innovación y Abuelas de Plaza de Mayo (🥈 2do Lugar)

**Integrantes:** _Agostina Filócomo_ ([agostinaf](https://github.com/agostinaf)), _Adolfo Simaz Bunzel_ ([asimazbunzel](https://github.com/asimazbunzel)), _Ezequiel Pássaro_ ([epassaro](https://github.com/epassaro))

## Instalación

> Requiere una instalación de [**Miniconda**](https://docs.conda.io/en/latest/miniconda.html) o alguna variante de [**Miniforge**](https://github.com/conda-forge/miniforge/releases/latest).

```
$ conda env create -f environment.yml
$ conda activate diaxi-training-tools
```

## Herramientas
- `create_detectron2_model.ipynb` [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1pnmmeUib-3sAUGxYIjcz-Vh4zT9xnQzi?usp=sharing)

  > En esta notebook se explica cómo entrenamos el modelo de segmentación que luego implementamos en el software. Fue pensada para ejecutarse en Google Colab ya que no contábamos con una GPU.

- `create_diaxi_dataset.ipynb`

  > En esta notebook se detalla paso a paso cómo se creó el dataset en formato COCO y los problemas que fuimos solucionando en el camino.

-  `bbox2mask.py`

    > Este script crea máscaras de segmentación rectangulares para datasets en formato COCO que solamente contienen *bounding boxes*.

- `catfilter.py`

  > Este script permite descartar las etiquetas que no queremos utilizar para entrenar el modelo.

- `imgidfix.py`

  > Este script mapea las IDs de las imágenes entre `0..N`. Es necesario para fusionar datasets con `pyodi`.

## Modelo
El modelo entrenado y el archivo de configuración puede descargarse [desde acá](https://github.com/epassaro/diaxi-training-tools/releases).

## Prensa
- Argentina.gob.ar - [_Se entregaron los premios a los ganadores del desafío “Inteligencia Artificial por la Identidad”_](https://www.argentina.gob.ar/noticias/se-entregaron-los-premios-los-ganadores-del-desafio-inteligencia-artificial-por-la)
- Abuelas.org.ar - [_"Estamos orgullosos de que la IA se pueda aplicar a causas tan importantes"_](https://www.abuelas.org.ar/noticia/estamos-orgullosos-de-que-la-ia-se-pueda-aplicar-a-causas-tan-importantes-1811)
- Infobae - [_Ya cualquier persona en el mundo puede consultar el archivo periodístico de Abuelas de Plaza de Mayo_](https://www.infobae.com/educacion/2023/08/10/ya-cualquier-persona-en-el-mundo-puede-consultar-el-archivo-periodistico-de-abuelas-de-plaza-de-mayo/)