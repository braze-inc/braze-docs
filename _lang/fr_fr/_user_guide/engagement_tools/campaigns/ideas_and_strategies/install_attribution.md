---
nav_title: "Comprendre l'installation des utilisateurs"
article_title: "Comprendre les installations d'utilisateurs" 
page_order: 7
page_type: reference
description: "Cet article de référence décrit les installations d'utilisateurs (suivi de l'attribution d'installation) et les différentes façons d'appliquer ces informations au sein de votre campagne."
tool:
  - Campaigns
  - Segments
---

# Comprendre l'installation des utilisateurs

> Le suivi de l'attribution d'installation est un excellent moyen d'améliorer votre relation initiale avec votre utilisateur. Savoir comment, où et, plus important encore, pourquoi un utilisateur installe votre application vous permet de mieux comprendre qui est votre utilisateur et comment vous devez lui présenter votre application. 

Bien que Braze ne fournisse pas de suivi d'attribution d'installation, nous pouvons nous intégrer à des [services]({{site.baseurl}}/partners/message_orchestration/) tels que Branch et AppsFlyer pour vous fournir de façon fluide/sans heurts, homogène, des données d'installation.

## Segmentez vos utilisateurs

Une fois que votre utilisateur installe votre application, vous pouvez commencer à le segmenter en fonction des [filtres d'attribution d'installation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#install-attribution) suivants. Par exemple, une application de voyage pourrait ajouter les utilisateurs issus d'une publicité relative à des offres de vacances à la plage à un segment "Amoureux de la plage". De même, une application musicale pourrait segmenter les utilisateurs en fonction du genre de musique affiché dans la publicité qui a conduit à l'installation.

## Meilleures pratiques

### Onboarding personnalisé

Maintenant que vous disposez de plus d'informations sur votre utilisateur, vous pouvez personnaliser son processus d'onboarding. Cela peut être aussi simple que de changer les images de vos messages pour les adapter à leurs préférences, ou aussi complexe que de créer un onboarding utilisateur unique pour chaque annonce qui pourrait conduire à une installation. Pour mettre à l'échelle une séquence complète de messages pouvant prendre en compte le comportement de l'utilisateur, reportez-vous à notre documentation sur [Canvas]({{site.baseurl}}/developer_guide/rest_api/messaging/#canvas).

### Données de référence de l'annonce

Les utilisateurs peuvent être attirés vers votre application par une offre promotionnelle ou un cadeau. L'utilisation des données d'attribution d'installation vous permet d'envoyer des campagnes contenant des codes de promotion ou des offres aux seuls utilisateurs qui se sont installés grâce à ces promotions. De la même manière, si votre annonce contient des informations sur un produit particulier (comme un film spécifique dans une appli vidéo ou une vente dans une appli de commerce électronique), vous pouvez envoyer des campagnes dirigeant les utilisateurs vers la bonne page de votre appli.

## Évaluer les efforts publicitaires

Les données d'attribution d'installation peuvent être précieuses pour évaluer l'efficacité de différentes campagnes marketing. En examinant les annonces et les campagnes qui conduisent au plus grand nombre d'installations et celles qui sont à la traîne, vous pouvez concentrer vos ressources sur les annonces les plus convaincantes.

