---
nav_title: Lecture & Indicateurs non lus
article_title: Carte de contenu lue & Indicateurs non lus pour Android/FireOS
page_order: 3
platform:
  - Android
  - Pare-feu
description: "Cet article de référence couvre les indicateurs Android lus et non lus et comment les implémenter dans vos Cartes de Contenu."
channel:
  - cartes de contenu
---

# Indicateurs lus et non lus {#read-indicators-for-android}

Braze vous permet d'activer optionnellement un indicateur non lu/lu sur les cartes de contenu.

!\[Read & Unread Indicators\]\[1\]

## Personnalisation des indicateurs {#customizing-the-indicators-for-android}
La couleur de ces indicateurs peut être personnalisée en modifiant les valeurs dans `com_braze_content_cards_unread_bar_color` dans votre fichier `colors.xml`.

```xml
<?xml version="1. " encoding="utf-8"?>
<resources>
  <! - La couleur utilisée pour mettre en évidence les Cartes de Contenu non lues à leur bord inférieur -->
  <color name="com_braze_content_cards_unread_bar_color">#1676d0</color>
</resources>
```
[1]: {% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %}
