---
nav_title: avril
page_order: 9
noindex: true
page_type: update
description: "Cet article contient les notes de version d’avril 2020."
---
# Avril 2020

## Partenariat avec Movable Ink

Movable Ink permet aux clients de Braze d’utiliser des fonctionnalités créatives intelligentes telles que des comptes à rebours, des sondages et des surfaces à gratter dans leurs campagnes de notification push, messages in-app et cartes de Contenu. L’intégration entre Movable Ink et Braze permet une approche plus complète pour les messages dynamiques axés sur les données, en offrant aux utilisateurs des éléments en temps réel sur les  choses importantes.

Commencez à [intégrer Movable Ink]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/movable_ink/) dans vos campagnes !

## Timing intelligent

Lors de la planification d'une campagne, vous pouvez utiliser [Timing Intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) (anciennement Intelligent Delivery) pour livrer votre message à chaque utilisateur au moment où Braze détermine qu'un individu est le plus susceptible de s'engager.

Les mises à jour de cette fonctionnalité comprennent :
- **Clarification des heures de silence**: La fonctionnalité Heures calmes reste inchangée, mais l’interface utilisateur a été modifiée pour être plus intuitive.
- **Ajout du graphique de prévisualisation**: Vous pouvez maintenant générer un graphique pour voir combien d’utilisateurs recevront des messages à chaque heure de la journée avec le timing intelligent, ainsi que la proportion d’utilisateurs ayant suffisamment de données pour pouvoir calculer leur moment d’envoi optimal.
- **Ajout d'un repli personnalisé**: Vous pouvez maintenant choisir l’heure locale à laquelle envoyer un message aux utilisateurs quand il n’y a pas assez de données sur l’engagement pour calculer un moment d’envoi optimal.

## Exportation de l’audience Facebook

Braze permet d’exporter manuellement vos utilisateurs à partir de la page Segments de Braze pour créer des publics Facebook personnalisés. Ceci est une exportation d'audience unique et statique et ne créera que de nouvelles [Audiences personnalisées Facebook]({{site.baseurl}}/partners/facebook/).

Actuellement disponible pour tous les clusters, un nouveau processus d’exportation d'audience de Braze vers Facebook existe, avec des étapes d’intégration simples qui rationalisent le processus. Vous n’aurez plus besoin de whitelister les URI OAuth Redirect pour envoyer des publics personnalisés, ou de modifier les paramètres de l’appli Facebook pour intégrer.

{% alert important %}
Notez que tous les clients utilisant actuellement Facebook Custom Audiences doivent réintégrer leurs segments Braze avec ces nouvelles étapes.
{% endalert%}


## Les mises à jour API du bloc de contenu et du modèle e-mail

Les [template/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) et [content_block/list]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) points de terminaison de l'API ont été mis à jour pour inclure un nouveau champ `tags`. Ce champ s’affichera sous forme de tableau, toutes les balises qui s’appliquent au modèle de bloc ou d’e-mail actuel.

## Adresse « De » personnalisée

Lors de la création d'un message électronique dans Braze, vous pouvez désormais personnaliser l'adresse de l'expéditeur du message dans la section **Informations d'envoi** de la composition de l'e-mail. Vous pouvez utiliser n'importe lequel de nos [tags de personnalisation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) pris en charge

![Adresse personnalisée de]({% image_buster /assets/img/personalized-from-name.png %}){: style="max-width:80%"}

