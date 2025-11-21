---
nav_title: Emplacements/ciblage
article_title: Ciblage des emplacements
page_order: 10
page_type: tutorial
tool: 
- Segments
- Location
description: "Cet article pratique vous explique comment configurer le ciblage par emplacement, ce qui vous permet de segmenter les utilisateurs en fonction de leur emplacement/localisation."

---

# Emplacements/ciblage

> Cet article vous explique comment configurer le ciblage par emplacement/localisation, ce qui vous permet de segmenter les utilisateurs en fonction de leur emplacement le plus récent. C'est parfait si vous cherchez à mettre en place des campagnes et des stratégies basées sur l'emplacement/localisation.

## Étape 1 : Créez votre segmentation

Accédez à la page **Segments**, sous **Audience**, pour afficher tous vos segments d'utilisateurs actuels. Sur cette page, vous pouvez créer et nommer de nouvelles segmentations. Pour commencer, sélectionnez **Créer un segment** et donnez un nom à votre segment.

\![Fenêtre modale/boîte de dialogue modale, etc.]({% image_buster /assets/img_archive/createsegment2.png %}){: style="max-width:70%;"}

## Étape 2 : Personnalisez votre emplacement/localisation

Après avoir créé votre segmentation, ajoutez un filtre **Emplacement/localisation le plus récent** pour cibler les utilisateurs en fonction du dernier endroit où ils ont utilisé votre appli. Vous avez la possibilité de mettre en évidence les utilisateurs à l'intérieur ou à l'extérieur d'une région circulaire standard ou d'une région polygonale personnalisable.

!Filtre pour l'emplacement/localisation le plus récent à l'intérieur d'un cercle.]({% image_buster /assets/img_archive/filter_recent_location.png %})

{% tabs %}
{% tab Circular %}

### Régions circulaires

Pour les emplacements circulaires, vous pouvez déplacer l'origine et ajuster le rayon d'emplacement/localisation de votre segmentation.

[Tracé circulaire des villes situées entre le New Jersey et New York.]({% image_buster /assets/img_archive/location_circle.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Polygonal %}

### Régions polygonales

Pour les régions polygonales, vous pouvez désigner plus précisément les zones que vous souhaitez inclure dans votre segment.

Un contour de l'État de New York en tant que région polygonale sélectionnée.]({% image_buster /assets/img_archive/create_polygon.png %}){: style="max-width:70%;"}

{% endtab %}
{% endtabs %}

## Prise en charge des partenariats pour les balises et les géorepérages

En combinant la prise en charge des balises ou des géorepérages existants avec nos fonctionnalités de ciblage et d'envoi de messages, vous obtenez davantage d'informations sur les actions physiques de vos utilisateurs, ce qui vous permet de leur envoyer des messages en conséquence. Vous pouvez tirer parti de l'emplacement/localisation avec certains de nos partenaires : 

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion/)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)

