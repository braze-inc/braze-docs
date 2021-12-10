---
nav_title: Installer la campagne d'attribution
article_title: Comprendre les installations de l'utilisateur
page_order: 7
page_type: Référence
description: "Cet article de référence décrit les installations de l'utilisateur (installation de suivi d'attribution) et différentes façons d'appliquer cette information dans votre campagne."
tool:
  - Campagnes
  - Segments
---

# Comprendre les installations de l'utilisateur

> Cet article de référence dépasse le concept de l'utilisateur installe (installation de suivi d'attribution) et différentes façons d'appliquer cette information dans votre campagne.

Installer le suivi des attributions est un excellent moyen d'améliorer votre relation initiale avec votre utilisateur. Savoir comment, où et plus important encore, pourquoi un utilisateur installe votre application vous permet de mieux comprendre qui est votre utilisateur et comment vous devriez le présenter à votre application. Bien que Braze ne fournisse pas de suivi d'attribution d'installation, nous pouvons intégrer avec des services tels que Fiksu et Tune pour vous fournir des données d'installation de façon transparente.

## Segment de vos utilisateurs

Une fois que votre utilisateur installera votre application, vous pourrez commencer à les segmenter en fonction des [filtres d'attribution d'installation][2] suivants. Par exemple, une application de voyage pourrait ajouter des utilisateurs provenant d'une annonce relative aux offres de vacances sur la plage à un segment "Beach Lovers". De même, une application de musique pourrait segmenter les utilisateurs en fonction du genre de musique affiché dans la publicité qui a conduit à l'installation.

## Meilleures pratiques

### Intégration personnalisée

Maintenant que vous avez plus d'informations sur votre utilisateur, vous pouvez personnaliser leur processus d'intégration. Cela peut être aussi simple que de changer les images dans vos messages pour correspondre à leurs préférences, ou aussi complexe que la création d'un utilisateur unique pour chaque annonce qui pourrait conduire à une installation. Pour mettre à jour une séquence complète de messages qui peut prendre en compte le comportement de l'utilisateur, veuillez consulter notre documentation sur [Canvas][5]

### Données de référence de l'annonce

Les utilisateurs peuvent être attirés vers votre application par une offre promotionnelle ou un don. Grâce à l'installation des données d'attribution, vous pouvez envoyer des campagnes contenant des codes de réduction ou des offres aux seuls utilisateurs qui ont installé à cause de ces promotions. De la même manière, si votre annonce contient des informations sur un produit particulier (comme un film spécifique dans une application vidéo ou une vente dans une application eCommerce), vous pouvez envoyer des campagnes dirigant les utilisateurs vers la page correcte de votre application.

## Évaluer les efforts de publicité

L'installation de données d'attribution peut être précieuse pour évaluer l'efficacité des différentes campagnes de marketing. Pour savoir quelles publicités et quelles campagnes mènent au plus grand nombre d'installations, et qui sont en retard peut être utilisé pour concentrer vos ressources dans les publicités les plus convaincantes.
[3]: {% image_buster /assets/img_archive/install_onboarding.png %}

[2]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#install-attribution
[5]: {{site.baseurl}}/developer_guide/rest_api/messaging/#canvas
