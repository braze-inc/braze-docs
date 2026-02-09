---
nav_title: API et identifiants
article_title: API et identifiants
page_order: 3
page_type: reference
description: "Cet article traite de la page API et identifiants, qui affiche les identifications d'API pour votre espace de travail."

---

# Clés API

> La page **API et identifiants** est votre centre de gestion centralisée de toutes vos clés d'API REST. Ici, vous pouvez accéder à l'ensemble des clés API et des identifiants d'applications de chaque espace de travail.

Vous trouverez la page **API et identifiants** sous **Paramètres**.

## Clés API

Cette section fournit les clés API REST de votre espace de travail, les identifiants uniques qui vous permettent d'accéder à vos données pour un espace de travail. Une clé API REST est requise pour chaque demande de l’API Braze. Pour plus d'informations sur la création et l'utilisation des clés API, consultez notre [présentation des clés API REST]({{site.baseurl}}/api/api_key/).

### Liste d’adresses IP autorisées

Pour renforcer la sécurité, vous pouvez spécifier une liste d’adresses IP et de sous-réseaux autorisés à faire des requêtes API REST pour une clé API REST spécifique. Vous définissez pour cela une liste d’autorisations, également appelée « Liste blanche ». Pour autoriser des adresses IP ou des sous-réseaux spécifiques, ajoutez-les à la section **Liste blanche des IP** lors de la création d'une nouvelle clé API REST : 

![Section API IP Whitelisting (Whiteliste des adresses IP API) de création d’une nouvelle clé API]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

Si vous n’en spécifiez aucune, les requêtes pourront être envoyées depuis n’importe quelle adresse IP.

{% alert tip %}
Vous créez un Webhook Braze à Braze en utilisant une liste blanche ? Consultez notre liste d'[adresses IP à mettre sur liste blanche.]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting)
{% endalert %}

### Alertes sur l'utilisation de l'API

Mettez en place des alertes d'utilisation de l'API pour surveiller l'activité de l'API clé et repérer rapidement les problèmes. Ces alertes vous aident à détecter des modèles de trafic inattendus avant qu'ils n'aient un impact sur votre expérience.

Vous pouvez suivre deux types d'activité API :

- **Les endpoints de l'API REST :** Des actions telles que l'envoi de messages, la création de campagnes ou l'exportation de données.
- **Demandes d'API du SDK :** Les événements de votre expérience sur client, tels que le déclenchement de messages in-app ou la synchronisation des profils utilisateurs. *Cette fonctionnalité est disponible si vous avez acheté des utilisateurs actifs par mois (CY 24-25).*

Une fois que vous avez choisi les éléments à suivre, vous pouvez définir des conditions d'alerte. Par exemple, vous serez informé si les réponses aux erreurs augmentent de 20 % en l'espace d'une heure. Vous recevrez une notification par e-mail, par webhook ou les deux, en fonction de vos paramètres. Pour commencer, consultez les [alertes d'utilisation de l'API]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_alerts/).

## Identifiants de l'application

Cette section comprend une liste d’identifiants utilisés pour référencer des applications spécifiques dans les demandes faites à l’API Braze. Pour en savoir plus sur les identifiants d’application, consultez [Clé API de l’identifiant de l’application]({{site.baseurl}}/api/identifier_types/).

## Autres identifiants

Pour intégrer notre API, vous pouvez rechercher les identifiants liés à tous les segments, campagnes, cartes de contenu et autres auxquels vous souhaitez accéder à partir de l'API externe de Braze. Tous les messages doivent respecter le codage [UTF-8.](https://en.wikipedia.org/wiki/UTF-8)  Une fois que vous avez sélectionné l’un d’eux, l’identifiant s’affiche sous le menu déroulant.

Pour plus d'informations, reportez-vous aux [types d'identifiants API]({{site.baseurl}}/api/identifier_types/).

