---
nav_title: décembre
page_order: 0
noindex: true
page_type: update
description: "Cet article contient les notes de version de décembre 2021."
alias: "/help/release_notes/2022/january/"
---
# Décembre 2021

## Mise à jour de l’endpoint d’exportation des utilisateurs

À partir de décembre 2021, les modifications suivantes entreront en vigueur pour le point de terminaison [Export users by segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) :

1. Le champ `fields_to_export` sera requis dans cette requête API. L’option « Tous les champs par défaut » sera supprimée.
2. Les champs pour `custom_events`, `purchases`, `campaigns_received` et `canvases_received` contiendront uniquement les données des 90 derniers jours.

## Nouvelles propriétés pour les événements d’engagement sur les messages Currents

De nouvelles propriétés ont été ajoutées pour sélectionner [les événements d'engagement des messages]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/). Cette mise à jour s’applique aux événements d’engagement sur les messages Currents suivants et à tous les partenaires qui les utilisent :

- Ajouter `LINK_ID`, `LINK_ALIAS` à :
  - Clic sur E-mail (toutes les destinations)
- Ajouter `USER_AGENT` à :
  - Ouverture d'e-mails
  - Clics sur e-mails
  - E-mails marqués comme spam
- Ajouter `MACHINE_OPEN` à :
  - Ouverture d'e-mails

## Nouvelle balise de personnalisation Liquid

Nous prenons désormais en charge le ciblage des utilisateurs qui ont activé les notifications push lorsque l’application est au premier plan, via les balises Liquid suivantes :

{% raw %}
- `{{most_recently_used_device.${foreground_push_enabled}}}`
- `{{targeted_device.${foreground_push_enabled}}}`
{% endraw %}

Pour plus d'informations, consultez [les balises de personnalisation prises en charge]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

## À propos des webhooks

Les webhooks sont des outils puissants et flexibles, mais ils peuvent être un peu déroutants. Si vous vous demandez ce que sont les webhooks et comment vous pouvez les utiliser dans Braze, consultez notre nouvel article sur [À propos des webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/).

## Amazon Personalize

Amazon Personalize, c'est comme si vous disposiez de votre propre système de recommandation Amazon machine learning ouvert toute la journée. Avec ses 20 ans et plus d’expérience en recommandation, Amazon Personalize vous permet d’améliorer l’engagement client en mettant en œuvre des recommandations personnalisées en temps réel sur les produits et le contenu et les promotions marketing ciblées. 

Si vous souhaitez en savoir plus, consultez notre nouvel article [Amazon Personalize]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalized_recommendations/amazon_personalize) pour comprendre les cas d'utilisation qu'Amazon Personalize propose, les données avec lesquelles il fonctionne, comment configurer le service et comment l'intégrer avec Braze.

## Nouveaux partenariats Braze

### Yotpo – eCommerce

L'intégration [Yotpo]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/yotpo/) et Braze vous permet de récupérer et d'afficher dynamiquement les évaluations par étoiles, les meilleures critiques et le contenu visuel généré par les utilisateurs sur les produits dans les e-mails et autres canaux de communication au sein de Braze. Vous pouvez également inclure les données de fidélisation des clients dans les e-mails et autres méthodes de communication pour créer une interaction plus personnalisée, ce qui stimule les ventes et la fidélisation.

### Zeotap – Plateforme de données client

Avec l'intégration de [Zeotap]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/zeotap/) et Braze, vous pouvez étendre l'échelle et la portée de vos campagnes en synchronisant les segments de clients Zeotap pour mapper les données utilisateur de Zeotap aux comptes utilisateurs de Braze. Vous pouvez ensuite vous servir de ces données pour offrir des expériences personnalisées et ciblées à vos utilisateurs.