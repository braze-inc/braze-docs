---
nav_title: Style personnalisé
article_title: Style personnalisé de fil d’actualité pour iOS
platform: iOS
page_order: 0
description: "Cet article de référence montre comment implémenter des styles de fil d’actualités personnalisé à votre application iOS."
channel:
  - fil d’actualité

---

# Style personnalisé

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu - il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

L’intégration de `SDWebImage` est nécessaire si vous prévoyez d’utiliser notre interface utilisateur Braze pour afficher des images dans les messages in-app iOS, le fil d’actualités ou les cartes de contenu.

## Remplacer les images par défaut

Braze permet aux clients de remplacer les images par défaut existantes par leurs propres images personnalisées. Pour y parvenir, créez un nouveau fichier `png` avec l’image personnalisée et ajoutez-la à l’ensemble d’images de l’application. Renommez ensuite le fichier avec le nom de l’image pour remplacer l’image par défaut de notre bibliothèque. Assurez-vous également de télécharger les versions `@2x` et `@3x` des images pour permettre différentes tailles de téléphone. Les images pouvant être remplacées dans les cartes de contenu incluent : Les images disponibles pour un remplacement dans le fil d’actualité comprennent :

* Indicateur d’icône de lecture : `Icons_Read`
* Image de marque substitutive : `img-noimage-lrg`

{% alert important %} 
Le remplacement des images par défaut n’est actuellement pas pris en charge dans notre intégration Xamarin iOS. 
{% endalert %}

