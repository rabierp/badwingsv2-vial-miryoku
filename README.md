# badwingsv2-vial-miryoku

Générateur de fichier de disposition [Vial](https://get.vial.today/)
implémentant la disposition [Miryoku](https://github.com/manna-harbour/miryoku)
pour le clavier ergonomique split **[Bad Wings V2](https://shop.hazel.cc/products/bad-wings-v2)**
(Hazel's Garage) — 36 touches unibody, matrice `split_3x5_3`, trackpad
Cirque intégré, firmware Vial préflashé.

Ce dépôt sert de **projet d'entraînement à Claude Code** : partir
d'un générateur simple et correct, puis l'étendre par petites
itérations (nouvelle disposition alpha, combos, tap dance, macros...)
en travaillant avec Claude Code comme pair de programmation.

## Le résultat

`output/bad_wings_v2_miryoku.vil` : un fichier prêt à importer dans
Vial, contenant 7 layers Miryoku (Base, Nav, Mouse, Media, Num, Sym,
Fun) — voir [docs/keymap.md](docs/keymap.md) pour le détail touche par
touche de chaque layer.

La couche de base utilise un QWERTY US classique (home row mods
GACS), pensé pour être utilisé avec le clavier système réglé sur
**"US International"** afin de conserver les accents français via
touches mortes. Voir la fin de [docs/keymap.md](docs/keymap.md) pour
le détail.

## Installation dans Vial

1. **Important — récupérez d'abord l'`uid` de votre carte** : dans
   Vial, `File > Download keymap` sur votre Bad Wings V2 tel qu'il
   est actuellement flashé, et notez le champ `"uid"` du fichier
   téléchargé. Ce nombre est propre à votre build de firmware ; sans
   lui, Vial peut refuser de charger un fichier généré ici.
2. Régénérez le fichier avec ce uid :
   ```
   python3 -m miryoku_vial --uid 0xVOTRE_UID -o output/bad_wings_v2_miryoku.vil
   ```
3. Dans Vial : `File > Load saved keymap`, sélectionnez le fichier
   généré.
4. Réglez le clavier du système d'exploitation sur **"United States -
   International"** (voir [docs/keymap.md](docs/keymap.md)) pour
   récupérer les accents français.

## Utilisation du générateur

Aucune dépendance externe (Python ≥ 3.10, stdlib uniquement) :

```
python3 -m miryoku_vial --uid 0x1234ABCD -o output/bad_wings_v2_miryoku.vil
```

Lancer les tests :

```
pip install pytest
python3 -m pytest
```

## Structure du dépôt

```
miryoku_vial/
  layout.py        matrice physique du Bad Wings V2 (issue de la
                    définition QMK LAYOUT_split_3x5_3, source de vérité)
  layers.py         contenu des 7 layers Miryoku (36 touches chacun)
  vial_export.py    assemble le document .vil complet
  cli.py            interface en ligne de commande
tests/              tests de la matrice et de l'export
docs/keymap.md      diagrammes des layers, doigt par doigt
output/             fichier .vil généré, prêt à importer
.github/workflows/  régénération automatique (voir ci-dessous)
```

## Régénération automatique (GitHub Actions)

Le workflow `.github/workflows/generate-vil.yml` se déclenche à
chaque modification de `miryoku_vial/**` ou `pyproject.toml` :

- il lance les tests (`pytest`) ;
- il régénère `output/bad_wings_v2_miryoku.vil` ;
- **sur un push**, si le fichier a changé, il le recommite
  automatiquement sur la même branche (commit `github-actions[bot]`,
  message `[skip ci]` pour ne pas relancer le workflow en boucle) ;
- **sur une pull request**, il échoue plutôt si le fichier committé
  est différent de celui qu'on obtiendrait en régénérant — signe
  qu'il faut relancer `python3 -m miryoku_vial` en local et committer
  le résultat avant de merger.

Le fichier régénéré en CI garde `uid=0` (valeur par défaut) : c'est
un point de départ, à re-régénérer localement avec votre propre
`--uid` avant import dans Vial (voir plus haut).

**Réglage requis une seule fois** : dans les paramètres du dépôt,
`Settings > Actions > General > Workflow permissions`, sélectionner
*"Read and write permissions"* — sinon le job ne peut pas pousser le
commit de régénération (il échouera au `git push`, la partie tests
reste néanmoins utile).

## D'où viennent les données

- La matrice physique (`miryoku_vial/layout.py`) reprend telle quelle
  la définition officielle QMK du Bad Wings V2
  (`keyboards/hazel/bad_wings/keyboard.json`, layout
  `LAYOUT_split_3x5_3`), pour être sûr de générer un fichier
  compatible avec le firmware réel.
- Le contenu des layers Nav/Mouse/Media/Num/Sym/Fun reproduit le
  comportement de référence Miryoku (thumb keys hold = layer, main
  opposée = contenu, home row de la main "libre" = modificateurs
  maintenus pour chorder).

## Pistes pour continuer avec Claude Code

Quelques exercices naturels pour la suite, à faire avec Claude Code :

- Ajouter une disposition alpha alternative (Colemak-DH, Bépo) et un
  flag CLI `--alphas` pour choisir.
- Ajouter des combos (ex: `J`+`K` → Échap) via le champ `combo` du
  `.vil`.
- Générer un rendu visuel (SVG/HTML) du clavier à partir des mêmes
  données, pour éviter de maintenir `docs/keymap.md` à la main.
- Ajouter un layer dédié aux accents français si l'astuce "US
  International" s'avère insuffisante à l'usage.
