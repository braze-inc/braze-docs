---
nav_title: Lecture & Indicateurs non lus
article_title: Flux d'actualités Lire & Indicateurs non lus pour Android/FireOS
page_order: 4
platform:
  - Android
  - Pare-feu
description: "Cet article de référence couvre la façon d'implémenter des indicateurs de lecture et de lecture dans votre flux d'actualités pour votre application Android."
channel:
  - fil d'actualité
---

# Indicateurs lus et non lus

Braze vous permet d'activer optionnellement un indicateur non lu/lu sur les cartes de flux d'actualités comme illustré ci-dessous :

!\[UnreadvsRead\]\[25\]

## Activation des indicateurs

Afin d'activer cette fonctionnalité, ajoutez la ligne suivante à votre fichier `braze.xml`:

```xml
<bool name="com_braze_newsfeed_unread_visual_indicator_on">vrai</bool>
```

## Personnalisation des indicateurs
Ces indicateurs peuvent être personnalisés en modifiant les tiroirs "icon_read" et "icon_unread".
[25]: {% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %}
