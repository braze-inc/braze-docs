---
nav_title: Avril
page_order: 9
noindex: vrai
page_type: Mettre à jour
description: "Cet article contient des notes de mise à jour pour avril 2020."
---

# Avril 2020

## Partenariat Movable Ink

Movable Ink fournit aux clients Braze la possibilité d'utiliser des fonctionnalités intelligentes de création comme __Minuterie à rebours, Sondages et Scratch Off dans leurs campagnes Push, Message In-App et Content Card__. Movable Ink and Braze power a more rounded approach to dynamic data driven messages, providing users with real-time elements about the things that important.

Pour plus d'informations sur la façon de commencer à intégrer Movable Ink dans vos campagnes, consultez notre [documentation]({{site.baseurl}}/partners/channel_extensions/creative_and_personalization/intelligent_creative/movable_ink/).

## Timing Intelligent

Lors de la planification d'une campagne, vous pouvez utiliser le Timing Intelligent (précédemment Intelligent Delivery) pour envoyer votre message à chaque utilisateur au moment où Braze détermine qu'un individu est le plus susceptible d'engager.

Les mises à jour de cette fonctionnalité incluent :
- __Clarification of Quiet Hours__ - La fonctionnalité Heures silencieuses reste la même, or l'interface a été ajustée pour clarification.
- __Ajout du graphique de prévisualisation__ - vous pouvez maintenant générer un graphique pour voir combien d'utilisateurs recevront des messages pour chaque heure de la journée avec le Timing intelligent, ainsi que la proportion d'utilisateurs ont assez de données pour calculer un temps optimal.
- __Ajout de la fonction de repli personnalisé__ - vous pouvez maintenant choisir l'heure locale à laquelle envoyer un message aux utilisateurs lorsqu'ils manquent de données d'engagement suffisantes pour calculer un temps optimal

Consultez notre [documentation]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/) pour plus d'informations.

## Exportation de l'audience Facebook

Braze fournit la possibilité d'exporter manuellement vos utilisateurs depuis la page des segments de Braze pour créer des audiences personnalisées Facebook. Ceci est une exportation statique unique et ne créera que de nouveaux publics personnalisés Facebook.

__Actuellement disponible pour toutes les Clusters__, un nouveau processus d'exportation de Braze sur Facebook existe et simplifie le processus avec de simples étapes d'intégration. Vous n'aurez plus besoin de mettre en liste blanche les URI de redirection OAuth pour envoyer des audiences personnalisées ou des gâchis dans les paramètres de l'application Facebook pour les intégrer.

{% alert important %}
__Veuillez noter que tous les clients qui utilisent actuellement des audiences personnalisées Facebook, DOIVENT réintégrer leurs Segments Braze avec ces nouvelles étapes.__
{% endalert%}

Pour accéder aux nouvelles étapes simplifiées d'exportation de l'audience Facebook, consultez notre documentation [ici]({{site.baseurl}}/partners/facebook/).

## Mises à jour du bloc de contenu et du modèle d'e-mail API

Les points de terminaison de l'API [template/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) et [content_block/list]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) ont été mis à jour pour inclure un nouveau champ `balises`. Ce champ sera listé sous la forme d'un tableau, toutes les balises qui s'appliquent au bloc actuel ou au modèle d'e-mail.

## Adresse de départ personnalisée

Lors de la création d'un message de courriel dans Braze, vous pouvez maintenant personnaliser l'adresse d'expédition du message dans la section « Infos d'envoi » de la composition du courriel. Vous pouvez utiliser l'un de nos [tags de personnalisation pris en charge]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)

!\[Adresse personnalisée \]\[0\]{: style="max-width:80%"}
[0]: {% image_buster /assets/img/personalized-from-name.png %}
