# DeepCV-project
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) 
[![Open in Visual Studio Code](https://img.shields.io/badge/Editor-VSCode-blue?style=flat-square&logo=visual-studio-code&logoColor=white)](https://github.dev/ArianeDlns/DeepCV-project/tree/main) [![GitHub commit](https://badgen.net/github/last-commit/ArianeDlns/chatbot-presidentielle2022/main)](https://GitHub.com/ArianeDlns/DeepCV-project/issues/) [![Report](https://img.shields.io/badge/Report-1.0-green?style=square&logo=overleaf&logoColor=white)](https://fr.overleaf.com/project/61aa186569ec83f4fb2a78b0)

Project for the Deep Learning &amp; Computer Vision course @CentraleSupélec 

## Installation
### Download the dataset and requirements 

```bash
$ pip install -r requirements.txt
```

:dragon: [pokemon-images-and-types](https://www.kaggle.com/datasets/vishalsubbiah/pokemon-images-and-types)

## Usage
### Generate the cleaned dataset
``generate_pokemon_per_type_files.ipynb``

### re-train the model
```bash
.
```

### Test the model
```bash
.
```

## Running the model
```bash
streamlit run pokemon_color.py
```

## :package: Structure
```bash
.
├── LICENSE
├── README.md
├── color_transfer.ipynb
├── data
│   ├── image
│   ├── pokemon.csv
│   └── pokemon_png
├── generate_pokemon_per_type_files.ipynb
├── notebooks
│   ├── contours.ipynb
│   ├── exploratory_analysis.ipynb
│   ├── pokemon_type_classifier.ipynb
│   └── pokemon_type_fine_tuning.ipynb
├── references
│   └── colorization
└── utils.py
```

## :world_map: Roadmap

- Etape 1 : A partir des images de pokemon récupérées, établir un script de détection des contours pour avoir des images à colorier. 

- Etape 2 : effectuer une analyse des couleurs présentes dans les images en fonction des types de pokemon (surement un passage de l'image en Lab et étude de l'espace a,b en fonction du type)

- Etape 3 : Réaliser un classifieur qui étant donné un pokemon en entrée te rend le type du pokemon (un CNN classique devrait le faire ? voir peut être des ressources sur Kaggle). Ce classifieur nous servira plus tard pour voir si les coloriages effectués sont "bien fait ou non" 

- Etape 4 : Réaliser un réseau pour colorier les pokemons en fonction d'un type ou de deux types donnés


## License
[![MIT](https://img.shields.io/badge/License-MIT-blue?style=square&logo=MIT&logoColor=white)](https://github.com/ArianeDlns/DeepCV-project/blob/main/LICENSE)

## Report
[![Report](https://img.shields.io/badge/Report-1.0-green?style=square&logo=overleaf&logoColor=white)](https://fr.overleaf.com/project/61aa186569ec83f4fb2a78b0)

## References
[1] Guillaume Charpiat, Ilja Bezrukov, Yasemin Altun, Matthias Hofmann and Bernhard Schölkopf, [Machine Learning Methods for Automatic Image Colorization](https://www.lri.fr/~gcharpia/publis_en_images/colorisation/) , chapter of the book Computational Photography: Methods and Applications, R. Lukac Editor, CRC Press.  
[2] Richard Zhang, Phillip Isola, and Alexei A. Efros. [Colorful image colorization. CoRR, abs/1603.08511, 2016.](https://richzhang.github.io/colorization/)  
[3] Erik Reinhard, Michael Ashikhmin, Bruce Gooch, and Peter Shirley [Color Transferbetween Images](https://www.cs.tau.ac.il/~turkel/imagepapers/ColorTransfer.pdf)  
[4] Francois Pitié, Anil C. Kokaram, Rozenn Dahyot [Automated colour grading using colour distribution transfer](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.458.7694&rep=rep1&type=pdf)  