---
nav_title: API et identifiants
article_title: API et identifiants
page_order: 3
page_type: reference
description: "Cet article traite de la page API et identifiants, qui affiche les identifications d'API pour votre espace de travail."

---

# clés API

> La page **API et identifiants** est votre centre de gestion centralisée de toutes vos clés d'API REST. Ici, vous pouvez accéder à l'ensemble des clés API et des identifiants d'applications de chaque espace de travail.

Vous trouverez la page **API et identifiants** sous **Paramètres**.

### clés API

Cette section fournit les clés API REST de votre espace de travail, les identifiants uniques qui vous permettent d'accéder à vos données pour un espace de travail. Une clé API REST est requise pour chaque demande adressée à l'API de Braze. Pour plus d'informations sur la création et l'utilisation des clés API, consultez notre [aperçu des clés API REST]({{site.baseurl}}/api/api_key/).

#### Liste d'autorisation des IP de l'API

Pour plus de sécurité, vous pouvez spécifier une liste d'adresses IP et de sous-réseaux autorisés à effectuer des demandes d'API REST pour une clé d'API REST donnée. C'est ce que l'on appelle la liste d'autorisation ou la liste blanche. Pour autoriser des adresses IP ou des sous-réseaux spécifiques, ajoutez-les à la section **Liste blanche des IP** lors de la création d'une nouvelle clé API REST : 

!Section de la liste blanche des adresses IP de l'API lors de la création d'une nouvelle clé API]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

Si vous n'en spécifiez pas, les demandes peuvent être envoyées à partir de n'importe quelle adresse IP.

{% alert tip %}
Créer un webhook Braze à Braze et utiliser allowlisting ? Consultez notre liste d'[adresses IP à mettre sur liste blanche.]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting)
{% endalert %}

### Identifiants de l'application

Cette section comprend une liste d'identifiants utilisés pour référencer des apps spécifiques dans les demandes adressées à l'API de Braze. Pour en savoir plus sur les identificateurs [d']({{site.baseurl}}/api/identifier_types/)application, reportez-vous à la [clé API d'identification d'application.]({{site.baseurl}}/api/identifier_types/)

### Autres identifiants

Pour intégrer notre API, vous pouvez rechercher les identifiants liés à tous les segments, campagnes, cartes de contenu et autres auxquels vous souhaitez accéder à partir de l'API externe de Braze. Tous les messages doivent respecter le codage [UTF-8](https://en.wikipedia.org/wiki/UTF-8). Après avoir sélectionné l'un d'entre eux, l'identifiant sera affiché sous le menu déroulant.

Pour plus d'informations, reportez-vous aux [types d'identifiants API]({{site.baseurl}}/api/identifier_types/).

