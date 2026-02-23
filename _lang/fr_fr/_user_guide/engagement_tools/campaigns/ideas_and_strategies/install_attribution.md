---
nav_title: Comprendre les installations utilisateur
article_title: Comprendre les installations utilisateur 
page_order: 7
page_type: reference
description: "Le présent article de référence décrit les installations utilisateur (suivi d’attribution d’installation) et différentes manières d’appliquer ces informations au sein de votre campagne."
tool:
  - Campaigns
  - Segments
---

# Comprendre les installations utilisateur

> Le suivi d’attribution d'installation est un excellent moyen d’améliorer votre relation initiale avec votre utilisateur. Savoir comment, où et, encore plus important, pourquoi un utilisateur installe votre application vous permet de mieux comprendre qui est votre utilisateur et comment vous devez lui présenter votre application. 

Bien que Braze ne fournisse pas de suivi d'attribution d'installation, nous pouvons intégrer des [services]({{site.baseurl}}/partners/message_orchestration/) tels que Branch et AppsFlyer pour vous fournir de façon fluide des données d'installation.

## Segmenter vos utilisateurs

Une fois que votre utilisateur installe votre application, vous pouvez commencer à le segmenter en fonction des [filtres d'attribution d'installation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#install-attribution) suivants. Par exemple, une application de voyage pourrait ajouter des utilisateurs provenant d’une publicité liée aux offres de vacances sur la plage dans un segment « Aiment la plage ». De même, une application musicale peut segmenter les utilisateurs en fonction du genre de musique affiché dans la publicité qui a entraîné l’installation.

## Bonnes pratiques

### Onboarding personnalisé

Maintenant que vous avez plus d’informations sur votre utilisateur, vous pouvez personnaliser son processus d’onboarding. Cela pourrait être aussi simple que de modifier les images de vos messages pour vous aligner sur leurs préférences ou aussi complexe que la création d’un onboarding utilisateur distinct pour chaque publicité qui pourrait entraîner une installation. Pour mettre à l'échelle une séquence complète de messages pouvant prendre en compte le comportement de l'utilisateur, reportez-vous à notre documentation sur [Canvas]({{site.baseurl}}/developer_guide/rest_api/messaging/#canvas).

### Données de référence de la publicité

Les utilisateurs peuvent être attirés sur votre application par une offre promotionnelle ou un cadeau. L’utilisation des données d’attribution d’installation vous permet d’envoyer des campagnes contenant des codes de réduction ou des offres uniquement aux utilisateurs qui ont installé en raison de ces promotions. De même, si votre annonce contient des informations sur un produit particulier (comme un film spécifique dans une application vidéo ou une vente dans une application d’e-commerce), vous pouvez envoyer des campagnes amenant les utilisateurs à la page correcte de votre application.

## Évaluer les efforts publicitaires

Les données d’attribution d'installation peuvent être utiles pour évaluer l’efficacité de différentes campagnes marketing. Le fait de voir quelles publicités et campagnes entraînent la plupart des installations et lesquelles sont moins efficaces peut être utilisé pour concentrer vos ressources sur les publicités les plus convaincantes.

