---
nav_title: Indicateurs de messages non lus et lus
article_title: "Indicateurs de messages non lus et lus de fil d'actualité pour Android et FireOS"
page_order: 3.1
platform: 
  - Android
  - FireOS
description: "Cet article de référence couvre les indicateurs de messages non lus et lus de fil d'actualité dans votre application Android ou FireOS."
channel:
  - news feed
  
---

# Indicateurs de messages non lus et lus

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

> Braze vous permet de basculer entre les indicateurs de messages lus et non lus sur les cartes de fil d'actualité.

![Une carte de fil d’actualité affichant l’image d’une montre accompagnée d’un texte. Dans le coin supérieur du texte, un triangle bleu ou gris indique si une carte a été lue ou non. Un triangle bleu indique qu'une carte a été lue.]({% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %})

## Activer les indicateurs

Pour activer cette fonctionnalité, ajoutez la ligne suivante à votre fichier `braze.xml` :

```xml
<bool name="com_braze_newsfeed_unread_visual_indicator_on">true</bool>
```

## Personnaliser les indicateurs

Ces indicateurs peuvent être personnalisés en modifiant les images `icon_read` et `icon_unread`.

