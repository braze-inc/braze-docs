---
nav_title: Indicateurs de messages non lus et lus
article_title: Indicateurs de messages non lus et lus de fil d'actualité pour Android et FireOS
page_order: 3.1
platform: 
  - Android
  - FireOS
description: "Cet article de référence couvre les indicateurs de messages non lus et lus de fil d'actualité dans votre application Android ou FireOS."
channel:
  - fil d’actualité
  
---

# Indicateurs de messages non lus et lus

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

Braze vous permet de basculer entre les indicateurs de messages non lus et lus sur les cartes de fil d'actualité, comme illustré ci-dessous :

![Une carte de fil d’actualité affichant l’image d’une montre accompagnée d’un texte. Dans le coin supérieur du texte, on trouve un triangle bleu ou gris, indiquant si une carte a été lue ou non. Un triangle bleu signifie qu’une carte a été lue.][25]

## Activer les indicateurs

Pour activer cette fonctionnalité, ajoutez la ligne suivante à votre fichier `braze.xml` :

```xml
<bool name="com_braze_newsfeed_unread_visual_indicator_on">true</bool>
```

## Personnaliser les indicateurs

Ces indicateurs peuvent être personnalisés en modifiant les images `icon_read` et `icon_unread`.

[25]: {% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %}
