---
nav_title: Ciblage de localisation
article_title: Ciblage de localisation
page_order: 6.5
page_type: tutorial
tool: 
- Segments
- Localisation
description: "Cet article pratique vous explique comment configurer le ciblage de localisation pour segmenter des utilisateurs en fonction de leur emplacement."

---

# Ciblage de localisation

> Cet article vous explique comment configurer le ciblage de localisation pour segmenter des utilisateurs en fonction de leur dernière localisation enregistrée. Le ciblage de localisation est une option idéale si vous envisagez de lancer des campagnes et des stratégies basées sur la localisation.

## Étape 1 : Créez votre segment

Accédez à la page **Segments**, dans **Engagement**, pour afficher tous vos segments d’utilisateurs actuels. Sur cette page, vous pouvez créer et nommer de nouveaux segments. Pour commencer, cliquez sur **Create Segment (Créer un segment)** et nommez votre segment.

![][1]{: style="max-width:70%;"}

## Étape 2 : Personnalisez votre emplacement

Après avoir créé votre segment, ajoutez un filtre **Most Recent Location (Localisation la plus récente)** pour cibler les utilisateurs en fonction du dernier emplacement où ils ont utilisé votre application. Vous pouvez sélectionner des utilisateurs dans une région circulaire standard ou dans une région polygonale personnalisable.

![][2]

### Régions circulaires

Avec les régions circulaires, vous pouvez déplacer l’origine et ajuster le rayon de votre segmentation.

![Un aperçu circulaire des villes entre New Jersey et New York.][3]{: style="max-width:70%;"}

### Régions polygonales

Avec les régions polygonales, vous pouvez désigner les zones que vous souhaitez inclure dans votre segment de manière plus précise.

![Un aperçu de l’état de New York sélectionné en tant que région polygonale.][4]{: style="max-width:70%;"}

{% alert tip %}
Vous souhaitez tirer parti du ciblage de localisation avec l’aide d’un partenaire Braze ? Découvrez les [partenaires de localisation contextuelle]({{site.baseurl}}/partners/message_personalization/location/) de Braze.
{% endalert %}

[1]: {% image_buster /assets/img_archive/createsegment2.png %}
[2]: {% image_buster /assets/img_archive/filter_recent_location.png %}
[3]: {% image_buster /assets/img_archive/location_circle.png %}
[4]: {% image_buster /assets/img_archive/create_polygon.png %}
