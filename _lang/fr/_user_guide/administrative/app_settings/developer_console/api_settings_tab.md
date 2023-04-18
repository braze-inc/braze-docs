---
nav_title: Paramètres API
article_title: Paramètres API
page_order: 0
page_type: reference
description: "Cet article de référence couvre la page API Settings (Paramètres API), qui affiche les identifications API pour votre groupe d’apps."

---

# Paramètres API

> Les **API Settings** (Paramètres API) affichent les identifications API pour votre groupe d’apps. La première section sur **Services** répertorie les articles pertinents pour différentes utilisations de l’API Braze ([User Data (Données utilisateur)][3],[Messaging (Envoi de messages)][4], [Email Sync][5] (Synchronisation par e-mail) ou [Export][6] (Exporter)).

La page **API Settings** (Paramètres API) comporte les sections suivantes :

- Clés API REST
- Identification
- Identifiants API supplémentaires

### Clés API REST

Cette section fournit les clés API REST du groupe d’apps, les identifiants uniques qui vous permettent d’accéder à vos données pour un groupe d’apps. Une clé API REST est requise pour chaque demande de l’API Braze. Pour plus d’informations sur la création et l’utilisation des clés API, consultez notre [présentation de la clé API REST]({{site.baseurl}}/api/api_key/).

#### Liste d’adresses IP autorisées

Pour renforcer la sécurité, vous pouvez spécifier une liste d’adresses IP et de sous-réseaux autorisés à faire des requêtes API REST pour une clé API REST spécifique. C’est ce que l’on appelle une « liste autorisée » ou « liste blanche ». Pour autoriser des adresses IP ou des sous-réseaux spécifiques, ajoutez-les dans la section **Liste blanche d’adresses IP** lors de la création d’une clé API REST : 

![Section API IP Whitelisting (Whiteliste des adresses IP API) de création d’une nouvelle clé API][26]

Si vous n’en spécifiez aucune, les requêtes pourront être envoyées depuis n’importe quelle adresse IP.

{% alert tip %}
Vous créez un Webhook Braze à Braze en utilisant une liste blanche ? Consultez notre liste [d’adresses IP à autoriser]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting).
{% endalert %}

### Identification

Cette section comprend une liste d’identifiants utilisés pour référencer des applications spécifiques dans les demandes faites à l’API Braze. Pour en savoir plus sur les identifiants d’application, consultez [Clé API de l’identifiant de l’application]({{site.baseurl}}/api/identifier_types/).

### Identifiants API supplémentaires

Pour intégrer notre API, vous pouvez rechercher les identifiants liés à tous les segments, campagnes, cartes de contenu et autres, auxquels vous souhaitez accéder à partir de l’API externe de Braze. Tous les messages doivent suivre le codage [UTF-8][12]. Une fois que vous avez sélectionné l’un d’eux, l’identifiant s’affichera sous le menu déroulant.

Pour plus d’informations, consultez la rubrique [Types d’identifiant API]({{site.baseurl}}/api/identifier_types/).

[3]: {{site.baseurl}}/api/endpoints/user_data/
[4]: {{site.baseurl}}/api/endpoints/messaging/
[5]: {{site.baseurl}}/api/endpoints/email/
[6]: {{site.baseurl}}/api/endpoints/export/
[12]: https://en.wikipedia.org/wiki/UTF-8 "Wikipedia: UTF-8"
[26]: {% image_buster /assets/img_archive/api-key-ip-whitelisting.png %}
