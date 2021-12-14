---
nav_title: Janvier
page_order: 12
noindex: vrai
page_type: Mettre à jour
description: "Cet article contient des notes de mise à jour pour janvier 2022."
---

# Janvier 2022

Bienvenue dans une nouvelle année !

## Mettre à jour pour exporter les utilisateurs par segment de terminaison

À partir de décembre 2021, les modifications suivantes prennent effet pour les [utilisateurs d'exporter par segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/):

1. Le champ `fields_to_export` dans cette requête API sera requis. L'option par défaut pour tous les champs sera supprimée.
2. Les champs pour `custom_events`, `achats`, `campagnes_received`, et `canvases_received` ne contiendra que les données des 90 derniers jours.

## Nouvelles propriétés pour les événements d'engagement de messages courants

De nouvelles propriétés ont été ajoutées pour la sélection des [événements d'engagement de message]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/). Cette mise à jour s'applique aux événements d'engagement de messages courants suivants et à tous les partenaires qui les utilisent :

- Ajouter `LINK_ID`, `LINK_ALIAS` à :
  - Clique sur l'email (toutes les destinations)
- Ajouter `USER_AGENT` à :
  - Courriel ouvert
  - Email Click
  - Email Marquer comme spam
- Ajouter `MACHINE_OPEN` à :
  - Courriel ouvert

## Nouveau tag de personnalisation Liquid

Nous supportons maintenant le ciblage des utilisateurs qui ont activé la poussée au premier plan sur leur appareil avec les balises Liquid suivantes :

{% raw %}
- `{{most_recently_used_device.${foreground_push_enabled}}}`
- `{{targted_device.${foreground_push_enabled}}}`
{% endraw %}

Pour plus d'informations, reportez-vous à [balises de personnalisation supportées]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

## Comprendre les webhooks

Les Webhooks sont des outils puissants et flexibles, mais ils peuvent être un peu déroutants. Si vous vous demandez quels sont les webhooks et comment vous pouvez les utiliser au Brésil, consultez notre nouvel article sur [Comprendre les webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/).

## Personnaliser Amazon

Amazon Personalize est comme avoir votre propre système de recommandation automatique Amazon pour toute la journée. Basé sur plus de 20 ans d'expérience dans les recommandations, La personnalisation d'Amazon vous permet d'améliorer l'engagement de vos clients en faisant fonctionner en temps réel des recommandations de produits et de contenu personnalisés et des promotions marketing ciblées.

Si vous souhaitez en savoir plus, visitez notre nouvel article [Amazon Personalize]({{site.baseurl}}/partners/message_personalization/dynamic_content/amazon_personalize/amazon_personalize/) pour comprendre les cas d'utilisation que Amazon Personnalise les offres, les données avec lesquelles il fonctionne, comment configurer le service et comment l'intégrer avec Braze.

## Nouveaux partenariats Braze

### Yotpo – commerce électronique

L'intégration de [Yotpo]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/yotpo/) et de Braze vous permet de tirer et d'afficher dynamiquement les notes des étoiles, les meilleurs commentaires, et le contenu visuel généré par les utilisateurs sur les produits dans les e-mails et les autres canaux de communication au Brésil. Vous pouvez également inclure des données de fidélisation au niveau du client dans les courriels et d'autres méthodes de communication pour créer une interaction plus personnalisée, boostant les ventes et fidélisation.

### Zeotap – Plateforme de données client

Avec l'intégration de [Zeotap]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/zeotap/) et de Braze, vous pouvez étendre l'échelle et la portée de vos campagnes en synchronisant les segments de clients de Zeotap pour associer les données utilisateur à Braze. Vous pouvez ensuite agir sur ces données, en fournissant des expériences ciblées personnalisées à vos utilisateurs.