---
nav_title: Indicateurs de messages non lus et lus
article_title: Indicateurs de messages non lus et lus de fil d’actualité pour le Web
platform: Web
page_order: 2
page_type: reference
description: "Cet article explique comment définir des indicateurs lus et non lus dans vos cartes News Feed via le SDK Braze."
channel: fil d’actualité

---

# Indicateurs de messages non lus et lus

> Cet article explique comment définir des indicateurs lus et non lus dans vos cartes News Feed via le SDK Braze.

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

Braze fournit un indicateur de messages lus et non lus sur les cartes de fil d’actualité comme indiqué sur l’image suivante :

![Une carte de fil d’actualité affichant l’image d’une montre accompagnée d’un texte. Dans le coin supérieur du texte, on trouve un triangle bleu ou gris, indiquant si une carte a été lue ou non. Un triangle bleu signifie qu’une carte a été lue.][25]

## Désactiver les indicateurs

Pour désactiver cette fonctionnalité, ajoutez le style suivant à votre CSS :

``` css
.ab-read-dot { display: none; }
.ab-read-indicator { display: none; }
```

[25]: {% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %}
