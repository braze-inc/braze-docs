---
nav_title: Indicateurs de messages non lus et lus
article_title: Indicateurs de messages non lus et lus et cartes de contenu pour Android et FireOS
page_order: 4.3
platform: 
  - Android
  - FireOS
description: "Cet article de référence couvre les indicateurs de messages non lus et lus pour Android et FireOS et la manière de les implémenter dans vos cartes de contenu."
channel:
  - cartes de contenu

---

# Indicateurs de messages non lus et lus {#read-indicators-for-android}

> Cet article de référence explique comment activer facultativement les indicateurs non lus et lus sur les cartes de contenu.

![Deux cartes de contenu affichées côte à côte. La première carte a une ligne bleue en bas, indiquant qu’elle n’a pas été vue. La deuxième carte n’a pas de ligne bleue, indiquant qu’elle a déjà été vue.][1]

## Personnaliser les indicateurs {#customizing-the-indicators-for-android}
La couleur de ces indicateurs peut être personnalisée en modifiant les valeurs dans `com_braze_content_cards_unread_bar_color` de votre fichier `colors.xml` :

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <!-- The color used to highlight unread Content Cards at their bottom edge -->
  <color name="com_braze_content_cards_unread_bar_color">#1676d0</color>
</resources>
```

[1]: {% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %}
