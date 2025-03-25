---
nav_title: Indicateurs de messages non lus et lus
article_title: Indicateurs de messages non lus et lus de fil d’actualité pour le Web
platform: Web
page_order: 2
page_type: reference
description: "Cet article explique comment définir des indicateurs lus et non lus dans vos cartes News Feed via le SDK Braze."
channel: news feed

---

# Indicateurs de messages non lus et lus

> Cet article explique comment définir des indicateurs lus et non lus dans vos cartes News Feed via le SDK Braze.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Braze fournit un indicateur de messages lus et non lus sur les cartes de fil d’actualité comme indiqué sur l’image suivante :

![Une carte de fil d’actualité affichant l’image d’une montre accompagnée d’un texte. Dans le coin supérieur du texte, un triangle bleu ou gris indique si une carte a été lue ou non. Un triangle bleu indique qu'une carte a été lue.]({% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %})

## Désactiver les indicateurs

Pour désactiver cette fonctionnalité, ajoutez le style suivant à votre CSS :

``` css
.ab-read-dot { display: none; }
.ab-read-indicator { display: none; }
```

