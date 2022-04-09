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
:dragon: [7,000 labeled Pokemon](https://www.kaggle.com/datasets/lantian773030/pokemonclassification)

## Usage
### Generate the cleaned dataset
Run ``generate_pokemon_per_type_files.ipynb``

### Re-train the model
Run ``training_scratch.ipynb``

<p align="center"> <img src="https://github.com/ArianeDlns/DeepCV-project/blob/main/img/model.jpg" width="700" alt="Model"/>   

We used the model from [Zhang et. al 2016](https://richzhang.github.io/colorization/)

### Test the model
```bash 
mkdir references
cd references
git clone https://github.com/richzhang/colorization.git
```
Run ``color_pokemon.ipynb``

## Running the model
```bash
streamlit run pokemon_color.py
```

## Results

### Recolorization with the CNN
<p align="center"> <img src="https://github.com/ArianeDlns/DeepCV-project/blob/main/img/recol_pikachu.png" width="700" alt="Recol Pikachu"/> 

### Recolorization per type using computer vision techniques 
<p align="center"> <img src="https://github.com/ArianeDlns/DeepCV-project/blob/main/img/pikachu_pdf_l_reset.png" width="700" alt="Recol Pikachu with types"/> 


## :package: Structure
```bash
.
├── LICENSE
├── README.md
├── color_pokemon.ipynb
├── color_transfer.ipynb
├── images
│   ├── train
│   └── val
├── data
│   ├── image
│   ├── pokemon.csv
│   └── pokemon_png
├── generate_pokemon_per_type_files.ipynb
├── notebooks
│   ├── building_from_scratch.ipynb
│   ├── contours.ipynb
│   ├── generate_pokemon_per_type_files.ipynb
│   ├── pokemon_type_classifier.ipynb
│   ├── pokemon_type_fine_tuning.ipynb
│   └── pokemon_type_nemlc.ipynb
├── pokemon_color.py
├── references
│   └── colorization
├── requirements.txt
├── training_scratch.ipynb
├── transfer_learning.ipynb
├── type_classifier.py
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
[2] Richard Zhang, Phillip Isola, and Alexei A. Efros. [Colorful image colorization. CoRR, abs/1603.08511, 2016.](https://richzhang.github.io/colorization/), in ECCV, 2016.    
[3] Erik Reinhard, Michael Ashikhmin, Bruce Gooch, and Peter Shirley [Color Transfer between Images](https://www.cs.tau.ac.il/~turkel/imagepapers/ColorTransfer.pdf), IEEE Computer Graphics and Applications, 21:34–41,10 2001.    
[4] Francois Pitié, Anil C. Kokaram, Rozenn Dahyot [Automated colour grading using colour distribution transfer](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.458.7694&rep=rep1&type=pdf), Comput. Vis. Image Underst., 107:123–137, 2007.  
[5] Satoshi Iizuka, Edgar Simo-Serra, and Hi-
roshi Ishikawa. Let there be Color!: Joint End-to-end Learn-
ing of Global and Local Image Priors for Automatic Image
Colorization with Simultaneous Classification. ACM Transac-
tions on Graphics (Proc. of SIGGRAPH 2016), 35(4):110:1–
110:11, 2016.  
[6] Gustav Larsson, Michael Maire, and Gre-
gory Shakhnarovich. Learning representations for automatic
colorization. CoRR, abs/1603.06668, 2016.
[7] Georg eHan Luke Melas-Kyriazi.
Combining deep convolutional neural networks with markov
random fields for image colorization. Dec. 2018.  
[8] Richard Zhang, Jun-Yan Zhu, Phillip Isola,
Xinyang Geng, Angela S Lin, Tianhe Yu, and Alexei A Efros.
Real-time user-guided image colorization with learned deep
priors. ACM Transactions on Graphics (TOG), 9(4), 2017