# Disposition des touches

Disposition Miryoku (base QWERTY / US International) générée pour le
Bad Wings V2. Les diagrammes ci-dessous représentent les 36 touches
physiques, main gauche à gauche, main droite à droite, pouces en bas
de chaque bloc.

`GUI/ALT/CTL/SFT` = home row mods : la touche envoie la lettre en tap,
le modificateur en hold. `LT(n)` = tap la touche indiquée, hold active
le layer `n`.

## Layer 0 — Base

```
Q     W     E     R     T           Y     U     I     O     P
A/GUI S/ALT D/CTL F/SFT G           H     J/SFT K/CTL L/ALT ;/GUI
Z     X     C     V     B           N     M     ,     .     /
            Esc   Spc   Tab         Del   Bspc  Ent
           (Media)(Nav)(Mouse)     (Fun) (Num) (Sym)
```

## Layer 1 — Nav (pouce gauche : Espace maintenu)

```
·     ·     ·     ·     ·          Undo  Cut   Copy  Paste Again
GUI   ALT   CTL   SFT   ·          Right Up    Down  Left  CapsLock
·     ·     ·     ·     ·          End   PgUp  PgDn  Home  Insert
            ·     ·     ·          Del   Bspc  Enter
```

## Layer 2 — Mouse (pouce gauche : Tab maintenu)

```
·     ·     ·     ·     ·          Undo  Cut   Copy  Paste Again
GUI   ALT   CTL   SFT   ·          MS→   MS↑   MS↓   MS←   ·
·     ·     ·     ·     ·          Wh→   Wh↑   Wh↓   Wh←   ·
            ·     ·     ·          Btn3  Btn1  Btn2
```

Le trackpad Cirque du Bad Wings V2 pilote directement le curseur ;
ce layer sert surtout aux clics (Btn1/2/3) pendant que le pouce
gauche maintient Tab.

## Layer 3 — Media (pouce gauche : Échap maintenu)

```
·     ·     ·     ·     ·          ·     ·     ·     ·     ·
GUI   ALT   CTL   SFT   ·          ·     Prev  VolDn VolUp Next
·     ·     ·     ·     ·          ·     ·     ·     ·     ·
            ·     ·     ·          Mute  Play  Stop
```

## Layer 4 — Num (pouce droit : Retour arrière maintenu)

```
[     7     8     9     ]          ·     ·     ·     ·     ·
;     4     5     6     =          ·     SFT   CTL   ALT   GUI
`     1     2     3     \          ·     ·     ·     ·     ·
            .     0     -          ·     ·     ·
```

## Layer 5 — Sym (pouce droit : Entrée maintenue)

```
{     &     *     (     }          ·     ·     ·     ·     ·
:     $     %     ^     +          ·     SFT   CTL   ALT   GUI
~     !     @     #     |          ·     ·     ·     ·     ·
            (     )     _          ·     ·     ·
```

## Layer 6 — Fun (pouce droit : Suppr maintenue)

```
F12   F7    F8    F9    PrtSc      ·     ·     ·     ·     ·
F11   F4    F5    F6    ScrLk      ·     SFT   CTL   ALT   GUI
F10   F1    F2    F3    Pause      ·     ·     ·     ·     ·
            ·     Spc   Tab        ·     ·     ·
```

## Pourquoi US International ?

La disposition alpha est un QWERTY US "brut" (touches physiques dans
l'ordre standard `QWERTY`). C'est fait pour être utilisé avec le
réglage clavier du système d'exploitation sur **"United States -
International"**, qui ajoute des touches mortes sur `' " ~ ^ \``
pour taper les caractères accentués français (`é è à ç ê ...`) sans
toucher à la disposition physique du firmware. Le mapping du firmware
(ce dépôt) n'a pas besoin de connaître cette couche : c'est purement
un réglage système, à activer côté OS.

Pour changer d'alphas (Colemak-DH, Dvorak, Bépo...), voir
`miryoku_vial/layers.py::BASE_QWERTY_US_INTL` — chaque position est
commentée avec son doigt (pinky/ring/middle/index/inner).
