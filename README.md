# DeepCV-project
Project for the Deep Learning &amp; Computer Vision course @CentraleSupélec 

## Installation
### Dataset

:dragon: [Pokémon](https://www.kaggle.com/datasets/vishalsubbiah/pokemon-images-and-types)


## Structure
```bash
.
```

## Roadmap

- Etape 1 : A partir des images de pokemon récupérées, établir un script de détection des contours pour avoir des images à colorier. 

- Etape 2 : effectuer une analyse des couleurs présentes dans les images en fonction des types de pokemon (surement un passage de l'image en Lab et étude de l'espace a,b en fonction du type)

- Etape 3 : Réaliser un classifieur qui étant donné un pokemon en entrée te rend le type du pokemon (un CNN classique devrait le faire ? voir peut être des ressources sur Kaggle). Ce classifieur nous servira plus tard pour voir si les coloriages effectués sont "bien fait ou non" 

- Etape 4 : Réaliser un réseau pour colorier les pokemons en fonction d'un type ou de deux types donnés


## License
[MIT](https://github.com/ArianeDlns/DeepCV-project/blob/main/LICENSE)

## References
[1] Guillaume Charpiat, Ilja Bezrukov, Yasemin Altun, Matthias Hofmann and Bernhard Schölkopf, [Machine Learning Methods for Automatic Image Colorization](https://www.lri.fr/~gcharpia/publis_en_images/colorisation/) , chapter of the book Computational Photography: Methods and Applications, R. Lukac Editor, CRC Press.  
[2] Richard Zhang, Phillip Isola, and Alexei A. Efros. [Colorful image colorization. CoRR, abs/1603.08511, 2016.](https://richzhang.github.io/colorization/)