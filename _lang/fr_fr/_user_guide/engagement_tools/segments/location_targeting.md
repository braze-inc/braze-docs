---
nav_title: Ciblage de localisation
article_title: Ciblage de localisation
page_order: 6.5
page_type: tutorial
tool: 
- Segments
- Location
description: "Cet article pratique vous explique comment configurer le ciblage de localisation pour segmenter des utilisateurs en fonction de leur emplacement."

---

# Ciblage de localisation

> Cet article vous explique comment configurer le ciblage de localisation pour segmenter des utilisateurs en fonction de leur dernière localisation enregistrée. Le ciblage de localisation est une option idéale si vous envisagez de lancer des campagnes et des stratégies basées sur la localisation.

## Étape 1 : Créez votre segment

Accédez à la page **Segments**, sous **Audience**, pour afficher tous vos segments d'utilisateurs actuels. Sur cette page, vous pouvez créer et nommer de nouveaux segments. Pour commencer, cliquez sur **Créer un segment** et donnez un nom à votre segment.

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), **les segments se** trouvent sous **Engagement.**
{% endalert %}

![][1]{: style="max-width:70%;"}

## Étape 2 : Personnalisez votre emplacement

Une fois que vous avez créé votre segmentation, ajoutez un filtre **Emplacement/localisation le plus récent** pour cibler les utilisateurs en fonction du dernier endroit où ils ont utilisé votre appli. Vous pouvez sélectionner des utilisateurs dans une région circulaire standard ou dans une région polygonale personnalisable.

![][2]

### Régions circulaires

Avec les régions circulaires, vous pouvez déplacer l’origine et ajuster le rayon de votre segmentation.

![Un contour circulaire des villes situées entre le New Jersey et New York.][3]{: style="max-width:70%;"}

### Régions polygonales

Avec les régions polygonales, vous pouvez désigner les zones que vous souhaitez inclure dans votre segment de manière plus précise.

![Un contour de l'État de New York comme région polygonale sélectionnée.][4]{: style="max-width:70%;"}

## Prise en charge des partenariats pour les balises et les géorepérages

En combinant la prise en charge des balises ou des géorepérages existants avec nos fonctionnalités de ciblage et d'envoi de messages, vous obtenez davantage d'informations sur les actions physiques de vos utilisateurs, ce qui vous permet de leur envoyer des messages en conséquence. Vous pouvez tirer parti de l'emplacement/localisation avec certains de nos partenaires : 

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion/)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)

[1]: {% image_buster /assets/img_archive/createsegment2.png %}
[2]: {% image_buster /assets/img_archive/filter_recent_location.png %}
[3]: {% image_buster /assets/img_archive/location_circle.png %}
[4]: {% image_buster /assets/img_archive/create_polygon.png %}
