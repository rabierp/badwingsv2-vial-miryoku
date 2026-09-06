# Contexte projet

Générateur Python (stdlib only) qui produit un fichier `.vil` (format
Vial) implémentant la disposition Miryoku pour le clavier **Bad Wings
V2** (36 touches, split, unibody, `LAYOUT_split_3x5_3`, trackpad
Cirque, firmware vial-qmk).

Ce dépôt est un terrain d'entraînement à Claude Code : privilégier des
itérations petites et testées plutôt que de grosses réécritures.

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
- `miryoku_vial/cli.py` — CLI (`python3 -m miryoku_vial`).
- `tests/` — vérifient la forme de la matrice et du document généré.
  Toujours garder `pytest` vert après une modification.

## Invariants à respecter

- Chaque layer dans `layers.py` doit garder exactement 36 entrées,
  dans l'ordre `layout.KEY_POSITIONS` (assertions déjà en place, ne
  pas les retirer).
- Les cases matrice `(0,3) (1,3) (0,7) (1,7)` n'ont pas d'interrupteur
  physique sur le Bad Wings V2 : elles doivent rester `-1` dans le
  `.vil` généré (voir `build_matrix`).
- Le champ `uid` du `.vil` est spécifique au firmware compilé de
  l'utilisateur : ne jamais le figer en dur, toujours passer par
  `--uid` (défaut 0, avec avertissement dans le README).

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
