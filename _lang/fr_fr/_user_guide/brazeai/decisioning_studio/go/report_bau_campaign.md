---
nav_title: Rapport sur la campagne BAU
article_title: Rapport sur la campagne BAU
page_order: 10
description: "Cet article apporte des réponses aux questions fréquemment posées sur l'établissement de rapports sur une campagne de type Business as Usual (BAU) dans le portail BrazeAI Decisioning Studio Go."
---

# Rapport sur la campagne "Business as Usual

> Cet article apporte des réponses aux questions fréquemment posées concernant l'établissement de rapports sur une campagne de type Business as Usual (BAU) dans le portail BrazeAI Decisioning Studio™ Go.

## A propos du rapport sur la campagne BAU

Par défaut, le rapport du portail BrazeAI Decisioning Studio™ Go comparera le groupe BrazeAI Decisioning Studio™ Go et le groupe de contrôle aléatoire. Outre la comparaison de ces deux groupes, il se peut que vous ayez un groupe Business as Usual (alias BAU) auquel vous aimeriez comparer les performances de BrazeAI Decisioning Studio™ Go. En configurant le reporting BAU, vous pouvez consulter les performances des trois groupes en un seul endroit dans le portail BrazeAI Decisioning Studio™ Go.

Le principal avantage de la mise en place du reporting BAU est l'application du filtrage des clics non valides de BrazeAI Decisioning Studio™ Go qui, lorsqu'il est appliqué aux trois groupes d'expérience, permet la comparaison des performances de clics la plus précise et la plus juste (ou " pommes à pommes ") en supprimant tout bruit supplémentaire provenant des clics présumés de la machine et des clics vers le lien de désabonnement.

## Conditions

Avant de mettre en place le reporting BAU, assurez-vous d'abord qu'il existe une comparaison de type " apples-to-apples " entre le groupe de traitement BAU, le BrazeAI Decisioning Studio™ Go et le groupe de contrôle aléatoire. Il s'agit notamment de vérifier que

- Aucun destinataire ne peut appartenir à plus d'un groupe (pendant toute la durée de l'expérience).
- Les destinataires sont répartis de manière aléatoire dans les groupes, de sorte qu'il n'y a pas de biais dans l'affectation des groupes.
- Toutes les options disponibles pour le groupe BAU (créativité, fréquence, temps, incitation ou offre) sont disponibles pour le BrazeAI Decisioning Studio™ Go et le groupe de contrôle aléatoire.

En l'absence d'un plan d'expérience "pommes à pommes", les rapports sur le BAU peuvent prêter à confusion ou induire en erreur.

Une fois que vous avez validé votre plan d'expérience, les informations suivantes sont nécessaires pour mettre en place le rapport BAU :
- Un ou plusieurs ID de campagne provenant de votre plateforme d'activation intégrée (Braze, Salesforce Marketing Cloud ou Klaviyo) où toutes les communications de la campagne sont des communications BAU.
    - Pour Braze, les campagnes et les toiles sont acceptées
    - Pour Salesforce Marketing Cloud, seuls les parcours sont acceptés.
    - Pour Klaviyo, seuls les flux sont acceptés.
- Un ID d'audience de votre plateforme d'activation intégrée qui suit les destinataires qui font partie de l'audience BAU chaque jour.
    - Pour Braze, seuls les segments sont acceptés.
    - Pour Salesforce Marketing Cloud, seules les extensions de données sont acceptées
    - Pour Klaviyo, seuls les segments sont acceptés

Si vous ne disposez pas d'une audience existante qui suit votre audience BAU, vous devez en créer une.

{% alert note %}
**Réservé aux clients de Braze :** Assurez-vous que votre exportation Braze Currents vers BrazeAI Decisioning Studio™ Go inclut les données de vos campagnes BAU.
{% endalert %}

## Considérations

À l'instar de BrazeAI Decisioning Studio™ Go plus généralement, le reporting BAU ne couvre que les KPI de clics, et non les KPI de conversion.

Pour l'instant, il n'est pas possible de filtrer sur des étapes du canvas ID spécifiques. Les événements de toutes les étapes du canvas seront inclus dans les données du BAU. Notez que cela risque d'invalider les comparaisons avec le BAU si seules certaines étapes du canvas doivent être prises en compte.

## Implanter une campagne BAU 

Suivez les instructions qui s'affichent sur votre portail BrazeAI Decisioning Studio™ Go. Vous devez avoir un ou plusieurs [ID de campagne et un ID d'audience.](#what-are-the-requirements-to-use-in-portal-bau-reporting)