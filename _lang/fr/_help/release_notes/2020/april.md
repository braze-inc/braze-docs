---
nav_title: Avril
page_order: 9
noindex: true
page_type: update
description: "Cet article contient les notes de version d’avril 2020."
---
# Avril 2020

## Partenariat avec Movable Ink

Movable Ink permet aux clients de Braze d’utiliser des fonctionnalités créatives intelligentes telles que des comptes à rebours, des sondages et des surfaces à gratter dans leurs campagnes de notification push, messages in-app et cartes de Contenu. L’intégration entre Movable Ink et Braze permet une approche plus complète pour les messages dynamiques axés sur les données, en offrant aux utilisateurs des éléments en temps réel sur les  choses importantes.

Commencez à [intégrer Movable Ink]({{site.baseurl}}/partners/channel_extensions/creative_and_personalization/intelligent_creative/movable_ink/) dans vos campagnes !

## Timing Intelligent

Lorsque vous programmez une campagne, vous pouvez utiliser le [Timing Intelligent]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/) (précédemment appellé Intelligent Delivery) pour transmettre votre message à chaque utilisateur au moment où Braze détermine qu’une personne est la plus susceptible de s’engager.

Les mises à jour de cette fonctionnalité comprennent :
- **Clarification des heures calmes** : La fonctionnalité Heures calmes reste inchangée, mais l’interface utilisateur a été modifiée pour être plus intuitive.
- **Ajout du graphique d’aperçu** : Vous pouvez maintenant générer un graphique pour voir combien d’utilisateurs recevront des messages à chaque heure de la journée avec le timing intelligent, ainsi que la proportion d’utilisateurs ayant suffisamment de données pour pouvoir calculer leur moment d’envoi optimal.
- **Ajout de fallback personnalisé** : Vous pouvez maintenant choisir l’heure locale à laquelle envoyer un message aux utilisateurs quand il n’y a pas assez de données sur l’engagement pour calculer un moment d’envoi optimal.

## Exportation de l’audience Facebook

Braze permet d’exporter manuellement vos utilisateurs à partir de la page Segments de Braze pour créer des publics Facebook personnalisés. Il s’agit d’une exportation d’audience statique unique qui créera uniquement des nouvelles [audiences personnalisées Facebook]({{site.baseurl}}/partners/facebook/).

Actuellement disponible pour tous les clusters, un nouveau processus d’exportation de public de Braze vers Facebook existe, avec des étapes d’intégration simples qui rationalisent le processus. Vous n’aurez plus besoin de whitelister les URI OAuth Redirect pour envoyer des publics personnalisés, ou de modifier les paramètres de l’appli Facebook pour intégrer.

{% alert important %}
Notez que tous les clients utilisant actuellement Facebook Custom Audiences doivent réintégrer leurs segments Braze avec ces nouvelles étapes.
{% endalert%}


## Les mises à jour API du bloc de contenu et du modèle e-mail

Les endpoints de l’API [template/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) et [content_block/list]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) ont été mis à jour pour inclure un nouveau champ `tags`.  Ce champ s’affichera sous forme de tableau, tous les tags qui s’appliquent au modèle de bloc ou d’e-mail actuel.

## Adresse « De » personnalisée

Lors de la création d’un message e-mail dans Braze, vous pouvez désormais personnaliser l’adresse de l’expéditeur dans la section **Sending Info** (Envoi d’informations) du composeur d’e-mails. Vous pouvez utiliser l’un de nos [tags de personnalisation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) pris en charge

![Adresse « De » personnalisée][0]{: style="max-width:80%"}

[0]: {% image_buster /assets/img/personalized-from-name.png %}
