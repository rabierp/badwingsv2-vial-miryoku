# Contexte projet

Générateur Python (stdlib only) qui produit un fichier `.vil` (format
Vial) implémentant la disposition Miryoku pour le clavier **Bad Wings
V2** (36 touches, split, unibody, `LAYOUT_split_3x5_3`, trackpad
Cirque, firmware vial-qmk).

Ce dépôt est un terrain d'entraînement à Claude Code : privilégier des
itérations petites et testées plutôt que de grosses réécritures.

Seul contributeur pour l'instant : on travaille en **commits directs
sur `main`**, pas de pull request systématique. Workflow attendu pour
une modification non triviale :

1. développer et lancer les tests (`pytest`) sur une branche dédiée ;
2. une fois vert, fusionner/pousser directement sur `main` (fast-forward
   ou merge, pas de PR GitHub) ;
3. supprimer la branche (locale **et** distante) une fois fusionnée —
   ne pas laisser de branches obsolètes traîner sur le dépôt.

Pour un changement trivial (doc, un-liner déjà testé), committer
directement sur `main` sans passer par une branche est acceptable.

## Où sont les choses

- `miryoku_vial/layout.py` — la matrice physique (`KEY_POSITIONS`),
  copiée depuis la définition QMK officielle du Bad Wings V2. Ne pas
  modifier sans revérifier contre `keyboards/hazel/bad_wings/keyboard.json`
  en amont (dépôt qmk/qmk_firmware) : c'est la source de vérité pour
  le matériel.
- `miryoku_vial/layers.py` — le contenu de chaque layer, en listes de
  36 keycodes QMK/Vial (chaînes), dans l'ordre `KEY_POSITIONS`. Chaque
  layer est commenté par rangée (pinky→inner pour la main gauche,
  inner→pinky pour la main droite — attention au sens, il change
  d'une main à l'autre).
- `miryoku_vial/vial_export.py` — assemble le document `.vil` complet
  (layout + macros/tap-dance/combos vides + réglages).
- `miryoku_vial/cli.py` — CLI (`python3 -m miryoku_vial`). Ne fige
  jamais l'uid en dur : `--uid` reste obligatoire pour un vrai import,
  défaut 0.
- `config/keyboard_uid.txt` — seul fichier destiné à être édité
  directement sur GitHub (web UI) par l'utilisateur final : contient
  uniquement l'uid de sa carte (décimal ou `0x...`). Lu par le
  workflow CI, jamais par le code Python lui-même (voir invariants).
- `tests/` — vérifient la forme de la matrice et du document généré.
  Toujours garder `pytest` vert après une modification.
- `.github/workflows/generate-vil.yml` — régénère et recommite
  `output/bad_wings_v2_miryoku.vil` sur push quand `miryoku_vial/**`,
  `pyproject.toml` ou `config/keyboard_uid.txt` changent. C'est le
  chemin "sans rien installer en local" mis en avant dans le README —
  le préserver. Pas de déclencheur `pull_request` : on committe
  directement sur `main`.

## Invariants à respecter

- Chaque layer dans `layers.py` doit garder exactement 36 entrées,
  dans l'ordre `layout.KEY_POSITIONS` (assertions déjà en place, ne
  pas les retirer).
- Les cases matrice `(0,3) (1,3) (0,7) (1,7)` n'ont pas d'interrupteur
  physique sur le Bad Wings V2 : elles doivent rester `-1` dans le
  `.vil` généré (voir `build_matrix`).
- Le champ `uid` du `.vil` est spécifique au firmware compilé de
  l'utilisateur : ne jamais le figer en dur dans le code Python,
  toujours passer par `--uid` (défaut 0, avec avertissement dans le
  README). Sa valeur réelle vit uniquement dans
  `config/keyboard_uid.txt`, lu par le workflow CI — pas ailleurs.

## Commandes utiles

```
python3 -m miryoku_vial -o output/bad_wings_v2_miryoku.vil
python3 -m pytest
```

## Ce qui n'est volontairement pas géré

- Combos, tap dance, macros, key overrides : slots présents mais
  vides dans le `.vil` généré (Vial les ignore si vides). À remplir
  au cas par cas si un exercice le demande.
- Auto-mouse-layer (activation automatique du layer Mouse au contact
  du trackpad) : c'est une option de compilation firmware
  (`POINTING_DEVICE_AUTO_MOUSE_ENABLE`), pas quelque chose que ce
  générateur de `.vil` peut piloter.
