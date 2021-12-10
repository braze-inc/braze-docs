---
nav_title: Personnalisation
article_title: Personnalisation des fils d'actualité pour iOS
platform: iOS
page_order: 5
description: "Cet article de référence couvre la façon de personnaliser votre flux d'actualités dans votre application iOS."
channel:
  - fil d'actualité
---

# Personnalisation

{% alert important %}
__Notez que l'intégration de `SDWebImage` est nécessaire si vous prévoyez d'utiliser notre interface utilisateur Braze pour afficher des images__ dans les messages In-App iOS, Flux d'actualités ou Cartes de contenu.
{% endalert %}

## Surcharge des images par défaut

Braze permet aux clients de remplacer les images existantes par leurs propres images personnalisées. Pour cela, créez un nouveau fichier `png` avec l'image personnalisée et ajoutez-le au lot d'images de l'application. Ensuite, renommez le fichier avec le nom de l'image (voir ci-dessous) pour remplacer l'image par défaut dans notre bibliothèque. Les images disponibles pour une substitution dans le fil d'actualité incluent :
* Lire l'indicateur d'icône : `Icons_Read`
* Image placeholder : `img-noimage-lrg`

{% alert note %} Assurez-vous de télécharger les versions `@2x` et `@3x` des images également pour s'adapter aux différentes tailles du téléphone. {% endalert %}

{% alert note %} Notez que le remplacement des images par défaut n'est actuellement pas pris en charge dans notre intégration Xamarin iOS. {% endalert %}
